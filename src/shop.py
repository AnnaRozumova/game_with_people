'''
Task:
1) There is pytest possible to use, it was installed with pipenv to this virtual environment
=> make test of 1 method from class Shop

Ondra's note for future (unit test,pytest,pylint install to virt.env, pyside2 (button to add customer and shop), 
write to file json? or csv,read it..filesystem work
with pipenv, maybe boto3 and dynamodb and s3..maybe docker and bashscripts and terminal,fastapi)
'''
from .human import Human


class Shop():
    def __init__(self, name: str, assortment: dict):
        self.name = name
        self.assortment = assortment

    def buy_product(self, product, amount_to_buy, customer):
        try:
            if amount_to_buy <= self.assortment[product]['amount']:
                self.assortment[product]['amount'] -= amount_to_buy
                price = self.assortment[product]['price'] * amount_to_buy
                return f'For {amount_to_buy} of {product} you will pay {price} korun'
            else:
                return f'Sorry, {customer.last_name} we dont have enough of {product}'
        except KeyError:
            print('Wrong name of product')

    def show_assortment(self, customer):
        if customer.sex == 'woman':
            return f'Dear Mrs. {customer.last_name}, we have today in {self.name} following products: {self.assortment}'
        else:
            return f'Dear Mr. {customer.last_name}, we have today in {self.name} following products: {self.assortment}'


if __name__ == "__main__":
    customer_1 = Human(34, 'woman', 'Anna', 'Rozumova', 160, 'blond')
    customer_2 = Human(40, 'man', 'Ondra', 'Rozum', 185, 'brown')
    customer_3 = Human(25, 'woman', 'Benik', 'Bibik', 108, 'red')
    shop1 = Shop('Albert', {'rohlik': {'price': 3, 'amount': 100}, 'chleba': {'price': 25, 'amount': 100}, 'ryze': {'price': 30, 'amount': 100}})
    answer_to_customer = shop1.buy_product('rohlik', 101, customer_1)
    print(answer_to_customer)
    what_we_have = shop1.show_assortment(customer_2)
    print(what_we_have)
    answer_to_customer = shop1.buy_product('rohlik', 10, customer_2)
    print(answer_to_customer)
