import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users

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
@anil.server.callable
def add_cake(cake_type, occasion, no_of_tiers, frosting_type, frosting_flavour, price, serving_size, sponge_flavour, filling)
  anvil.users.get_user()
  app_tables.tblorderitems.add_row('', '', '', '', cake_type, occasion, no_of_tiers, frosting_type, frosting_flavour, price, serving_size, sponge_flavour, filling)

@anvil.server.callable
def add_the_vanilla_cake():
  anvil.users.get_user()
  app_tables.tblorderitems.add_row(cake_type="Sponge Cake",
                                         occasion="",
                                         no_of_tiers= 1,
                                         frosting_type = "Buttercream",
                                         frosting_flavour="Vanilla",
                                         price=30.00,
                                         serving_size = 8,
                                         sponge_flavour = "Vanilla",
                                         filling="Vanilla cream"
                                    
                                        )
@anvil.server.callable
def add_the_chocolate_cake():
  app_tables.tblorderitems.add_row(cake_type="Sponge Cake",
                                   occasion="",
                                   no_of_tiers= 1,
                                   frosting_type = "Buttercream",
                                   frosting_flavour="Chocolate Ganache",
                                   price=30.00,
                                   serving_size = 8,
                                   sponge_flavour = "Chocolate",
                                   filling="Chocolate cream"

                                  )

@anvil.server.callable
def add_the_salted_caramel_cake():
  app_tables.tblorderitems.add_row(cake_type="Sponge Cake",
                                   occasion="",
                                   no_of_tiers= 1,
                                   frosting_type = "Buttercream",
                                   frosting_flavour="Salted Caramel",
                                   price=35.00,
                                   serving_size = 8,
                                   sponge_flavour = "Vanilla",
                                   filling="salted caramel cream"

                                  )

@anvil.server.callable
def add_the_lemon_cake():
  app_tables.tblorderitems.add_row(cake_type="Sponge Cake",
                                   occasion="",
                                   no_of_tiers= 1,
                                   frosting_type = "Buttercream",
                                   frosting_flavour="Lemon",
                                   price=30.00,
                                   serving_size = 8,
                                   sponge_flavour = "Vanilla",
                                   filling="lemon meringue cream"

                                  )

@anvil.server.callable
def add_the_orange_cake():
  app_tables.tblorderitems.add_row(cake_type="Sponge Cake",
                                   occasion="",
                                   no_of_tiers= 1,
                                   frosting_type = "Buttercream",
                                   frosting_flavour="Orange",
                                   price=35.00,
                                   serving_size = 8,
                                   sponge_flavour = "Plain",
                                   filling= "Orange Cream"

                                  )

@anvil.server.callable
def add_the_almond_cake():
  app_tables.tblorderitems.add_row(cake_type="Sponge Cake",
                                   occasion="",
                                   no_of_tiers= 1,
                                   frosting_type = "Buttercream",
                                   frosting_flavour="Almond",
                                   price=25.00,
                                   serving_size = 8,
                                   sponge_flavour = "Plain",
                                   filling= "Almond cream"

                                  )

@anvil.server.callable
def add_the_chocolate_orange_cake():
  app_tables.tblorderitems.add_row(cake_type="Sponge Cake",
                                   occasion="",
                                   no_of_tiers= 1,
                                   frosting_type = "Buttercream",
                                   frosting_flavour="Chocolate Orange",
                                   price=25.00,
                                   serving_size = 8,
                                   sponge_flavour = "Chocolate",
                                   filling= "Orange cream"

                                  )
