from ._anvil_designer import StaffDashboardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffDashboard(StaffDashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Gets the user's role from the database
    user = anvil.users.get_user()
    if user is None:
      # If the user isn't found users are redirected to login. 
      open_form("StaffLogin")
      return 
      
    try:
      role = user["role"]
      self.role = role
    # If the role is not in the database it will catch the error and redirect to login
    except KeyError:
      alert("Error, invalid role")
      open_form("StaffLogin")
      return

    
    self.calendar_button.visible = False
    self.statistics_button.visible = False
    if role == "Manager":
      self.calendar_button.visible = True
      self.statistics_button.visible = True
      self.dashboard_title.text = "Manager Dashboard"
    if role == "Employee":
      self.dashboard_title.text = "Employee Dashboard"

  def view_orders_button_click(self, **event_args):
    open_form("StaffViewOrders", role = self.role)
    pass

  def view_account_button_click(self, **event_args):
    open_form("StaffViewAccount", role = self.role)
    pass

  def statistics_button_click(self, **event_args):
    open_form("Statistics", role = self.role)
    pass

  def calendar_button_click(self, **event_args):
    open_form("Calendar", role = self.role)
    pass
