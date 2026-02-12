import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import anvil.pdf


@anvil.server.callable
def get_all_orders():
  return app_tables.tblorders.search()

@anvil.server.callable
def get_all_orders_from_orderitems():
  return app_tables.tblorderitems.search()

@anvil.server.callable
def get_all_order_info(): 
  combined = []
  for item in app_tables.tblorderitems.search():
    order = item["order_id"]      
    if not order:
      continue
    try:
      user = order["user"]  
      if not user:
        continue 

    # Building one combined dictionary 
      combined.append({
        "order_row": order,

        "customer": f"{user['firstname']} {user['surname']}",
        "order_id": order["order_id"],
        "collection_date": order["collection_date"],
        "order_status": order["order_status"],
        "date_of_order": order["date_of_order"],
        "total_price": order["total_price"],

        # Order item details
        "cake_type": item["cake_type"],
        "sponge_flavour": item["sponge_flavour"],
        "filling": item["filling"],
        "frosting_type": item["frosting_type"],
        "frosting_flavour": item["frosting_flavour"],
        "occasion": item["occasion"],
        "serving_size": item["serving_size"],
        "no_of_tiers": item["no_of_tiers"],
        "allergies": item["allergies"],
        "inscription": item["inscription"],
        "additional_details": item["additional_details"],
        "reference_image": item["reference_image"]
      })
    # Stops a row being deleted from causing problems or if data doesn't match up
    except tables.TableError:
      continue
  return combined


@anvil.server.callable
def confirm_order_status(order):
  if order["order_status"] == "Pending":
    order["order_status"] = "Confirmed"
    order.update()

  # Sending an email so they know their order is being made
  customer = order["user"]
  anvil.email.send(
    to = customer["email"], 
    from_address = "CakesBakesCardiff", 
    subject = "Order Confirmation", 
    text = f"""Hello {customer["firstname"]}, \nYour order has been confirmed! 
It is now in the process of being made."""
  )
  return order

@anvil.server.callable
def reject_order_status(order, rejection):
  if order["order_status"] == "Pending":
    order["order_status"] = "Rejected"
    order["rejection_reason"] = rejection
    order.update()

  # Sending an email to the customer informing them of the rejection
  customer = order["user"]
  if customer:
    anvil.email.send(
      to = customer["email"], 
      from_address = "CakesBakesCardiff", 
      subject = "Order Rejection", 
      # Using the rejection reason in the email so they are aware of why it was rejected
      text = f""" Unfortunately, your order has been rejected due to the following
      reason: {rejection}."""
    )
    return order

@anvil.server.callable
def mark_order_as_complete(order):
  if order['order_status'] == "Pending":
    order['order_status'] = "Completed"
    order.update()  


@anvil.server.callable
def display_order(order):
  cakes = app_tables.tblorderitems.search(order_id = order)
  return cakes


@anvil.server.callable
def check_weekly_orders():
  today = datetime.datetime.now()
  days_since_monday = today.weekday()
  start = today - datetime.timedelta(days = days_since_monday)
  weekly_orders = app_tables.tblorders.search('date_of_order' >= start)
  return len(weekly_orders)

@anvil.server.callable
def get_week(selected_date):
  # selected_date.weekday is the number corresponding to the day of the week
  start_of_week = selected_date - datetime.timedelta(days = selected_date.weekday())
  # datetime.delta calculated the difference in days
  end_of_week = start_of_week + datetime.timedelta(days=6)
  return start_of_week, end_of_week

@anvil.server.callable
def get_weekly_stats(start_of_week, end_of_week):
  orders = app_tables.tblorders.search()
  total_items = 0
  cancelled = 0
  rejected = 0
  income = 0

  for order in orders:
    order_date = order["date_of_order"].date()
    # If order date is in within the start and end date, the order count increases
    if start_of_week <= order_date <= end_of_week:
      total_items = total_items + 1
      if order["order_status"] == "Cancelled":
        cancelled = cancelled + 1
      elif order["order_status"] == "Rejected":
        rejected = rejected + 1
      income = income + order["total_price"]

  # returns a dictionary of order information
  return {
    "total items" : total_items, 
    "cancelled" : cancelled,
    "rejected" : rejected, 
    "income" : income
  }

@anvil.server.callable
def get_reasons(start_of_week, end_of_week):
  orders = app_tables.tblorders.search()
  reason_count = {
    "Too complex" : 0,
    "Too complex for the given time" : 0,
    "Unable to take more orders" : 0,
    "not offering the requested flavours" : 0,
    "Event was postponed or cancelled" : 0,
    "Collection date was no longer suitable" : 0,
    "Allergies or dietary requirements changed" : 0,
    "Changed mind on the cake design and flavour" : 0,
    "Other" : 0
  }

  # Loops through orders to increment the cancellation or rejection reasons
  for order in orders:
    order_date = order["date_of_order"].date()
    if start_of_week <= order_date <= end_of_week:
      if order["order_status"] == "Rejected":
        reason = order["rejection_reason"]
      elif order["order_status"] == "Cancelled":
        reason = order["cancellation_reason"]
      else:
        reason = None

      if reason is not None:
        if reason in reason_count:
          reason_count[reason] = reason_count[reason] + 1

  return reason_count

@anvil.server.callable
def marked_date_check(selected_date):
  row = app_tables.tblunavailability.get(unavailability_date = selected_date)
  return row 

@anvil.server.callable
def add_unavailable_date(selected_date, reason):
  user = anvil.users.get_user()
  app_tables.tblunavailability.add_row(staff_id = user, 
                                       unavailability_date = selected_date, 
                                       reason = reason)

# Sending an invoice as a PDF
@anvil.server.callable
def create_invoice(order):
  pdf = anvil.pdf.render_form("Invoice", order = order)
  return pdf

@anvil.server.callable
def send_invoice(order):
  user = order["order_row"]["user"]
  email = user["email"]
  pdf = create_invoice(order)
  anvil.email.send(
    from_address = "CakesBakesCardiff",
    from_name = "Invoice",
    to = email,
    subject = "Your order",
    text = "Thank you for your order. Here is your invoice: ",
    attachments = pdf
  )
  return pdf