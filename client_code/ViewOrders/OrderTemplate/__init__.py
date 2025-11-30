from ._anvil_designer import OrderTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime 


class OrderTemplate(OrderTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    selected_date = self.item["collection_date"]
    current_date = datetime.date.today()
    self.days_until_collection = (selected_date - current_date).days
    order = self.item
    cakes = anvil.server.call('display_cake',order)

    cake_info = ""
    # Adding information from tblOrderItems into a list for each cake
    for cake in cakes:
      cake_info = f"{cake['sponge_flavour']} {cake['cake_type']}\n{cake['filling']} filling\n{cake['frosting_flavour']} {cake['frosting_type']}"
    self.cake_name_label.text = cake_info
    self.date_label.text = "Date of Order: " + str(self.item["date_of_order"])
    self.status_label.text = "Order Status: " + str(self.item["order_status"])
    self.collection_date_label.text = "Collection Date: " + str(self.item["collection_date"])

    # Need to get price from tblOrderItems
    self.price_label.text = "£" + str(self.item["total_price"])
    self.break_label.text = "-----------------------------------------------------------------------------------"
    self.remove_order_button.visible = False

    # Any code you write here will run before the form opens.

  def cancel_order_button_click(self, **event_args):
    if self.days_until_collection <= 7:
      #print("can't cancel")
      alert("An order cannot be cancelled within 7 days of the collection date")
    else:
      anvil.server.call('cancel_order', self.item)
      self.status_label.text = "Order Status: " + str(self.item["order_status"])
      self.remove_order_button.visible = True
      self.cancel_order_button.visible = False
    pass

  def remove_order_button_click(self, **event_args):
    self.date_label.text = ""
    self.status_label.text = ""
    
# Need to get price from tblOrderItems
    self.price_label.text = ""
    self.break_label.text = ""
    self.cake_name_label.text = ""
    self.date_label.text = ""
    self.collection_date_label.text = ""
    self.remove_order_button.visible = False
    self.cancel_order_button.visible = False
  pass
