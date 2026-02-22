from ._anvil_designer import StaffViewOrdersTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffViewOrders(StaffViewOrdersTemplate):
  def __init__(self, role, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = role

    self.all_orders = anvil.server.call("get_all_order_info")
    self.order_repeating_panel.items = self.all_orders

    # Getting dropdowns to display
    order_list = []
    for row in app_tables.tblstaffdropdown.search(category = "sort"):
      order_list.append(row["choice"])
    self.sort_dropdown.items = order_list

    order_list = []
    for row in app_tables.tblstaffdropdown.search(category = "filter"):
      order_list.append(row["choice"])
    self.filter_dropdown.items = order_list
    
  # QUICKSORT to sort order based on the selected dropdown
  def quicksort(self, orders, start, end, sort_value):
    if start >= end:
      return orders

    pivot = orders[start]
    low = start + 1
    high = end

    while True:
      # Low pointer
      while low <= high and orders[low][sort_value] <= pivot[sort_value]:
        low = low + 1

      # High pointer
      while high >= low and orders[high][sort_value] >= pivot[sort_value]:
        high = high - 1

      if low < high:
        temp = orders[low]
        orders[low] = orders[high]
        orders[high] = temp
      else:
        break

    # Swap pivot into the correct position
    temp = orders[start]
    orders[start] = orders[high]
    orders[high] = temp

    self.quicksort(orders, start, high - 1, sort_value)
    self.quicksort(orders, high + 1, end, sort_value)

    return orders

  # INVERSE QUICKSORT
  def inverse_quicksort(self, orders, start, end, sort_value):
    if start >= end:
      return orders

    pivot = orders[start]
    low = start + 1
    high = end

    while True:
      # Low pointer
      while low <= high and orders[low][sort_value] >= pivot[sort_value]:
        low = low + 1

      # High pointer
      while high >= low and orders[high][sort_value] <= pivot[sort_value]:
        high = high - 1

      if low < high:
        temp = orders[low]
        orders[low] = orders[high]
        orders[high] = temp
      else:
        break

    # Swap pivot into the correct position
    temp = orders[start]
    orders[start] = orders[high]
    orders[high] = temp

    self.inverse_quicksort(orders, start, high - 1, sort_value)
    self.inverse_quicksort(orders, high + 1, end, sort_value)

    return orders
      
  def home_button_click(self, **event_args):
    open_form("StaffDashboard", role = self.role)
    pass
    
  def sort_dropdown_change(self, **event_args):
    selected = self.sort_dropdown.selected_value
    if selected == "All Orders":
      self.order_repeating_panel.items = self.all_orders

    if selected == "Price Low to High":
      sort_value = "total_price"
      sorted_orders = self.quicksort(self.all_orders[:], 0, len(self.all_orders) - 1, sort_value)
      self.order_repeating_panel.items = sorted_orders

    if selected == "Nearest Collection Date":
      sort_value = "collection_date"
      sorted_orders = self.quicksort(self.all_orders[:], 0, len(self.all_orders) - 1, sort_value)
      self.order_repeating_panel.items = sorted_orders

    if selected == "Price High to Low":
      sort_value = "total_price"
      sorted_orders = self.inverse_quicksort(self.all_orders[:], 0, len(self.all_orders) - 1, sort_value)
      self.order_repeating_panel.items = sorted_orders

  # LINEAR SEARCH
  # Searches for orders based on certain criteria
  def linear_search(self, orders, field, search_item):
    # Empty list of results that will be displayed
    results = []
    current = 0

    # Repeat while then end of the list has not been reached
    while current < len(orders):
      # Compare the item at the current index to the search item
      if orders[current][field] == search_item:
        results.append(orders[current])
      # Moves to next search item
      current = current + 1

    # Return results
    return results
 
  @handle("filter_dropdown", "change")
  def filter_dropdown_change(self, **event_args):
    filter = self.filter_dropdown.selected_value

    # Filter for confirmed orders
    if filter == "Confirmed Orders":
      field = "order_status"
      search_item = "Confirmed"
      filtered_orders = self.linear_search(self.all_orders, field, search_item)
      self.order_repeating_panel.items = filtered_orders

    # Filter for rejected orders
    if filter == "Rejected Orders":
      field = "order_status"
      search_item = "Rejected"
      filtered_orders = self.linear_search(self.all_orders, field, search_item)
      self.order_repeating_panel.items = filtered_orders

    # Filter for cancelled orders
    if filter == "Cancelled Orders":
      field = "order_status"
      search_item = "Cancelled"
      filtered_orders = self.linear_search(self.all_orders, field, search_item)
      self.order_repeating_panel.items = filtered_orders

    # Filter for pending orders
    if filter == "Pending Orders":
      field = "order_status"
      search_item = "Pending"
      filtered_orders = self.linear_search(self.all_orders, field, search_item)
      self.order_repeating_panel.items = filtered_orders

    # Filter for completed orders
    if filter == "Completed Orders":
      field = "order_status"
      search_item = "Completed"
      filtered_orders = self.linear_search(self.all_orders, field, search_item)
      self.order_repeating_panel.items = filtered_orders

    # Displaying all orders
    if filter == "All Orders":
      self.order_repeating_panel.items = self.all_orders



  

      
