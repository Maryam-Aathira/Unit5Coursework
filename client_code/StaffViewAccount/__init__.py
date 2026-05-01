from ._anvil_designer import StaffViewAccountTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffViewAccount(StaffViewAccountTemplate):
  def __init__(self, role, **properties):
    self.init_components(**properties)
    self.role = role
    self.role_label.text = "Role: " + str(role)

    user = anvil.users.get_user()
    if user:
      self.firstname_box.text = user["firstname"]
      self.surname_box.text = user["surname"]
      self.email_box.text = user["email"]


    # Validation
  def validate_names(self, text, message):
    # Checks it isn't empty
    if not text.strip():
      alert(f"Please enter a {message}")
      return False
    # Checks only letters are entered
    if not text.isalpha():
      alert(f"Please enter letters only for a {message}")
      return False
    return True

  def validate_email(self, email):
    if not email.strip():
      alert("Please enter an email")
      return False
    if "@" not in email or "." not in email:
      alert("Please enter a valid email")
      return False
    return True

  
  def home_button_click(self, **event_args):
    open_form("StaffDashboard")
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
    if not self.validate_names(firstname, "firstname"):
      return 
    if not self.validate_names(surname, "surname"):
      return
    if not self.validate_email(email):
      return

    anvil.server.call("update_user_details", firstname, surname, email)
    alert("Changes saved")
    pass
