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


  def home_button_click(self, **event_args):
    open_form('StaffDashboard')
    pass

  @handle("confirm_date", "click")
  def confirm_date_click(self, **event_args):
    selected_date = self.unavailability_picker.date
    if selected_date is None:
      alert("Please select a date")
      return

    unavailable = anvil.server.call("marked_date_check", selected_date)
    if unavailable:
      alert("This date has already been marked as unavailable")
      return

    anvil.server.call("add_unavailable_date", selected_date)
    selected_date = selected_date.strftime("%d/%m/%Y")
    alert(f"{selected_date} has been marked as unavailable")

    # Checks to see is this date has already been marked as unavailable
    
    pass
