from ._anvil_designer import StaffLoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffLogin(StaffLoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   
   # self.manager_radio_button_selection()

  #def manager_radio_button_clicked(self, **event_args):
 

  def sign_in_button_click(self, **event_args):
    if self.manager_radio_button.selected == True:
      open_form("ManagerDashboard")
    else:
      open_form("EmployeeDashboard")
    pass
