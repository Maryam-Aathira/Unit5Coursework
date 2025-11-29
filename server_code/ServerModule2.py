import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import datetime

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
  order = app_tables.tblorders.add_row(user = user, 
                                      date_of_order = datetime.datetime.now(),
                                      collection_date = collection_date,
                                      order_status = "Pending",
                                      total_price = 0)
  
  app_tables.tblorderitems.add_row(#user = user,
                                   order = order, 
                                   cake_type = cake_type, occasion = occasion, 
                                   no_of_tiers = no_of_tiers, frosting_type = frosting_type, 
                                   frosting_flavour = frosting_flavour, 
                                   price = price, 
                                   serving_size = serving_size, 
                                   sponge_flavour = sponge_flavour, filling = filling, allergies = allergies, 
                                   additional_details = additional_details, 
                                   inscription = inscription, reference_image = reference_image)
 
  cakes = app_tables.tblorderitems.search(order = order)
  total_price = 0
  for cake in cakes:
    total_price = total_price + cake["price"]
  order["total_price"] = total_price

#@anvil.server.callable
#def confirm_standard_order(cake_type, occasion, no_of_tiers, frosting_type,
 #                          frosting_flavour, price, serving_size,
  #                         sponge_flavour, filling, collection_date):

  #user = anvil.users.get_user()
  #order = app_tables.tblorders.add_row(user = user, 
   #                                    date_of_order = datetime.datetime.now(),
    #                                   collection_date = collection_date,
     #                                  order_status = "Pending",
      #                                 total_price = 0)

#  app_tables.tblorderitems.add_row(
 #   order = order,
  #  user=user,
#    cake_type=cake_type,
 #   occasion=occasion,
  #  no_of_tiers=no_of_tiers,
   # frosting_type=frosting_type,
    #frosting_flavour=frosting_flavour,
#    price=price,
 #   serving_size=serving_size,
  #  sponge_flavour=sponge_flavour,
   # filling=filling,
    #collection_date=collection_date,
    #order_status="Pending"
 # )

  
@anvil.server.callable
def confirm_standard_order(cake_type, occasion, no_of_tiers, frosting_type, 
                           frosting_flavour, price,
                           serving_size, sponge_flavour, filling, collection_date):
  user = anvil.users.get_user()
  
  order = app_tables.tblorders.add_row(user = user, 
                                       date_of_order = datetime.datetime.now(),
                                       collection_date = collection_date,
                                       order_status = "Pending",
                                       total_price = 0)
  
  app_tables.tblorderitems.add_row(order = order, cake_type = cake_type, occasion = occasion, 
                                   no_of_tiers = no_of_tiers, frosting_type = frosting_type, 
                                   frosting_flavour = frosting_flavour, 
                                   price = price, serving_size = serving_size, 
                                   sponge_flavour = sponge_flavour, filling = filling,)

  cakes = app_tables.tblorderitems.search(order = order)
  total_price = 0
  for cake in cakes:
    total_price = total_price + cake["price"]
  order["total_price"] = total_price
  
@anvil.server.callable
def retrieve_orders():
  user = anvil.users.get_user()
  return app_tables.tblorders.search(user = user)

@anvil.server.callable
def cancel_order(order):
  order["order_status"] = "Cancelled"
  pass