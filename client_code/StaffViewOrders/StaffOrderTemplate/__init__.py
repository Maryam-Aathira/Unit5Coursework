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
   # self.role = role
    order = self.item
    role = get_open_form().role
    #self.price_label.visible = True

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

      

    #order = self.item




  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    pass

   # cake_info = ""

    
  def staff_confirm_button_click(self, **event_args):
    anvil.server.call('confirm_order_status', self.item)
    alert("Order confirmed")
    self.status_label.text = "Confirmed"
    

  def staff_reject_button_click(self, **event_args):
    anvil.server.call('reject_order_status', self.item)
    alert("Order rejected")
    self.status_label.text = "Rejected"
  


 #   self.date_label.text = "Date of Order: " + str(self.item["date_of_order"])
  #  self.status_label.text = "Order Status: " + str(self.item["order_status"])
   # self.info_label.text = "Collection Date: " + str(self.item["collection_date"])