class customer_order:
    def __init__(self, food, price):
        self.order_name = food
        self.order_price = price



if __name__ == '__main__':
    while True:
        print("1. Add item")
        print("2. Calculate Bill")
        choice = int(input("Enter your choice : "))

        if(int(choice) == 1):
            food = input("Enter food item : ")
            price = int(input("Enter Price : "))
            obj1 = customer_order(food, price)

        if int(choice) == 2:
            pass