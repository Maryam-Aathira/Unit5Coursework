import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_all_orders():
  return app_tables.tblorders.search()
  
@anvil.server.callable
def get_all_orders_from_orderitems():
  return app_tables.tblorderitems.search()

@anvil.server.callable
def confirm_order_status(order):
 # orders = app_tables.tblorders.search(order_id = order_id)
  #for order in orders:
    if order['order_status'] == "Pending":
      order['order_status'] = "Confirmed"
    return order

@anvil.server.callable
def reject_order_status(order):
  #orders = app_tables.tblorders.search(order_id = order_id)
  #for order in orders:
    if order['order_status'] == "Pending":
      order['order_status'] = "Rejected"
    return order
    
@anvil.server.callable
def display_order(order):
  cakes = app_tables.tblorderitems.search(order_id = order)
  return cakes
  