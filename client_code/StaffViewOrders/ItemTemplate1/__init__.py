from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    role = get_open_form().role
    self.confirm_button.background = "#238823"
    self.confirm_button.foreground = "#ffffff"

    self.reject_button.background = "#d2222d"
    self.reject_button.foreground = "#ffffff"


    if role == "Manager":
      self.confirm_button.visible = True
      self.reject_button.visible = True
    else:
      self.confirm_button.visible = False
      self.reject_button.visible = False



  @handle("confirm_button", "click")
  def confirm_button_click(self, **event_args):
    final_order = self.item["order_row"]
    anvil.server.call('confirm_order_status', final_order)
    alert("Order confirmed")
    self.order_status.text = "Confirmed"
    self.order_status.role = None

  @handle("reject_button", "click")
  def reject_button_click(self, **event_args):
    final_order = self.item["order_row"]
    anvil.server.call('reject_order_status', final_order)
    alert("Order rejected")
    self.order_status.text = "Rejected"
    self.order_status.role = None
    pass






    #self.order_repeating_panel = self.all_orders


    # Any code you write here will run before the form opens.

