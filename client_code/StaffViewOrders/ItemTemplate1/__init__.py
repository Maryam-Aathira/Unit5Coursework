from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    role = get_open_form().role
    # Ensuring rejection is not visible initally
    self.rejection_reason.visible = False
    self.rejection_reason_dropdown.visible = False
    self.confirm_rejection.visible = False

    # Making the confirm button green
    self.confirm_button.background = "#238823"
    self.confirm_button.foreground = "#ffffff"

    # Making the reject button red
    self.reject_button.background = "#d2222d"
    self.reject_button.foreground = "#ffffff"

    self.confirm_rejection.background = "#d2222d"
    self.confirm_rejection.foreground  = "#ffffff"
    self.confirm_rejection.bold

    # Implementing user permissions
    if role == "Manager":
      self.confirm_button.visible = True
      self.reject_button.visible = True
    else:
      self.confirm_button.visible = False
      self.reject_button.visible = False


  # Confirming the order
  @handle("confirm_button", "click")
  def confirm_button_click(self, **event_args):
    #  weekly_orders = anvil.server.call("check_weekly_orders")
    # max_weekly_orders = 3
    # if weekly_orders >= max_weekly_orders:
    #   confirm("Are you sure you want to accept any more orders?")

    # Updating order status in the database
    final_order = self.item["order_row"]
    anvil.server.call('confirm_order_status', final_order)
    alert("Order confirmed")
    # Updating the table
    self.order_status.text = "Confirmed"
    self.order_status.role = None
    self.confirm_button.visible = False
    self.reject_button.visible = False
    #self.mark_complete_button = False

  @handle("reject_button", "click")
  def reject_button_click(self, **event_args):
    # Rejection reason dropdown
    item_list = []
    for row in app_tables.tblstaffdropdown.search(category="rejection"):
      item_list.append(row["choice"])
      self.rejection_reason_dropdown.items = item_list

    self.rejection_reason_dropdown.visible = True
    self.confirm_rejection.visible = True
    pass

  @handle("rejection_reason_dropdown", "change")
  def rejection_reason_dropdown_change(self, **event_args):
    rejection = self.rejection_reason_dropdown.selected_value
    if rejection != "Other":
      self.rejection_reason.visible = False
      self.rejection_reason.text = ""
    else:
      self.rejection_reason.visible = True
    pass


  @handle("confirm_rejection", "click")
  def confirm_rejection_click(self, **event_args):
    rejection = self.rejection_reason_dropdown.selected_value
    if rejection == "Other":
      rejection = self.rejection_reason.text
    # Updating order status in the database
    final_order = self.item["order_row"]
    anvil.server.call('reject_order_status', final_order, rejection)
    # Updating the table
    alert("Order rejected")
    self.order_status.text = "Rejected"
    self.order_status.role = None
    self.confirm_button.visible = False
    self.reject_button.visible = False
    self.rejection_reason.visible = False
    self.rejection_reason_dropdown.visible = False
    self.confirm_rejection.visible = False
    self.mark_complete_button = False
    pass

  @handle("mark_complete_button", "click")
  def mark_complete_button_click(self, **event_args):
    final_order = self.item["order_row"]
    anvil.server.call("mark_order_as_complete", final_order)
    pdf = anvil.server.call("send_invoice", self.item)
    anvil.media.download(pdf)
    alert("Order marked as complete")
    self.order_status.text = "Completed"
    pass


