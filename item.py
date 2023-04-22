class Item:
    pay_rate = 1

    def __init__(self, goods_name, price, quantity):
        self.goods_name = goods_name
        self.price = price
        self.quantity_of_goods = quantity

    def calculate_total_price(self):
        overall_price_ = self.price * self.quantity_of_goods
        return overall_price_

    def apply_discount(self):
        self.price *= self.pay_rate


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
print(item1.price)
Item.pay_rate = 0.8
item1.apply_discount()
print(item1.price)
print(item2.price)
