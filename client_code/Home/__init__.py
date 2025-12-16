from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user = anvil.users.get_user()
    if user is not None:
      self.login_button.visible = False

    # Any code you write here will run before the form opens.

  def view_orders_click(self, **event_args):
    open_form('ViewOrders')
    pass

  def browse_button_click(self, **event_args):
    open_form("Browse")
    pass

  def create_button_click(self, **event_args):
    open_form("CustomCake")
    pass

  def view_account_click(self, **event_args):
    open_form('ViewAccount')
    pass

  def login_button_click(self, **event_args):
    open_form('Login')
    pass
