from ._anvil_designer import ViewAccountTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ViewAccount(ViewAccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   # user = anvil.users.get_user()
    #if user:
     # self.firstname_box.text = user["firstname"]
     # self.surname_box.text = user["surname"]
    #  self.email_box = user["email"]

  def view_order_button_click(self, **event_args):
    open_form("ViewOrders")
    pass

  def home_button_click(self, **event_args):
    open_form("Home")
    pass

  def sign_out_button_click(self, **event_args):
    anvil.users.logout()
    open_form("Home")
    pass
