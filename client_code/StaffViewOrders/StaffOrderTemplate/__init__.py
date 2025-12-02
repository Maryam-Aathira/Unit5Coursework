from ._anvil_designer import StaffOrderTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffOrderTemplate(StaffOrderTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    order = self.item

    self.price_label.text = "£" + str(order["total_price"]) + "   " + str(order['collection_date']) + "   " + order["cake_type"]


  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    pass

