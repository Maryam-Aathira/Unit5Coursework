from ._anvil_designer import BrowseTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# importing my own libraries
from datetime import date

class Browse(BrowseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_add_v_click(self, **event_args):
    anvil.server.call('add_standard_cake')
    pass


    



