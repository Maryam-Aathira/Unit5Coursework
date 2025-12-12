import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import datetime
import random

@anvil.server.callable
def generate_order_id():
  while True:
   order_id = random.randint(100000, 999999)
   existing = app_tables.tblorders.get(order_id = order_id)
   if existing is None:
    return order_id

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

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
  
@anvil.server.callable
def retrieve_orders():
  user = anvil.users.get_user()
  return app_tables.tblorders.search(user = user)

@anvil.server.callable
def cancel_order(order, reason):
  order["order_status"] = "Cancelled"
  order["cancellation_reason"] = reason
  
  #Sending an email to the customer about their cancellation
#  anvil.email.send(
#    to = "ethanjlewis2008@gmail.com",
#    from_address = "noreply",
#    from_name = "M3 App 1",
#    subject = "Your cancellation", 
#    html = "<h1> Cancel <h1>"
#  )
  pass

@anvil.server.callable
def display_cake(order):
  cakes = app_tables.tblorderitems.search(order_id = order)
  return cakes

@anvil.server.callable
def create_account(firstname, surname, email, password):
  app_tables.users.add_row(firstname = firstname, surname = surname, email = email)

@anvil.server.callable
def sign_in(email):
  user = app_tables.users.search(email=email)
  print("Works")
  return user