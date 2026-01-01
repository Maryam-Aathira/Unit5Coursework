from ._anvil_designer import StatisticsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from plotly import graph_objects as go


class Statistics(StatisticsTemplate):
  def __init__(self,role, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = role 
    Plot.templates.default = "material_light"
    selected_date = self.week_date_picker 
    anvil.server.call("get_week", selected_date)
  # Creating income report as a graph
    
    self.plot_1.data = [
#      go.Scatter(
 #       x = [1, 2, 3],
  #      y = [3, 1, 6],
   #     marker = dict(
    #      color= 'rgb(10, 12, 10)'
     #   )
    #  ),
      go.Bar(
        x = [1, 2, 3],
        y = [3, 1, 6],
        name = 'Income'
      )
    ]


  
  def home_button_click(self, **event_args):
    open_form('StaffDashboard')
    pass
