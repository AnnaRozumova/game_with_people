from src.shop import Shop
from src.human import Human

def test_buy_product():
    customer_1 = Human(34, 'woman', 'Anna', 'Rozumova', 160, 'blond')
    shop1 = Shop('Albert', {'rohlik': {'price': 3, 'amount': 100}, 'chleba': {'price': 25, 'amount': 100}, 'ryze': {'price': 30, 'amount': 100}})
    test_return = shop1.buy_product('rohlik', 10, customer_1)
    expected_return = "For 10 of rohlik you will pay 30 korun"
    assert test_return == expected_return
