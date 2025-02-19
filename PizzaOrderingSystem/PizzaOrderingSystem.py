from abc import ABC, abstractmethod
""" We can opt for a modular design, which is straightforward and easier to implement. 
    However, this approach may lack adherence to core OOP principles, resulting in a less 
    structured and less scalable solution. While modular design (using classes for base, size,
    and pizza, and creating objects as needed) works well for simple requirements, 
    it can become complex when additional specifications or behaviors are introduced. 
    Handling such scenarios may require extra validations or overriding mechanisms, 
    leading to increased maintenance effort and reduced code clarity.
    
    Use Modular Design When:
        The differences between options (base, size, topping) are purely data-driven (e.g., name and price).
        You want simplicity and the ability to quickly add or modify options without modifying the class structure.
        The logic associated with each option is uniform or minimal.
    
    Use Inheritance-Based Design When:
        Each option (e.g., Thin Crust, Thick Crust) has unique behavior or requires additional methods and attributes.
        You need polymorphism for clean handling of different option types.
        You foresee complex business logic for future extensions (e.g., special rules for combinations of sizes, toppings, and bases).
"""
class PizzaBase(ABC):
    """Abstraction for base 
    this is extendable."""
    @abstractmethod
    def price(self):
        pass
    @abstractmethod
    def description(self):
        pass
class ThinCrust(PizzaBase):
    def price(self):
        return 5.0
    def description(self):
        return "Thin Crust Pizza"
class ThickCrust(PizzaBase):
    def price(self):
        return 7.0
    def description(self):
        return "Thick Crust Pizza"

class PizzaSize(ABC):
    @abstractmethod
    def get_multiplier(self):
        pass
    @abstractmethod
    def description(self):
        pass
class SmallSize(PizzaSize):
    def get_multiplier(self):
        return 1.0
    def description(self):
        return "Small Size 12\" Pizza."
class MediumSize(PizzaSize):
    def get_multiplier(self):
        return 1.5
    def description(self):
        return "Medium Size 16\" Pizza"
class LargeSize(PizzaSize):
    def get_multiplier(self):
        return 2.5
    def description(self):
        return "Large Size 20\" Pizza "

class Toppings(ABC):
    @abstractmethod
    def price(self):
        pass
    @abstractmethod
    def description(self):
        pass
class TomatoTopping(Toppings):
    def price(self):
        return 0.99
    def description(self):
        return "Sliced fresh tomato"
class CheeseTopping(Toppings):
    def price(self):
        return 0.99
    def description(self):
        return "Fresh Diary Cheese"
class PepperoniTopping(Toppings):
    def price(self):
        return 1.99
    def description(self):
        return "Pepperoni"
    
class Pizza:
    def __init__(self, base, size) -> None:
        self.base = base
        self.size = size
        self.toppings = []
    def _add_toppings(self, topping):
        self.toppings.append(topping)
    def _calculate_price(self):
        baseprice = self.base.price()
        sizeprice = self.size.get_multiplier()
        toppingprice = sum(topping.price() for topping in self.toppings)
        return ( baseprice + toppingprice ) * sizeprice 
    def _generate_description(self):
        description  = f"{self.base.description()} pizza of {self.size.description()}"
        if self.toppings:
            top_desc = ", ".join(top.description() for top in self.toppings)
            description += top_desc
        else:
            description += "no toppings."
        return description

if __name__ == "__main__":
    print("Welcome to the Pizza Builder!")

    # Step 1: Select Base
    base_options = [ThinCrust(), ThickCrust()]
    print("\nSelect your pizza base:")
    for i, base in enumerate(base_options, 1):
        print(f"{i}. {base.description()} (${base.price():.2f})")
    base_choice = int(input("Enter your choice (1/2): ")) - 1
    selected_base = base_options[base_choice]

    # Step 2: Select Size
    size_options = [SmallSize(), MediumSize(), LargeSize()]
    print("\nSelect your pizza size:")
    for i, size in enumerate(size_options, 1):
        print(f"{i}. {size.description()} (Multiplier: {size.get_multiplier()})")
    size_choice = int(input("Enter your choice (1/2/3): ")) - 1
    selected_size = size_options[size_choice]

    # Step 3: Create Pizza
    pizza = Pizza(selected_base, selected_size)

    # Step 4: Select Toppings
    topping_options = [TomatoTopping(), CheeseTopping(), PepperoniTopping()]
    print("\nSelect your toppings (enter numbers separated by commas or leave blank for no toppings):")
    for i, topping in enumerate(topping_options, 1):
        print(f"{i}. {topping.description()} (${topping.price():.2f})")
    topping_choices = input("Enter your choices (e.g., 1,2): ").split(",")

    for choice in topping_choices:
        if choice.strip().isdigit():
            topping_index = int(choice.strip()) - 1
            if 0 <= topping_index < len(topping_options):
                pizza._add_toppings(topping_options[topping_index])

    # Step 5: Display Pizza Details
    print("\nYour Pizza Order Summary:")
    print(f"Description: {pizza._generate_description()}")
    print(f"Total Price: ${pizza._calculate_price():.2f}")
