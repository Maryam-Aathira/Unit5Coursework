from ._anvil_designer import ResetPasswordTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ResetPassword(ResetPasswordTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def back_button_click(self, **event_args):
    open_form('CustomerLogin')
    pass

  def next_button_click(self, **event_args):
    open_form('ResetPassword2')
    pass
