from ._anvil_designer import StaffLoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffLogin(StaffLoginTemplate):
  def __init__(self, role = "None", **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
   #self.manager_radio_button_selection()

  #def manager_radio_button_clicked(self, **event_args):
 

  def sign_in_button_click(self, **event_args):
    if self.manager_radio_button.selected:
      role = "Manager"
    if self.employee_radio_button.selected:
      role = "Employee"
    open_form("StaffDashboard", role = role)
    pass

  def back_button_click(self, **event_args):
    open_form('Home')
    pass

  def employee_radio_button_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def manager_radio_button_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass
