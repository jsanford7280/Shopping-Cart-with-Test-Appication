# shopping cart test

import unittest
from testscript import *

# test shopping cart class
class ShoppingCartTests(unittest.TestCase):

# test add 
    def testAdd(self):
        cart = ShoppingCart()
        self.assertEquals(cart.isEmpty(), True)

        cart.add(CartItem("NoteBook", 1))
        self.assertEquals(cart.isEmpty(), False)

        items = cart.getItems()
        self.assertEquals(len(items), 1)

# test remove
    def testRemove(self):
        itemPencil = CartItem("Pencil", 1)
        itemNoteBook = CartItem("NoteBook", 1)
        
        cart = ShoppingCart()
        cart.add(itemPencil)
        cart.add(itemNoteBook)

        self.assertEquals(len(cart.getItems()), 2)
        cart.remove(itemPencil)
        self.assertEquals(len(cart.getItems()), 1)
        
        item = cart.getItems()[0]

        self.assertEquals(item, itemNoteBook)

        cart.remove(itemNoteBook)

        self.assertEquals(cart.isEmpty(), True)

# test GetQuantity
    def testGetQuantity(self):
        itemPencil = CartItem("Pencil", 1)
        itemNoteBook = CartItem("NoteBook", 1)
        itemPencilOther = CartItem("Pencil", 2)

        cart = ShoppingCart()
        cart.add(itemPencil)

        self.assertEquals(cart.getQuantity(itemPencil), 1)
        self.assertEquals(cart.getQuantity(itemNoteBook), 0)

        cart.add(itemPencilOther)
        self.assertEquals(cart.getQuantity(itemPencil), 3)

# test IsEmpty 
    def testIsEmpty(self):
        cart = ShoppingCart()
        self.assertEquals(cart.isEmpty(), True)

        cart.add(CartItem("NoteBook", 1))
        self.assertEquals(cart.isEmpty(), False)

    
# test GetItems 
    def testGetItems(self):
        itemPencil = CartItem("Pencil", 1)
        itemNoteBook = CartItem("NoteBook", 1)
        itemPencilOther = CartItem("Pencil", 2)

        cart = ShoppingCart()

        self.assertEquals(len(cart.getItems()), 0)

        cart.add(itemPencil)
        cart.add(itemNoteBook)
        cart.add(itemPencilOther)

        items = cart.getItems()
        self.assertEquals(len(items), 2)
        

# test Clear 
    def testClear(self):
        itemPencil = CartItem("Pencil", 1)
        cart = ShoppingCart()
        cart.add(itemPencil)

        self.assertEquals(cart.isEmpty(), False)

        cart.clear()

        self.assertEquals(cart.isEmpty(), True)
