print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

menu=[
    "Wings",
    "Cookies",
    "Spring Rolls",
    "Salmon","Steak",
    "Meat Tornado",
    "A Literal Garden",
    "Ice Cream",
    "Cake",
    "Pie",
    "Coffee",
    "Tea",
    "Unicorn Tears"
]

count=[0,0,0,0,0,0,0,0,0,0,0,0,0]

set_order = input(">")

def get_order( count, set_order ,menu ):
 while set_order!="quit":
    
  if set_order in menu:
      count[menu.index(set_order)]+=1
      print(f"{count[menu.index(set_order)]} order of {set_order} have been added to your meal ")
  else:
      print("This order is not on the menu ,Please Choose Something From The Menu")
  set_order = input('>')

get_order( count ,set_order ,menu )
