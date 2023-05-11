class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        # Update orders and coffees in Customer and Coffee instances
        self.customer.orders(self)
        self.customer.coffees(self.coffee)
        self.coffee.orders(self)
        self.coffee.customers(self.customer)

        # Add the new order to the Order.all list
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from classes.customer import Customer
        if not isinstance(value, Customer):
            raise Exception("Invalid input: customer must be of type Customer.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from classes.coffee import Coffee
        if not isinstance(value, Coffee):
            raise Exception("Invalid input: coffee must be of type Coffee.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 1 or value > 10:
            raise Exception("Invalid input: price must be a number between 1 and 10.")
        self._price = value
