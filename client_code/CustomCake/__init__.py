from ._anvil_designer import CustomCakeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CustomCake(CustomCakeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Frosting Flavour dropdown 
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="frosting_flavour"):
      item_list.append((row["choice"], row))
    self.frosting_flavour_dropdown.items = item_list
    
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="cake_type"):
      item_list.append((row["choice"], row))
    self.cake_type_dropdown.items = item_list
    
    # Sponge flavour dropdown
    for row in app_tables.tbldropdownoptions.search(category="sponge_flavour"):
      item_list.append((row["choice"], row))
    self.sponge_flavour_dropdown.items = item_list

    # Frosting type dropdown 
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="frosting_type"):
      item_list.append((row["choice"], row))
    self.frosting_type_dropdown.items = item_list

    
    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    open_form('Home')
    pass

  
  def cake_type_dropdown_change(self, **event_args):
    pass
  
