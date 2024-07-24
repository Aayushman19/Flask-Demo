class customer_order:
    amt = 0
    def __init__(self, food, price):
        self.order_name = food
        self.order_price = price
    
    def add(price):
        amt += price

    def get_amt(amt):
        return amt

class total_bill:
    def __init__(self, amount, discount):
        self.discount = discount
        self.amount = amount

    def calculate(discount, amount):
        dis = (discount/amount)*100
        amount -= dis
        print("Final Bill : ", amount)

if __name__ == '__main__':
    while True:
        print("1. Add item")
        print("2. Calculate Bill")
        choice = int(input("Enter your choice : "))

        if(int(choice) == 1):
            food = input("Enter food item : ")
            price = int(input("Enter Price : "))
            obj1 = customer_order(food, price)

        if(int(choice) == 2):
            amt = obj1.get_amt()
            dis = 15
            obj2 = total_bill(amt, dis)
            obj2.calculate(amt, dis)