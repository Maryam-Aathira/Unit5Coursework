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
  def __init__(self, cake_type = "Sponge Cake", flavour = "Blank", price = 0.00):
    self.cake_type = cake_type
    self.flavour = flavour
    self.price = price

  def add_to_order(self):
    anvil.server.call('add_standard_cake', self.cake_type, self.flavour, self.price)


class Vanilla(Cake):
  def __init__(self):
    super().__init__
    self.flavour = "Vanilla"
    self.price = 30.00
