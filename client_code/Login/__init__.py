from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def employee_login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def customer_login_button_click(self, **event_args):
    open_form('CustomerLogin')
    pass

  def manager_login_button_click(self, **event_args):
    open_form('ManagerDashboard')
    pass
