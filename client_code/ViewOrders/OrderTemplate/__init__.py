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

    selected_date = self.collection_date_picker.date
    current_date = datetime.date.today()
    days_until_collection = (selected_date - current_date).days
    #order = self.item
   # cakes = app_tables.tblorderitems.search(order=order)
    
    #self.cake_name_label = "Cake: " + str(self.item["cake_type"]) + str(self.item["sponge_flavour"])
    self.date_label.text = "Date of Order: " + str(self.item["date_of_order"])
    self.status_label.text = "Order Status: " + str(self.item["order_status"])
    # Need to get price from tblOrderItems
    self.price_label.text = "£" + str(self.item["total_price"])
    self.break_label.text = "-----------------------------------------------------------------------------------"
    self.remove_order_button.visible = False

    # Any code you write here will run before the form opens.

  def cancel_order_button_click(self, **event_args):
    if days_until_collection <= 7:
      print("can't cancel")
      alert("Can't cancel")
    else:
      anvil.server.call('cancel_order', self.item)
      self.status_label.text = "Order Status: " + str(self.item["order_status"])
      self.remove_order_button.visible = True
    pass

  def remove_order_button_click(self, **event_args):
    self.date_label.text = ""
    self.status_label.text = ""
# Need to get price from tblOrderItems
    self.price_label.text = ""
    self.break_label.text = ""
    self.remove_order_button.visible = False
    self.cancel_order_button.visible = False
  pass
