from ._anvil_designer import BrowseTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# importing my own libraries
from datetime import date

class Browse(BrowseTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  # Calls the number from the arrays 
  def button_add_v_click(self, **event_args):
    open_form("AddStandardCake", 0)
    pass

  def button_add_c_click(self, **event_args):
    open_form("AddStandardCake", 1)
    pass

  def button_add_s_c_click(self, **event_args):
    open_form("AddStandardCake", 2)
    pass

  def button_add_l_click(self, **event_args):
    open_form("AddStandardCake", 3)
    pass

  def button_add_o_click(self, **event_args):
    open_form("AddStandardCake", 4)
    pass

  def button_add_a_click(self, **event_args):
    open_form("AddStandardCake", 5)
    pass

  def button_add_c_o_click(self, **event_args):
    open_form("AddStandardCake", 6)
    pass

  def button_home_click(self, **event_args):
    open_form("Home")

  def button_view_orders_click(self, **event_args):
    open_form("ViewOrders")
    pass

  @handle("button_view_account", "click")
  def button_view_account_click(self, **event_args):
    open_form("ViewAccount")
    pass


    