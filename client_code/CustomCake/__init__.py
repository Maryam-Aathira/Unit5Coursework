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

    # Sponge flavour dropdown
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="sponge_flavour"):
      item_list.append(row["choice"])
    self.sponge_flavour_dropdown.items = item_list
  
    # Frosting Flavour dropdown 
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="frosting_flavour"):
      item_list.append(row["choice"])
    self.frosting_flavour_dropdown.items = item_list
    
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="cake_type"):
      item_list.append(row["choice"])
    self.cake_type_dropdown.items = item_list

    # Frosting type dropdown 
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="frosting_type"):
      item_list.append(row["choice"])
    self.frosting_type_dropdown.items = item_list

    # Occassion dropdown
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="occasion"):
      item_list.append(row["choice"])
    self.occasion_dropdown.items = item_list

    # Number of tiers dropdown
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="no_of_tiers"):
      item_list.append(row["choice"])
    self.no_of_tiers_dropdown.items = item_list

    # Filling dropdown
    item_list = []
    for row in app_tables.tbldropdownoptions.search(category="filling"):
      item_list.append(row["choice"])
    self.filling_dropdown.items = item_list
    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    open_form('Home')
    pass
  
  def cake_type_dropdown_change(self, **event_args):
    pass

  def add_to_order_button_click(self, **event_args):
    cake_type = self.cake_type_dropdown.selected_value
    occasion = self.occasion_dropdown.selected_value
    sponge_flavour =  self.sponge_flavour_dropdown.selected_value
    no_of_tiers = int(self.no_of_tiers_dropdown.selected_value)
    frosting_type = self.frosting_type_dropdown.selected_value
    frosting_flavour = self.frosting_flavour_dropdown.selected_value
   # price = float(self.price.text[1:])
    serving_size = int(self.enter_serving_size.text)
    filling = self.filling_dropdown.selected_value
    allergies = self.enter_allergies.text
    inscription = self.enter_inscription.text
    additional_details = self.enter_additional_info.text
    anvil.server.call("add_custom_cake", cake_type, occasion, no_of_tiers, 
                      frosting_type, frosting_flavour, 
                      #price, 
                      serving_size, 
                      sponge_flavour, filling, allergies, additional_details, 
                      inscription)
    pass
  
