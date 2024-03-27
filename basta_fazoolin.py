class Menu:
  def __init__(self, name, items,start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
      
  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    total = 0
    for purchased_item in purchased_items:
      total += self.items[purchased_item]
    return total

class Franchise:
  def __init__(self, address, menus):
    self.menus = menus
    self.address = address

  def __repr__(self):
    return f"Address is: {self.address}"

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu("brunch", brunch_items, 11, 16)
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird_menu = Menu("early_bird", early_bird_items, 15, 18)
dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner_menu = Menu("dinner", dinner_items, 17, 23)
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu = Menu("kids", kids_items, 11, 21)

print("Total value of brunch for purchased-items: ", brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))

print("Total value of early-bird for purchased-items: ", early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)",]))

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store)
print(new_installment)

print(flagship_store.available_menus(17))

Basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu =  Menu("Take a' Arepa", arepa_items, 10, 20)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

business = Business("Take a' Arepa", arepas_place)

print("Thank you for your review!")

