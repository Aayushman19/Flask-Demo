class customer_order:
    def __init__(self):
        self.order_name = None
        self.order_price = None



if __name__ == '__main__':
    while True:
        counter = 1
        print(counter + ". Add item")
        counter += 1
        print(counter + ". Calculate Bill")
        choice = input("Enter your item")
        n = int(input())

        if(int(choice) == 1):
            food = input("Enter food item")
            obj1 = customer_order(food)

        if int(choice) == 2:
            pass