from ._anvil_designer import CalendarTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Calendar(CalendarTemplate):
  def __init__(self, role, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = role

    # Any code you write here will run before the form opens.

  def home_button_click(self, **event_args):
    open_form('StaffDashboard', self.role)
    pass
