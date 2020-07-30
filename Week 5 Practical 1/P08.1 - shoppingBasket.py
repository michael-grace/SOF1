#***Shopping Basket***

the_stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}
prices = {
 "banana": 40,
 "apple": 20,
 "orange": 15,
 "pear": 30
}
basket_1 = {
 "banana": 4,
 "pear": 3
}
basket_2 = {
 "apple": 1,
 "pear": 3
}

def basket_price(basket, stock, prices):
    total_price = 0
    for key in basket:
        if basket[key] > stock[key]:
            return -1
        else:
            total_price += basket[key]*prices[key]
    return total_price

def checkout(basket, stock, prices):
    price = basket_price(basket, stock, prices)
    if  price != -1:
        for key in basket:
            global the_stock
            the_stock[key] -= basket[key]
    return price

def add_stock(items, stock):
    for key in items:
        if key in stock.keys():
            stock[key] += items[key]
        else:
            stock[key] = items[key]
    print(stock)

def price_increase(increase, prices):
    for key in prices:
        prices[key] *= (1+increase)
        prices[key] = round(prices[key])
    return prices

print(basket_price(basket_1, the_stock, prices))
print(basket_price(basket_2, the_stock, prices))

print(the_stock)
print(checkout(basket_1, the_stock, prices))
print(the_stock)

#Reset the Stock
the_stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

print(the_stock)
print(checkout(basket_2, the_stock, prices))
print(the_stock)

add_stock({"apple":5, "kiwi":10}, the_stock)

print(price_increase(0.2, prices))