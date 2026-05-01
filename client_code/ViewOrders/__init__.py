from ._anvil_designer import ViewOrdersTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ViewOrders(ViewOrdersTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
  
    self.sign_in_info.visible = False
    user = anvil.users.get_user()
    
    if user is None:
      self.sign_in_info.visible = True
      return
    
    self.get_orders()


  def get_orders(self):
    all_customer_orders = anvil.server.call("retrieve_orders")
    self.order_panel.items = all_customer_orders
   
  def view_account_click(self, **event_args):
    open_form("ViewAccount")
    pass

  def home_click(self, **event_args):
    open_form("Home")
    pass 

  @handle("order_history_button", "click")
  def order_history_button_click(self, **event_args):
    open_form("OrderHistory")
    pass
