from ._anvil_designer import AddStandardCakeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date
from datetime import timedelta

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

  @handle("collection_date_picker", "change")
  def collection_date_picker_change(self, **event_args):
    pass


  def confirm_order_button_click(self, **event_args,):
    # Checking for availablity
    selected = self.collection_date_picker.date
    unavailable = anvil.server.call("marked_date_check", selected)
    if unavailable:
      alert("Unfortunately, we are unavailable for collection that day.")
      return
      
    if not self.valid_future_date(selected):
      return
   
    
    user = anvil.users.get_user()
    if user is None:
      alert("Sign in to continue")
      return
    # Checks the user has entered a collection date
    if not selected:
      alert("Please enter a collection date")
      return
    # Checks the user has fully entered their account information
    if not user["firstname"] or not user["surname"]:
      alert("Please complete your account information before placing an continuing")
      open_form("ViewAccount")
      return
    self.collection_date_picker.text = selected.strftime("%d/%m/%Y")
    cake_type = "Sponge cake"
    occasion = "None"
    sponge_flavour = self.sponge_flavour.text
    no_of_tiers = 1
    frosting_type = "Buttercream"
    frosting_flavour = self.frosting_flavour.text
    price = float(self.price.text[1:])
    serving_size = 10
    filling = "None"
    collection_date = self.collection_date_picker.date
    anvil.server.call('confirm_standard_order', cake_type, occasion, no_of_tiers, 
                      frosting_type, frosting_flavour, price, 
                      serving_size, sponge_flavour, filling, collection_date)
    alert("Your order has been requested!")
  pass

  def valid_future_date(self, selected):
    min_date = date.today() + timedelta(days = 3)
    if selected is None:
      alert("Please select a collection date")
      return False
    # Prevents users from selecting a previous date
    if selected <= date.today():
      alert("Please pick a date in the future")
      return False
    # Prevents users from expecting cakes to be ready too quickly
    if selected <= min_date:
      alert("Please pick a collection date that is at least three days in advance")
      return False
    return True
    
  def view_orders_button_click(self, **event_args):
    open_form("ViewOrders")
    pass

  def home_click(self, **event_args):
    open_form('Home')
    pass

