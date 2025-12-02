from ._anvil_designer import StaffOrderTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffOrder(StaffOrderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    order = self.item

    self.order_id_label.text = str(order["order_id"])
    self.cake_type_label.text = order["cake_type"]
    self.sponge_flav_label.text = order["sponge_flavour"]
    self.collection_date_label.text = order["collection_date"]

    # Any code you write here will run before the form opens.
