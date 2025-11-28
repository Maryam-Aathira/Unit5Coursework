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
    self.calculated_price = 0.00
    self.calculate_price()
    # self.reference_image.source

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

  def home_click(self, **event_args):
    open_form('Home')
    pass

  # Calling calulate price functionn for all dropdowns so the price gets updated
  def cake_type_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def filling_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def sponge_flavour_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def frosting_type_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def frosting_flavour_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def enter_serving_size_pressed_enter(self, **event_args):
    self.calculate_price()
    pass

  def no_of_tiers_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def enter_inscription_pressed_enter(self, **event_args):
    self.calculate_price()
    pass






  # Calculated the cost of each cake
  def calculate_price(self, **event_args):
    price = 20.00

    # Gets the frosting flavour from the dropdown and sets this as a new variable to compare for price
    frosting_flavour = self.frosting_flavour_dropdown.selected_value
    if frosting_flavour == "Vanilla" or frosting_flavour == "Chocolate" or frosting_flavour == "Lemon":
      price = price + 5.00
    elif frosting_flavour == "Salted Caramel" or frosting_flavour == "Almond":
      price = price + 10.00

    frosting_type = self.frosting_type_dropdown.selected_value
    if frosting_type == "Buttercream":
      price = price + 3.00
    elif frosting_type == "Fondant":
      price = price + 7.00

    tiers = int(self.no_of_tiers_dropdown.selected_value or 1)
    #int(tiers)
    if tiers == 1:
      price = price + 0.00
    if tiers == 2:
      price = price + 35.00
    if tiers == 3:
      price = price + 50.00
    if tiers == 4:
      price = price + 75.00
    if tiers == 5:
      price = price + 120.00

    inscription = self.enter_inscription.text
    if inscription != "" or inscription != " ":
      price = price + 2.00

    self.price_label.text = "£" + str(price)
    self.calculated_price = price
    pass

  def add_to_order_button_click(self, **event_args):
    cake_type = self.cake_type_dropdown.selected_value
    occasion = self.occasion_dropdown.selected_value
    sponge_flavour =  self.sponge_flavour_dropdown.selected_value
    no_of_tiers = int(self.no_of_tiers_dropdown.selected_value or 1)
    frosting_type = self.frosting_type_dropdown.selected_value
    frosting_flavour = self.frosting_flavour_dropdown.selected_value
    price = self.calculated_price
    serving_size = int(self.enter_serving_size.text or 1)
    filling = self.filling_dropdown.selected_value
    allergies = self.enter_allergies.text
    inscription = self.enter_inscription.text
    additional_details = self.enter_additional_info.text
    reference_image = self.reference_image.source or None
    collection_date = self.collection_date_picker.date
    anvil.server.call("add_custom_cake", cake_type, occasion, no_of_tiers, 
                      frosting_type, frosting_flavour, 
                      price, serving_size, 
                      sponge_flavour, filling, allergies, additional_details, 
                      inscription, reference_image, collection_date)
    pass

  def upload_image_change(self, file, **event_args):
    self.reference_image.source = file
    pass

  def view_orders_click(self, **event_args):
    open_form("ViewOrders")
    pass

  def view_account_click(self, **event_args):
    open_form("ViewAccount")
    pass






  

  
