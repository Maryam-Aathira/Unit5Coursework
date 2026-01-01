from ._anvil_designer import StatisticsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from plotly import graph_objects as go


class Statistics(StatisticsTemplate):
  def __init__(self,role, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = role 
    Plot.templates.default = "material_light"
    
    # Creating a template for the empty graph
    self.plot_1.data = [
      go.Bar(
        x = ["Income", "Cancelled", "Rejected"],
        y = [0,0,0],
        name = "Weekly Statistics"
      )
    ]
    
  @handle("view_stats_button", "click")
  def view_stats_button_click(self, **event_args):
    # Finding the week
    selected_date = self.week_date_picker.date
    start_of_week, end_of_week = anvil.server.call("get_week", selected_date)
    if selected_date is None:
      alert("Please select a start date")
    self.graph_info_label.text = f"{start_of_week} to {end_of_week}"
    # Getting the actual statistics
    stats = anvil.server.call("get_weekly_stats", start_of_week, end_of_week)
      
     # Creating the report as a graph
    self.plot_1.data = [
        #      go.Scatter(
        #       x = [1, 2, 3],
        #      y = [3, 1, 6],
        #     marker = dict(
        #      color= 'rgb(10, 12, 10)'
        #   )
        #  ),
      go.Bar(
        x = ["Income", "Cancelled", "Rejected"],
        y = [stats["income"], stats["cancelled"], stats["rejected"]],
        name = 'Income'
      )
    ]
    pass


    
    
  

  
  def home_button_click(self, **event_args):
    open_form('StaffDashboard')
    pass



