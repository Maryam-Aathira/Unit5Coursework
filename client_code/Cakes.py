import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1
#
#    Module1.say_hello()
#




class Cake():
  def __init__(self, name = "Blank", price = 0.00):
    self.name = name 
    self.price = price

  def add_standard_cake_to_order(self):
    anvil.server.call('add_standard_cake', self.name, self.price)


class Vanilla(Cake):
  def __init__(self, name, price):
    super.__init__
    self.name = "Vanilla"
    self.price = 30.00
