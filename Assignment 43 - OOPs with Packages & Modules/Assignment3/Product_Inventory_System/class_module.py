class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print(
            self.product_id,
            self.product_name,
            self.price,
            self.quantity
        )
