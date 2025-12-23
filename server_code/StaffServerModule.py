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
def get_all_order_info(): 
  combined = []
  for item in app_tables.tblorderitems.search():
    order = item['order_id']      
    user = order['user']      

    # Building one combined dictionary 
    combined.append({
      'customer': f"{user['firstname']} {user['surname']}",
      'order_id': order['order_id'],
      'collection_date': order['collection_date'],
      'order_status': order['order_status'],
      'date_of_order': order['date_of_order'],
      'total_price': order['total_price'],

      # Order Item details
      'cake_type': item['cake_type'],
      'sponge_flavour': item['sponge_flavour'],
      'filling': item['filling'],
      'frosting_type': item['frosting_type'],
      'frosting_flavour': item['frosting_flavour'],
      'occasion': item['occasion'],
      'serving_size': item['serving_size'],
      'no_of_tiers': item['no_of_tiers'],
      'allergies': item['allergies'],
      'inscription': item['inscription'],
      'additional_details': item['additional_details'],
    })
  print(f"Orders:{combined}")
  return combined

  
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
  