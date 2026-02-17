import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import datetime
import random

# Generating an order id to be visible and later referenced in invoices etc
# This is done using the random library
@anvil.server.callable
def generate_order_id():
  while True:
   order_id = random.randint(100000, 999999)
   existing_id = app_tables.tblorders.get(order_id = order_id)
   if existing_id is None:
    return order_id

# Adding Standard cakes to the customer's order
@anvil.server.callable
def add_standard_cake(order, cake_type, occasion, no_of_tiers, frosting_type, frosting_flavour, price, 
                      serving_size, sponge_flavour, filling):
  user = anvil.users.get_user()
  if not user:
    return
  app_tables.tblorderitems.add_row(order_id = order, cake_type = cake_type, occasion = occasion, 
                                   no_of_tiers = no_of_tiers, frosting_type = frosting_type, 
                                   frosting_flavour = frosting_flavour, price = price, 
                                   serving_size = serving_size, 
                                   sponge_flavour = sponge_flavour, filling = filling)

# Adding a custom cake to the customer's order
@anvil.server.callable
# Takes all user inputs
def add_custom_cake(cake_type, occasion, no_of_tiers, frosting_type, frosting_flavour, price, 
                    serving_size, sponge_flavour, filling, allergies, additional_details, inscription, 
                    reference_image, collection_date):
  user = anvil.users.get_user()
  if not user:
    return
  order_id_number = generate_order_id()
  # Adds a new order to the database
  order = app_tables.tblorders.add_row(order_id = order_id_number, 
                                      user = user, 
                                      date_of_order = datetime.datetime.now(),
                                      collection_date = collection_date,
                                      order_status = "Pending",
                                      total_price = 0)

  # Adds a new order in tblorderitems
  app_tables.tblorderitems.add_row(
                                   order_id = order, 
                                   cake_type = cake_type, occasion = occasion, 
                                   no_of_tiers = no_of_tiers, frosting_type = frosting_type, 
                                   frosting_flavour = frosting_flavour, 
                                   price = price, 
                                   serving_size = serving_size, 
                                   sponge_flavour = sponge_flavour, filling = filling, allergies = allergies, 
                                   additional_details = additional_details, 
                                   inscription = inscription, reference_image = reference_image)
 
  cakes = app_tables.tblorderitems.search(order_id = order)
  total_price = 0
  for cake in cakes:
    total_price = total_price + cake["price"]
  order["total_price"] = total_price

  # Sending an email to the customer
  customer = anvil.users.get_user()
  anvil.email.send(
    to = customer["email"], 
    from_address = "CakesBakesCardiff", 
    subject = "Order request", 
    text = "We have received your request."
  )

  # Sending an email to the manager notifying them of an order
  user = app_tables.users.get(role = "Manager")
  anvil.email.send(
    to = user["email"], 
    from_address = "CakesBakesCardiff", 
    subject = "Order request", 
    text = (f""" You have received a new order request from {customer["firstname"]}!
    """)
  )

@anvil.server.callable
# Takes all user inputs
def confirm_standard_order(cake_type, occasion, no_of_tiers, frosting_type, 
                           frosting_flavour, price,
                           serving_size, sponge_flavour, filling, collection_date):
  user = anvil.users.get_user()
  if not user:
    return
  order_id_number = generate_order_id()

  # Adds a new order in the database
  order = app_tables.tblorders.add_row(order_id = order_id_number,
                                       user = user, 
                                       date_of_order = datetime.datetime.now(),
                                       collection_date = collection_date,
                                       order_status = "Pending",
                                       total_price = 0)

  # Adds a new order to tblorderitems
  app_tables.tblorderitems.add_row(order_id = order, cake_type = cake_type, occasion = occasion, 
                                   no_of_tiers = no_of_tiers, frosting_type = frosting_type, 
                                   frosting_flavour = frosting_flavour, 
                                   price = price, serving_size = serving_size, 
                                   sponge_flavour = sponge_flavour, filling = filling,)

  cakes = app_tables.tblorderitems.search(order_id = order)
  total_price = 0
  for cake in cakes:
    total_price = total_price + cake["price"]
  order["total_price"] = total_price

  # Sending an email to the customer
  customer = anvil.users.get_user()
  anvil.email.send(
    to = customer["email"], 
    from_address = "CakesBakesCardiff", 
    subject = "Order request", 
    text = "We have received your request."
  )

  # Sending an email to the manager notifying them of an order
  user = app_tables.users.get(role = "Manager")
  if not user or not user["email"]:
    return
  anvil.email.send(
    to = user["email"], 
    from_address = "CakesBakesCardiff", 
    subject = "Order request", 
    text = (f""" You have received a new order request from {customer["firstname"]}!
    """)
  )
  
@anvil.server.callable
def retrieve_orders():
  user = anvil.users.get_user()
  # Returns empty list if user isn't logged in
  if user is None:
    return []
  # List of all the current order statuses
  current_orders = ["Pending", "Confirmed", "Rejected", "Cancelled"]
  # Searches for orders that have the order status in current_orders list
  all_orders = app_tables.tblorders.search(user = user, order_status = q.any_of(*current_orders))

  # If the order was cancelled or rejected at it is too old (more than 30 days old),
  # it is skipped and not classed as a recent ordr to display. 
  recent_orders = []
  today = datetime.date.today()
  for order in all_orders:
    order_date = order["date_of_order"].date()
    if order["order_status"] == "Rejected" or order["order_status"] == "Cancelled":
      days_since_order = (today - order_date).days
      if days_since_order > 30:
        continue

    recent_orders.append(order)
  return recent_orders

# Changes order status to cancelled in the database
@anvil.server.callable
def cancel_order(order, reason):
  order["order_status"] = "Cancelled"
  order["cancellation_reason"] = reason
  
  # Sending an email to the customer about their cancellation
  customer = anvil.users.get_user()
  anvil.email.send(
    to = customer["email"], 
    from_address = "CakesBakesCardiff", 
    subject = "Order request", 
    text = f""" Hello {customer["firstname"]},
    Your order has been cancelled successfully
    Reason: 
    {reason}
    """
  )

  # Sending an email to the manager to confirm thir cancellation
  manager = app_tables.users.get(role = "Manager")
  if manager:
    anvil.email.send(
      to = manager["email"],
      from_address = "CakesBakesCardiff",
      subject = "Order cancellation",
      text = f""" An order has been cancelled.
      {customer["firstname"]} {customer["surname"]} has cancelled because: 
      {reason}"""
    )
  pass


@anvil.server.callable
def display_cake(order):
  cakes = app_tables.tblorderitems.search(order_id = order)
  return cakes

# Takes the details the user entered and updates that to the database
@anvil.server.callable
def update_user_details(firstname, surname, email):
  user = anvil.users.get_user()
  if user is None:
    raise Exception("Not logged in")
  user["firstname"] = firstname
  user["surname"] = surname
  user["email"] = email
  user["active"] = True
  user.update()

# Deletes all account info for that user
@anvil.server.callable
def delete_account():
  user = anvil.users.get_user()
  if user is None:
    raise Exception("Not logged in")

  user.delete()
  anvil.users.logout()
