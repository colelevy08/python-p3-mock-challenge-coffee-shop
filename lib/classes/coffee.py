class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []
        self._customers = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Coffee name cannot be changed after creation.")
        self._name = value

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order:
            if not isinstance(new_order, Order):
                raise Exception("Invalid input: order must be of type Order.")
            self._orders.append(new_order)
        return self._orders

    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer:
            if not isinstance(new_customer, Customer):
                raise Exception("Invalid input: customer must be of type Customer.")
            self._customers.add(new_customer)
        return list(self._customers)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders) if self._orders else 0
