from ._anvil_designer import StatisticsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Statistics(StatisticsTemplate):
  def __init__(self,role, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = role 
    Plot.templates.default = "material_light"
    
    # Creating a template for the empty graphs
    self.plot_1.data = [
      go.Bar(
        x = ["Cancelled", "Rejected", "Total items"],
        y = [0,0,0],
        name = "Weekly Statistics"
      )
    ]

    self.income_plot.data = [
      go.Bar(
        x = ["Income"],
        y = 0,
        name = "Income"
      )
    ]

    self.reasons_plot.data = [
      go.Pie(
       labels = "",
       values = "",
      )
    ]
    # Creating the plot layout designs
    self.plot_1.layout = {
      "title": {"text": "Types of Orders"},
      "xaxis": {"title": {"text": "Order statuses"}},
      "yaxis": {"title": {"text": "Number of orders"}}
    }

    self.reasons_plot.layout = {
      "title": {"text": "Reasons for cancellations and rejections"}
    }

    
  @handle("view_stats_button", "click")
  def view_stats_button_click(self, **event_args):
    # Finding the week
    selected_date = self.week_date_picker.date
    if selected_date is None:
      alert("Please select a start date")
      return
    start_of_week, end_of_week = anvil.server.call("get_week", selected_date)
    reason_count = anvil.server.call("get_reasons", start_of_week, end_of_week)
    # Formatting to DD/MM/YYYY
    start = start_of_week.strftime("%d/%m/%Y")
    end = end_of_week.strftime("%d/%m/%Y")
    self.graph_info_label.text = f"From {start} to {end}"

    
    # Getting the actual statistics
    stats = anvil.server.call("get_weekly_stats", start_of_week, end_of_week)
      
    # Creating the report as a bar graph
    self.plot_1.data = [
      go.Bar(
        x = ["Cancelled", "Rejected", "Total items"],
        y = [stats["cancelled"], stats["rejected"], stats['total items']],
        name = 'Weekly Statistics'
      )
    ]

    self.income_plot.data = [
      go.Bar(
        x = ["Income"],
        y = [stats["income"]], 
        name = "Income"
      )
    ]

    pass  

    # Creating a cancellations and rejections reasons pie charts
    labels = list(reason_count.keys())
    values = list(reason_count.values())
    self.reasons_plot.data = [
      go.Pie(
        labels = labels,
        values = values
      )
    ]

  
  def home_button_click(self, **event_args):
    open_form('StaffDashboard')
    pass



