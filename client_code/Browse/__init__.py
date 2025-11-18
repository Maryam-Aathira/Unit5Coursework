from ._anvil_designer import BrowseTemplate
from anvil import *
import anvil.users
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
    anvil.server.call('add_the_vanilla_cake')
    pass

  def button_add_c_click(self, **event_args):
    anvil.server.call('add_the_chocolate_cake')
    pass

  def button_add_s_c_click(self, **event_args):
    anvil.server.call('add_the_salted_caramel_cake')
    anvil.server.call('add_cake', '')
    pass

  def button_add_l_click(self, **event_args):
    anvil.server.call('add_the_lemon_cake')
    pass

  def button_add_o_click(self, **event_args):
    anvil.server.call('add_the_orange_cake')
    pass

  def button_add_a_click(self, **event_args):
    anvil.server.call('add_the_almond_cake')
    pass

  def button_add_c_o_click(self, **event_args):
    anvil.server.call('add_the_chocolate_orange_cake')
    pass


    



