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
    anvil.server.call('add_standard_cake', 'Sponge Cake', '', 1, 'Buttercream', 'Vanilla', 30.00, 8, 'Vanilla', 'Vanilla cream')
    pass

  def button_add_c_click(self, **event_args):
    anvil.server.call('add_standard_cake', 'Sponge Cake', '', 1, 'Buttercream', 'Chocolate Ganache', 30.00, 8, 'Chocolate', 'Chocolate cream')
    pass

  def button_add_s_c_click(self, **event_args):
    #anvil.server.call('add_the_salted_caramel_cake')
    anvil.server.call('add_standard_cake', 'Sponge Cake', '', 1, 'Buttercream', 'Salted Caramel', 35.00, 8, 'Vanilla', 'Salted Caramel cream')
    pass

  def button_add_l_click(self, **event_args):
    anvil.server.call('add_standard_cake', 'Sponge Cake', '', 1, 'Buttercream', 'Lemon', 30.00, 8, 'Vanilla', 'Lemon Meringue cream')
    pass

  def button_add_o_click(self, **event_args):
    anvil.server.call('add_standard_cake', 'Sponge Cake', '', 1, 'Buttercream', 'Orange', 35.00, 8, 'Plain', 'Orange cream')
    pass

  def button_add_a_click(self, **event_args):
    anvil.server.call('add_standard_cake', 'Sponge Cake', '', 1, 'Buttercream', 'Almond', 25.00, 8, 'Plain', 'Almond cream')
    pass

  def button_add_c_o_click(self, **event_args):
    anvil.server.call('add_standard_cake', 'Sponge Cake', '', 1, 'Buttercream', 'Chocolate Orange', 25.00, 8, 'Chocolate', 'Orange cream')
    pass


    



