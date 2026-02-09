import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import datetime
import random

#def after_user_login(user):


@anvil.server.callable
def generate_order_id():
  while True:
   order_id = random.randint(100000, 999999)
   existing = app_tables.tblorders.get(order_id = order_id)
   if existing is None:
    return order_id

# Adding Standard cakes to the customer's order
@anvil.server.callable
def add_standard_cake(cake_type, occasion, no_of_tiers, frosting_type, frosting_flavour, price, 
                      serving_size, sponge_flavour, filling):
  anvil.users.get_user()
  app_tables.tblorderitems.add_row(cake_type = cake_type, occasion = occasion, 
                                   no_of_tiers = no_of_tiers, frosting_type = frosting_type, 
                                   frosting_flavour = frosting_flavour, price = price, 
                                   serving_size = serving_size, 
                                   sponge_flavour = sponge_flavour, filling = filling)

@anvil.server.callable
def add_custom_cake(cake_type, occasion, no_of_tiers, frosting_type, frosting_flavour, price, 
                    serving_size, sponge_flavour, filling, allergies, additional_details, inscription, 
                    reference_image, collection_date):
  user = anvil.users.get_user()
  order_id_number = generate_order_id()
  order = app_tables.tblorders.add_row(order_id = order_id_number, 
                                      user = user, 
                                      date_of_order = datetime.datetime.now(),
                                      collection_date = collection_date,
                                      order_status = "Pending",
                                      total_price = 0)
  
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
def confirm_standard_order(cake_type, occasion, no_of_tiers, frosting_type, 
                           frosting_flavour, price,
                           serving_size, sponge_flavour, filling, collection_date):
  user = anvil.users.get_user()
  order_id_number = generate_order_id()
  
  order = app_tables.tblorders.add_row(order_id = order_id_number,
                                       user = user, 
                                       date_of_order = datetime.datetime.now(),
                                       collection_date = collection_date,
                                       order_status = "Pending",
                                       total_price = 0)
  
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
  current_orders = ["Pending", "Confirmed", "Rejected"]
  all_orders = app_tables.tblorders.search(order_status = q.any_of(*current_orders))

  recent_order = []
  now = datetime.datetime.now(datetime.timezone.utc)
  for order in all_orders:
    order_date = order["date_of_order"]
    if order["order_status"] == "Rejected":
      difference = (now - order_date).days
      if difference > 30:
        continue

    recent_order.append(order)
  return recent_order
      

  


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

@anvil.server.callable
def create_account(firstname, surname, email, password):
  if app_tables.users.get(email = email):
    return False
  app_tables.users.add_row(firstname = firstname, surname = surname, email = email, 
                          password_hash = anvil.users.hash_password(password))

@anvil.server.callable
def sign_in(email, password):
  #anvil.users.login_with_email_and_password(email, password)
  #user = app_tables.users.search(email=email)
  #print("Works")
  pass

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

@anvil.server.callable
def delete_account():
  user = anvil.users.get_user()
  if user is None:
    raise Exception("Not logged in")

  user.delete()
  anvil.users.logout()


#@anvil.server.callable
#def check_orders():
  #cutoff = datetime