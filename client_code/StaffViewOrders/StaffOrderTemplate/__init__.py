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
    
    if role == "Manager":
      self.staff_confirm_button.visible = True
      self.staff_reject_button.visible = True
    else:
      self.staff_confirm_button.visible = False
      self.staff_reject_button.visible = False

      

    #order = self.item

    self.price_label.text = "£" + str(order["total_price"]) + "   " + str(order['collection_date']) + "   " + order['order_status']
    #+ order["cake_type"]


  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    pass

  def staff_confirm_button_click(self, **event_args):
    anvil.server.call('confirm_order_status', self.item)
    alert("Order confirmed")
    pass

  def staff_reject_button_click(self, **event_args):
    anvil.server.call('reject_order_status', self.item['user'])
    alert("Order rejected")
    pass

