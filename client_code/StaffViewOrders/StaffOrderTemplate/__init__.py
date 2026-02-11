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
    role = get_open_form().role


    order = self.item
    cakes = anvil.server.call('display_cake', order)

    # Adding information from tblOrderItems into a list for each cake
    for cake in cakes:
      cake_info = f"{cake['sponge_flavour']} {cake['cake_type']}\n{cake['filling']} filling\n{cake['frosting_flavour']} {cake['frosting_type']}"
    self.info_label.text = cake_info
    self.price_label.text = "£" + str(order["total_price"]) + "   " + str(order['collection_date']) + "   " 
    self.status_label.text = str(order['order_status'])
    self.reference_picture.source = cake["reference_image"]

    if role == "Manager":
      self.staff_confirm_button.visible = True
      self.staff_reject_button.visible = True
    else:
      self.staff_confirm_button.visible = False
      self.staff_reject_button.visible = False


  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    pass

