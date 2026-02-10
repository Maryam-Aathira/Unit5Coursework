from ._anvil_designer import OrderHistoryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class OrderHistory(OrderHistoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def get_orders(self):
    all_customer_orders = anvil.server.call("get_all_customer_orders")
    self.order_panel.items = all_customer_orders

  
  @handle("home_button", "click")
  def home_button_click(self, **event_args):
    open_form("Home")
    pass

  @handle("view_account_button", "click")
  def view_account_button_click(self, **event_args):
    open_form("ViewAccount")
    pass
