from ._anvil_designer import StaffViewAccountTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffViewAccount(StaffViewAccountTemplate):
  def __init__(self, role, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = role
    self.role_label.text = "Role: " + str(role)

    user = anvil.users.get_user()
    if user:
      self.firstname_box.text = user["firstname"]
      self.surname_box.text = user["surname"]
      self.email_box.text = user["email"]

  
  def home_button_click(self, **event_args):
    open_form('StaffDashboard')
    pass

  def sign_out_button_click(self, **event_args):
    anvil.users.logout()
    open_form("Home")
    pass

  @handle("save_changes_button", "click")
  def save_changes_button_click(self, **event_args):
    firstname =  self.firstname_box.text
    surname = self.surname_box.text
    email = self.email_box.text
    if not firstname or not surname or not email:
      alert("Enter all details")
      return
    anvil.server.call("update_user_details", firstname, surname, email)
    pass

