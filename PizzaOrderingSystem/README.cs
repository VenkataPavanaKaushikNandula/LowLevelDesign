----------------------------------------------------------------
                High Level Requirments
1. User should be able to order a Pizza with different options
2. User should be able to choose from different bases.
3. User should be able to choose different toppings one or more.
4. User should be able to choose a particular size of pizza.
5. System should summarize the total cost of the pizza.
----------------------------------------------------------------
                        Classes
1. PizzaBase an abstract class to implement different types of bases.
    At instance, implemented Thincrust, Thickcrust. Several other
    bases can be implemented using the abstraction.
2. PizzaSize an abstract class to implement different sizes of pizza.
3. Toppings is also an abstract class that can be used to implement
   different toppings which is extendable.
4. Pizza class is the main where pizza is constructed with chosen
options and the core calculation of prize and ordering logic is placed.
---------
