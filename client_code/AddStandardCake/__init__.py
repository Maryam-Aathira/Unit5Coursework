from ._anvil_designer import AddStandardCakeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

NameArray = ["Vanilla Cake","Chocolate Cake", "Salted Caramel Cake", "Lemon Cake", 
             "Orange Cake", "Almond Cake", "Chocolate Orange Cake"]

FlavourArray = ["Vanilla Sponge" , "Chocolate Sponge", "Vanilla Sponge", 
              "Vanilla Sponge", "Plain Sponge", "Plain Sponge", "Chocolate Sponge"]

PriceArray = ["£25","£25","£30","£25","£30","£20","£20"]

FrostingArray = ["Vanilla", "Chocolate Ganache", "Salted Caramel", "Lemon", 
                "Orange Flavoured", "Almond Flavoured", "Chocolate orange"]


class AddStandardCake(AddStandardCakeTemplate):
  def __init__(self, CakeNo, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.CakeTitle.text = NameArray[CakeNo]
    self.sponge_flavour.text = FlavourArray[CakeNo]
    self.frosting_flavour.text = FrostingArray[CakeNo]
    self.price.text = PriceArray[CakeNo]
    # Any code you write here will run before the form opens.

  def confirm_order_button_click(self, **event_args,):
    cake_type = "Sponge cake"
    occasion = "None"
    sponge_flavour = self.sponge_flavour.text
    no_of_tiers = 1
    frosting_type = "Buttercream"
    frosting_flavour = self.frosting_flavour.text
    price = float(self.price.text[1:])
    serving_size = 10
    filling = "None"
    anvil.server.call('confirm_standard_order', cake_type, occasion, no_of_tiers, 
                      frosting_type, frosting_flavour, price, 
                      serving_size, sponge_flavour, filling)

  pass

  def view_orders_button_click(self, **event_args):
    
    pass

  def home_click(self, **event_args):
    open_form('Home')
    pass
