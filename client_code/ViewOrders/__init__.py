from ._anvil_designer import ViewOrdersTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ViewOrders(ViewOrdersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.current_order = []
   # user = anvil.users.get_user()
    

    # Any code you write here will run before the form opens.

  def view_account_click(self, **event_args):
    open_form('ViewAccount')
    pass

  def home_click(self, **event_args):
    open_form('Home')
    pass

  #def confirm_order_click(self, **event_args):
   # for cake in self.current_order:
    #  anvil.server.call('add_custom_cake', 
     #                   cake["cake_type"],
      #                  cake["sponge_flavour"])
    #pass
