from ._anvil_designer import CustomCakeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date 
import datetime 
from datetime import timedelta


class CustomCake(CustomCakeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.calculated_price = 0.00
    self.calculate_price()
    # self.reference_image.source

    # Makes the additional boxes unseen initially.  
    self.other_frosting.visible = False
    self.other_filling.visible = False
    self.other_occasion.visible = False
    self.enter_allergies.visible = False


#  while True:
 #   if self.cake_type_dropdown.selected_value == "Cupcakes":
  #    self.no_of_tiers_dropdown.visible = False
   #   self.no_of_tiers_label.visible = False
  #  else:
   #   self.no_of_tiers_dropdown.visible = True
    #  self.no_of_tiers_label.visible = True
      
      
    

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

  # Calling calulate price function for all dropdowns so the price gets updated
  def cake_type_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def filling_dropdown_change(self, **event_args):
    filling = self.filling_dropdown.selected_value
    if filling != "Other":
      self.other_filling.visible = False
      self.other_filling.text = ""
    else:
      self.other_filling.visible = True
    self.calculate_price()
    pass

  def sponge_flavour_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def frosting_type_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  def frosting_flavour_dropdown_change(self, **event_args):
    frosting_flavour = self.frosting_type_dropdown.selected_value
    if frosting_flavour != "Other":
      self.other_frosting.visible = False
      self.other_frosting.text = ""
    else:
      self.other_frosting.visible = True
    self.calculate_price()
    pass

  def occasion_dropdown_change(self, **event_args):
    occasion = self.occasion_dropdown.selected_value
    if occasion != "Other":
      self.other_occasion.visible = False
      self.other_occasion.text = ""
    else:
      self.other_occasion.visible = True
    pass

  @handle("enter_serving_size", "change")
  def enter_serving_size_pressed_enter(self, **event_args):
    self.calculate_price()
    pass
  
  def no_of_tiers_dropdown_change(self, **event_args):
    self.calculate_price()
    pass

  @handle("enter_inscription", "change")
  def enter_inscription_pressed_enter(self, **event_args):
    self.calculate_price()
    pass


  # Calculated the cost of each cake
  def calculate_price(self, **event_args):
    # Starting price of a plain one tier cake
    price = 25.00

    # Increases the price if the filling isn't a standard one
    filling = self.filling_dropdown.selected_value
    if filling == "Other":
      self.other_filling.visible = True
      price = price + 5.00

      
    # Gets the frosting flavour from the dropdown and sets this as a new variable to compare for price
    frosting_flavour = self.frosting_flavour_dropdown.selected_value
    if frosting_flavour == "Vanilla" or frosting_flavour == "Chocolate" or frosting_flavour == "Lemon":
      price = price + 5.00
    elif frosting_flavour == "Salted Caramel" or frosting_flavour == "Almond":
      price = price + 10.00
    elif frosting_flavour == "Other":
      self.other_frosting.visible = True
      price = price + 8.00


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

    inscription = self.enter_inscription.text.strip()
    if inscription != "":
      price = price + 2.00

    serving_size = self.enter_serving_size.text
    if serving_size.isdigit():
      serving_size = int(serving_size)
      if serving_size >= 8 and serving_size <= 12:
        price = price + 5
      elif serving_size >= 13 and serving_size <= 24:
        price = price + 10
      elif serving_size >= 25 and serving_size <= 30:
        price = price + 15
      elif serving_size >= 31 and serving_size <= 40:
        price = price + 25

    self.price_label.text = f"£{price:.2f}"
    self.calculated_price = price
    pass

  # Ensuring fields have been selected 
  def validating_dropdown(self, selected_value, message):
    if selected_value is None:
      alert(message)
      return False
    return True

  # Ensuring the other option have been selected
  def validate_other_option(self, selected_value, other_textbox, message):
    if selected_value == "Other" and other_textbox.text.strip() == "":
      alert(message)
      return False
    return True

  # Ensuring the text boxes have information entered
  def validate_text_entry(self, text, message):
    if text.strip() == "":
      alert(message)
      return False 
    return True

  def validate_checkbox(self, checkbox, text, message):
    if checkbox.checked and text.strip() == "":
      alert(message)
      return False  
    return True
    

  def add_to_order_button_click(self, **event_args):
    # Calling the function to check all fields have been entered
    # Checks cake type
    if not self.validating_dropdown(
      self.cake_type_dropdown.selected_value,
      "Please enter a cake type"
    ):
      return
    # Checks sponge flavour
    if not self.validating_dropdown(
      self.sponge_flavour_dropdown.selected_value,
      "Please enter a sponge flavour"
    ):
      return
    # Checks filling
    if not self.validating_dropdown(
      self.filling_dropdown.selected_value,
      "Please enter a filling"
    ):
      return
    # Checks the 'other' dropdown option for filling
    if not self.validate_other_option(
      self.filling_dropdown.selected_value,
      self.other_filling,
      "Please enter a filling"
    ):
      return
    # Checks the 'other' dropdown option for frosting flavour
    if not self.validate_other_option(
      self.frosting_flavour_dropdown.selected_value,
      self.other_frosting,
      "Please enter a frosting flavour"
    ):
      return
    # Checks the 'other' dropdown option for frosting flavour
    if not self.validate_other_option(
      self.occasion_dropdown.selected_value,
      self.other_occasion,
      "Please enter an occasion"
    ):
      return
    # Checks the serving size has been entered
    if not self.validate_text_entry(
      self.enter_serving_size.text,
      "Please enter a serving size"
    ):
      return
    # Checks the checkbox has been checked and necessary allergy details are entered
    if not self.validate_checkbox(
      self.other_checkbox,
      self.enter_allergies.text,
      "Please enter any other allergies"
    ):
      return

    # Checking that the date isn't marked as unavailable
    selected = self.collection_date_picker.date
    unavailable = anvil.server.call("marked_date_check", selected)
    if unavailable:
      alert("Unfortunately, we are unavailable for collection that day.")
      return


    # Calls the function to check the date
    if not self.valid_future_date(selected):
      return

    # Taking the values the user has entered and storing them in easy variable name
    # This is later stored in the database through the server module 
    cake_type = self.cake_type_dropdown.selected_value
    occasion = self.occasion_dropdown.selected_value
    if occasion == "Other":
      occasion = self.other_occasion.text
    sponge_flavour =  self.sponge_flavour_dropdown.selected_value
    no_of_tiers = int(self.no_of_tiers_dropdown.selected_value or 1)
    frosting_type = self.frosting_type_dropdown.selected_value
    frosting_flavour = self.frosting_flavour_dropdown.selected_value
    if frosting_flavour == "Other":
      frosting_flavour = self.other_frosting.text
    price = self.calculated_price
    serving_size = int(self.enter_serving_size.text or 1)
    filling = self.filling_dropdown.selected_value
    if filling == "Other":
      filling = self.other_filling.text
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
    alert("Your order has been requested!")
    pass


  # Checks the date is valid
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


  # Allows a reference image to be uploaded
  def upload_image_change(self, file, **event_args):
    self.reference_image.source = file
    pass

  def view_orders_click(self, **event_args):
    open_form("ViewOrders")
    pass

  def view_account_click(self, **event_args):
    open_form("ViewAccount")
    pass

  @handle("other_checkbox", "change")
  def other_checkbox_change(self, **event_args):
    self.enter_allergies.visible = True
    pass

  @handle("nuts_checkbox", "change")
  def nuts_checkbox_change(self, **event_args):
    alert("Traces of nuts may be found in cakes. If allergy is severe do not continue to place an order")
    pass

  @handle("collection_date_picker", "change")
  def collection_date_picker_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass


