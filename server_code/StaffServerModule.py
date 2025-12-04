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
    
  
    
#@anvil.server.callable
#def get_every_order():
 # all_orders = []
  #for order in app_tables.tblorders.search():
   # cakes = list(app_tables.tblorderitems.search(order = order))
    #cake_info = []
#    for cake in cakes:
 #     cake_info.append({"cake_type" : cake["cake_type"],
  #                 "sponge_flavour" : cake["sponge_flavour"],

   #               })
    #  all_orders.append({
     #   "total_price" : order['total_price'],
      #  "collection_date" : order['collection_date']     
   #   }
        
    #  )
 # return all_orders
  
                   #"order_id" : order["order"],
  