from ._anvil_designer import SignupTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Signup(SignupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    # Any code you write here will run before the form opens.

  def back_button_click(self, **event_args):
   open_form("CustomerLogin")
  pass

  def confirm_signup_button_click(self, **event_args):
    firstname = self.firstname_text_box.text
    surname = self.surname_text_box.text
    email = self.email_text_box.text
    anvil.server.call('create_account', firstname, surname, email)
    pass
