from ._anvil_designer import BrowseTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# importing my own libraries
from datetime import date

class Browse(BrowseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.current_order = None

  # Direct to home page
  def home_click(self, **event_args):
    open_form("Home")
    pass
  # Directs to view orders page
  def view_orders_click(self, **event_args):
    open_form('ViewOrders')
    pass
  
  # CHECK!!!!!!!!
  def vanilla_add_click(self, **event_args):
    if self.current_order == None:
      self.current_order = app_tables.tblOrders.add_row(
        order_status = 'Pending Review',
        customer = self.chosen_customer
      )
          
    vanilla_cake = self.the_vanilla
    app_tables.tblOrderItems.add_row(
      order = self.current_order,
      cake_type = vanilla_cake['Sponge cake'],
      sponge_flavour = vanilla_cake['Vanilla'], 
      serving_size = vanilla_cake[10],
    )
 


    # MESSAGEBOX or something 
    pass


