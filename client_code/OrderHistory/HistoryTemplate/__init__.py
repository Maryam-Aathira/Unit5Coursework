from ._anvil_designer import HistoryTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class HistoryTemplate(HistoryTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    order = self.item
    cakes = anvil.server.call("display_cake",order)

    cake_info = ""
    # Adding information from tblOrderItems into a list for each cake
    for cake in cakes:
      cake_info = f"{cake['sponge_flavour']} {cake['cake_type']}\n{cake['filling']} filling\n{cake['frosting_flavour']} {cake['frosting_type']}"
    self.cake_name_label.text = cake_info
    self.date_label.text = "Date of Order: " + str(self.item["date_of_order"].strftime("%d/%m/%Y"))
    self.status_label.text = "Order Status: " + str(self.item["order_status"])
    self.collection_date_label.text = "Collection Date: " + str(self.item["collection_date"].strftime("%d/%m/%Y"))
    self.reference_picture.source = cake["reference_image"]

    # Need to get price from tblOrderItems
    self.price_label.text = "£" + str(self.item["total_price"])
    self.break_label.text = "-----------------------------------------------------------------------------------"

