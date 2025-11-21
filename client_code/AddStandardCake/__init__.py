from ._anvil_designer import AddStandardCakeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

NameArray = ["Vanilla Cake","Chocolate Cake", "Salted Caramel Cake", "Lemon Cake", "Orange Cake", "Almond Cake", "Chocolate Orange Cake"]
FlavourArray = ["Vanilla Sponge - Vanilla Buttercream Frosting", 
                "Chocolate Sponge - Chocolate Ganache", "Vanilla Sponge - Salted Caramel Frosting"
                , "Vanilla Sponge - Lemon Frosting", "Plain Sponge - Orange Frosting"
                ,"Plain Sponge - Almond Frosting", "Chocolate Sponge - Chocolate Orange Frosting"]
PriceArray = ["£30","£30","£35","£30","£35","£25","£25"]


class AddStandardCake(AddStandardCakeTemplate):
  def __init__(self, CakeNo, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.CakeTitle.text = NameArray[CakeNo]
    self.cake_flavour.text = FlavourArray[CakeNo]
    self.price.text = PriceArray[CakeNo]
    # Any code you write here will run before the form opens.
