'''
Task:
1) study little bit basic usage of git
https://realpython.com/python-git-github-intro/

2) make an account on github  - Done
3) initialize in this project usage as git repository 
4) connect this repository to github account 
------------------------------------------------

5) change some file little bit (even just commentary)
6) stage the change in git in vscode
7) and commit it and synchronize (or push) in vscode to that github
================================================

6) study little bit basic usage of pipenv
7) install pipenv from linux terminal eventhough it is installed (in some case it will just write that it is already installed)

8) create virtual environment for this play_with_people project
9) use this virtual environment in this project
10) there should be now Pipfile and Pipfile.lock (?)

Ondra's note for future (unit test,pytest,pylint install to virt.env, pyside2 (button to add customer and shop), 
write to file json? or csv,read it..filesystem work
with pipenv, maybe boto3 and dynamodb and s3..maybe docker and bashscripts and terminal,fastapi)
'''
from human import Human


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
    answer_to_customer = shop1.buy_product('rohlik1', 10, customer_2)
    print(answer_to_customer)
