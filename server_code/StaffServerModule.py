import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime


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
    order = item['order_id']      
    user = order['user']      

    # Building one combined dictionary 
    combined.append({
      'order_row': order,
      
      'customer': f"{user['firstname']} {user['surname']}",
      'order_id': order['order_id'],
      'collection_date': order['collection_date'].strftime("%d/%m/%Y"),
      'order_status': order['order_status'],
      'date_of_order': order['date_of_order'].strftime("%d/%m/%Y"),
      'total_price': order['total_price'],

      # Order item details
      'cake_type': item['cake_type'],
      'sponge_flavour': item['sponge_flavour'],
      'filling': item['filling'],
      'frosting_type': item['frosting_type'],
      'frosting_flavour': item['frosting_flavour'],
      'occasion': item['occasion'],
      'serving_size': item['serving_size'],
      'no_of_tiers': item['no_of_tiers'],
      'allergies': item['allergies'],
      'inscription': item['inscription'],
      'additional_details': item['additional_details'],
      'reference_image': item['reference_image']
    })
  return combined

  
@anvil.server.callable
def confirm_order_status(order):
 # orders = app_tables.tblorders.search(order_id = order_id)
  #for order in orders:
    if order['order_status'] == "Pending":
      order['order_status'] = "Confirmed"
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
  #orders = app_tables.tblorders.search(order_id = order_id)
  #for order in orders:
    if order['order_status'] == "Pending":
      order['order_status'] = "Rejected"
      order['rejection_reason'] = rejection
      order.update()
      
    # Sending an email to the customer informing them of the rejection
    customer = order["user"]
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

  