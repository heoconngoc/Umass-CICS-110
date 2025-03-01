# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949
class Item:
  def __init__(self, name, price, quantity):
    self.name = name 
    self.price = price
    self.quantity = quantity
  
  def __eq__(self, other):
    if isinstance(other, Item):
      return self.name == other.name
    return False
  
  def __repr__(self):
        return f"Item (name={self.name}, price={self.price}, quantity={self.quantity})"

class VendingMachine:
  def __init__(self):
    self.items = []
    self.sale_history = []
    self.total_sales = 0
    self.balance = 0

  def __repr__(self):
    return f"Vending Machine (items={self.items}, total_sales={self.total_sales}, sale_history={self.sale_history}, balance={self.balance})"

  def add_item(self, name, price, quantity):
    newItem = Item(name, price, quantity)
    if newItem not in self.items:
      self.items.append(newItem)
    else:
      for item in self.items:
        if item == newItem:
          item.quantity += quantity
          item.price = price
          break
    print(f'{quantity} {name}(s) added to inventory')

  def get_item_price(self, name):
    for item in self.items:
      if item.name == name:
        return item.price
    print('Invalid item')
    return None
  
  def get_item_quantity(self, name):
    for item in self.items:
      if item.name == name:
        return item.quantity
    print('Invalid item')
    return None
  
  def list_items(self):
    if not self.items:
      print("No items in the vending machine")
    else:
      print("Available items:")
      sorted_items = sorted(self.items, key=lambda item: item.name)
      for item in sorted_items:
        print(f"{item.name} (${item.price}): {item.quantity} available")
  
  def insert_money(self, dollar):
    if dollar != 1.0 and dollar != 2.0 and dollar != 5.0:
      print("Invalid amount")
      return
    self.balance += dollar
    self.balance = round(self.balance,2)
    print(f"Balance: {self.balance}")
  
  def purchase(self, name):
    for item in self.items:
      if item.name == name:
        if item.quantity == 0:
          print(f"Sorry {item.name} is out of stock")
          return
        if self.balance < item.price:
          print(f"Insufficient balance. Price of {item.name} is {item.price}")
          return
        else:
          item.quantity -= 1
          self.balance = round(self.balance - item.price, 2)
          print(f"Purchased {name}")
          print(f"Balance: {self.balance}")
          self.total_sales = round(self.total_sales + item.price, 2) 
          self.sale_history.append((item.name, item.price, 1))
          return
    print("Invalid item")
    return
  
  def output_change(self):
    if self.balance == 0:
      print("No change")
    else:
      print(f"Change: {self.balance}")
      self.balance = 0
  
  def remove_item(self, name):
    for item in self.items:
      if item.name == name:
        self.items.remove(item)
        print(f"{item.name} removed from inventory")
        return
    print("Invalid item")
  
  def empty_inventory(self):
    self.items.clear()
    print("Inventory cleared")
  
  def get_total_sales(self):
    return self.total_sales
  
  def stats(self, n):
    if not self.sale_history:
      print("No sale history in the vending machine")
      return
    recent_sales = self.sale_history[-n:] if n <= len(self.sale_history) else self.sale_history
    
    sales_summary = {}
    for name, total_cost, quantity in recent_sales:
        if name in sales_summary:
            sales_summary[name]["quantity"] += quantity
            sales_summary[name]["total_sales"] += total_cost
        else:
            sales_summary[name] = {"quantity": quantity, "total_sales": total_cost}

    sorted_sales = sorted(sales_summary.items())

    print(f"Sale history for the most recent {len(recent_sales)} purchase(s):")
    for name, stats in sorted_sales:
        print(f"{name}: ${stats['total_sales']} for {stats['quantity']} purchase(s)")

# # Create a new vending machine
# vending_machine = VendingMachine()

# # Add some items to the inventory
# vending_machine.add_item('Soda', 1.50, 5)
# vending_machine.add_item('Chips', 0.75, 10)
# vending_machine.add_item('Candy', 0.50, 15)

# # Show the available items
# vending_machine.list_items()

# # Insert some coins
# vending_machine.insert_money(1.00)
# vending_machine.insert_money(1.00)

# # Purchase an item
# vending_machine.purchase('Soda')

# # Get the price of an item
# print(vending_machine.get_item_price('Chips'))

# # Purchase another item
# vending_machine.purchase('Chips')

# # Get the total sales
# print(vending_machine.get_total_sales())

# # Insert some coins
# vending_machine.insert_money(5.00)
# vending_machine.insert_money(5.00)

# # Purchase another item
# vending_machine.purchase('Chips')
# vending_machine.purchase('Chips')
# vending_machine.purchase('Chips')
# vending_machine.purchase('Candy')
# vending_machine.purchase('Candy')

# # print stats
# vending_machine.stats(3)
# vending_machine.stats(5)
# vending_machine.stats(10)

# # Remove an item
# vending_machine.remove_item('Candy')

# # Show the available items again
# vending_machine.list_items()

# # Get the quantity of an item
# print(vending_machine.get_item_quantity('Gum'))

# # Empty the inventory
# vending_machine.empty_inventory()

# # Show the available items again
# vending_machine.list_items()
