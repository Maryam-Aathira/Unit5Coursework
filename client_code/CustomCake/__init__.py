from ._anvil_designer import CustomCakeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CustomCake(CustomCakeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    open_form('Home')
    pass

  def cake_type_dropdown_change(self, **event_args):
    item_list = []
    for row in app_tables.tbldropdownoptions.search():
      item_list.append
    pass
