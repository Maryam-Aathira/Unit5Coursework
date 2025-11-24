from ._anvil_designer import CustomerLoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CustomerLogin(CustomerLoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def sign_in_button_click(self, **event_args):
    app_tables.Users.add_row(email = self.email.text)
    pass
