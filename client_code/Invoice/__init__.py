from ._anvil_designer import InvoiceTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Invoice(InvoiceTemplate):
  def __init__(self, order, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = order

    # Any code you write here will run before the form opens.
