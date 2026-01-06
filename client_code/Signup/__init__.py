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


  def back_button_click(self, **event_args):
   open_form("Home")
  pass

  def confirm_signup_button_click(self, **event_args):
    firstname = self.firstname_text_box.text
    surname = self.surname_text_box.text
    email = self.email_text_box.text
    password = self.password_text_box.text
    retype_password = self.retype_text_box.text

    if retype_password != password:
      alert("Passwords do not match")
      return False

    try:
      anvil.users.signup_with_email(email, password)
      anvil.users.login_with_email(email, password)
     # user = anvil.users.get_user()
      anvil.server.call("update_user_details", firstname, surname)
      open_form('Home')
      #user["firstname"] = firstname
     # user["surname"] = surname

    except anvil.users.AuthenticationFailed:
      alert("Login failed")
    except anvil.users.UserExists:
      alert("Already an account with this email")
      

    
  
  
