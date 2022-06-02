# script.py

# cart item class
class CartItem:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity\

    def __str__(self):
        return self.name

    # get and Set for name
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    # get and set for quantity
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity):
        self.quantity = quantity
# shopping cart class
class ShoppingCart:
    # constructor
    def __init__(self):

        # List To Store All CartItems
        self.items = []

    # add item to cart
    def add(self, itemOther):

        # loop to check if the item is already in the cart
        found = False
        
        # loop all the items and check if the item matches any existing items
        for item in self.items:
            if item.getName() == itemOther.getName():
                # If Yes, Then Increase It's Quantity
                item.setQuantity(item.getQuantity() + itemOther.getQuantity())

                # flag set, and break loop
                found = True
                break
        
        # if item is not found in the list, add it
        if not found:
            self.items.append(itemOther)
                
    # return true if the list is empty
    def isEmpty(self):
        return len(self.items) == 0

    # return list of all cart items
    def getItems(self):
        return self.items

    # removes an item from list
    def remove(self, itemOther):

        # Loop Through All The Items And Check If The Item 
        # Matches Any Existing Item
        for item in self.items:
            if item.getName() == itemOther.getName():
                # If The Item Is Found, Remove It And Exit
                self.items.remove(item)
                break
    
    # return the quantity of the item
    def getQuantity(self, itemOther):
        # Loop Through All The Items And Check If The Item 
        # Matches Any Existing Item
        for item in self.items:
            if item.getName() == itemOther.getName():
                # If Yes, Then Return It's Quantity
                return item.getQuantity()
        return 0

    # clears cart
    def clear(self):
        self.items.clear()
