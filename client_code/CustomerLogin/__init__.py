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

    #email = self.email_textbox.text  
    
    

  def create_account_button_click(self, **event_args):
    open_form('Signup')
    #app_tables.users.add_row(email = self.email.text)
    pass

  def back_button_click(self, **event_args):
    open_form("Home")
    pass

  def reset_password_button_click(self, **event_args):
    open_form('ResetPassword')
    pass
