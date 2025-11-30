from ._anvil_designer import StaffDashboardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffDashboard(StaffDashboardTemplate):
  def __init__(self, role, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.calendar_button.visible = False
    self.statistics_button.visible = False
    if role == "Manager":
      self.calendar_button.visible = True
      self.statistics_button.visible = True
      self.dashboard_title.text = "Manager Dashboard"
    if role == "Employee":
      self.dashboard_title.text = "Employee Dashboard"

    # Any code you write here will run before the form opens.

  def view_orders_button_click(self, **event_args):
    open_form("StaffViewOrders")
    pass
