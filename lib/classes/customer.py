class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise Exception("Invalid input: name must be a string with length between 1 and 15.")
        self._name = value

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order:
            if not isinstance(new_order, Order):
                raise Exception("Invalid input: order must be of type Order.")
            self._orders.append(new_order)
        return self._orders

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee:
            if not isinstance(new_coffee, Coffee):
                raise Exception("Invalid input: coffee must be of type Coffee.")
            self._coffees.add(new_coffee)
        return list(self._coffees)

    def create_order(self, coffee, price):
        from classes.order import Order
        new_order = Order(self, coffee, price)
        return new_order
