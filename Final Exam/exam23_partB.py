# 316539196
# 20

import copy


# Q4 - The class will include the following methods in addition to the constructor(see home exam for details)
# 1. add_product
# 2. add_to_costumer
# 3. pay_bill
# 4. people_in_store
class GroceryStore(object):

    def __init__(self):
        self.d_inventory= {} # dict of the Stores Products. (can't be static - relative to a Stores Object.)
        self.d_customers = {} # dict of the Stores Customers. (can't be static - relative to a Stores Object.)

    def add_product(self, p_name_id, p_amount, p_price):

        name_product = str.lower(p_name_id)
        if name_product not in self.d_inventory.keys():
            self.d_inventory[name_product] = Product(name_product, p_amount, p_price)
            return True
        else:
            return False

    def add_to_costumer(self, p_name_id, c_customer_id):

        name_product = str.lower(p_name_id)
        if name_product in self.d_inventory.keys():
            """It makes sense that their will not be a customer for a non existing product,
            that's why we will create a costumer only when we know that the products, he\she wants to buy, exists."""

            if c_customer_id not in self.d_customers.keys():
                customer = Customer(c_customer_id)
            else:
                customer = self.d_customers[c_customer_id]

            customer.add_product_to_shopping_cart(copy.deepcopy(self.d_inventory[name_product]))

            self.update_customers_status(c_customer_id, customer)
            self.update_inventory(name_product)
            return True
        else:
            return False

    def pay_bill(self, c_customer_id, customer_payment):
        sum_shopping_cart = self.d_customers[c_customer_id].calc_sc_products_price()
        excess = customer_payment - sum_shopping_cart
        del self.d_customers[c_customer_id]
        return excess

    def people_in_store(self):
        return len(self.d_customers.keys())

    def update_inventory(self, p_name_id):
        p_amount = self.d_inventory[p_name_id].get_amount()
        if p_amount > 0:
            p_amount = self.d_inventory[p_name_id].update_amount(-1)
        if p_amount == 0:
            del self.d_inventory[p_name_id]
            print(p_name_id, " is out of stock!")

    def update_customers_status(self, customer_id, customer):
        if customer_id not in self.d_customers.keys():
            self.d_customers[customer_id] = customer
        else:
            print("Asaf you have a Bug in update_customers_status.")

class Product(object):

    def __init__(self, name_id, amount, price):
        """
            Constractor for a new Product in our Grocery Store.
        Args:
            name_id ():  <String> name of the product. (one-to-one variable)
            amount (): <Int> the amount of units from a given product in the store.
            price (): <Flout> the price of the product.
        """
        self.name_id = name_id
        self.amount = amount     # I can create another level of abstraction and create a List of products,
                                 # and not use the amount like this.
        self.price = price

    def get_name_id(self):
        return self.name_id

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

    def update_amount(self, new_amount):
        self.amount += new_amount
        return self.amount



class Customer(object):
    def __init__(self, customer_id):
        """
            Constractor for a Customer in the Grocery Store.
            a customer is created only if he has put a product in his Shopping Cart.
            a customer is counted "exit" only if he has an open Shopping Cart in our Store.
            There cant be a customer without a shopping_cart. [Correct Logically and Design wise].
        Args:
            customer_id (): <Int> number of a customer. (one-to-one variable)
            [Quicker for searching to define as int and not string].
            shopping_cart (): List<Products> the customers shopping cart - a list of products.
        """
        self.customer_id = customer_id
        self.shopping_cart = {}

    def get_customer_id(self):
        return self.customer_id

    def get_shopping_cart(self):
        return self.shopping_cart

    def calc_sc_products_price(self):
        p_price_sum = 0
        for p_name_id in self.shopping_cart.keys():
            p_price_sum += (self.shopping_cart[p_name_id].get_price() *
                            self.shopping_cart[p_name_id].get_amount())
            '''Another time I see how I can put here a list to replace
             the amount variable and create for loop instead.'''
        return p_price_sum


    def add_product_to_shopping_cart(self, p_product):

        if p_product.get_name_id() in self.shopping_cart.keys():
            self.update_shopping_cart(p_product.get_name_id(), 1)
        else:
            self.shopping_cart[p_product.get_name_id()] = Product(p_product.get_name_id(), 1, p_product.get_price())
            ''' creating multiplication of objects, if the inventory was managed as a list of 
                objects so I would just move objects between lists and not create another 
                object doe the shopping cart of each customer. '''


    def update_shopping_cart(self, p_name_id, p_amount):
        self.shopping_cart[p_name_id].update_amount(p_amount)

if __name__ == "__main__":
    g = GroceryStore()

    assert (g.add_product("milk", 3, 10)) == True
    assert (g.add_product("bread", 1, 20)) == True
    assert (g.add_product("MIlK", 3, 10)) == False
    assert (g.add_product("milk", 1, 10)) == False
    assert (g.add_to_costumer("cheese", 111)) == False
    assert (g.add_to_costumer("milk", 111)) == True
    assert (g.add_to_costumer("MILK", 111)) == True
    assert (g.add_to_costumer("bread", 111)) == True
    assert (g.add_to_costumer("milk", 112)) == True
    assert (g.add_to_costumer("bread", 112)) == False
    assert (g.add_to_costumer("milk", 111)) == False
    assert (g.people_in_store()) == 2
    assert (g.pay_bill(112, 10.5)) == 0.5
    assert (g.people_in_store()) == 1
    assert (g.pay_bill(111, 60)) == 20
    assert (g.people_in_store()) == 0

    assert (g.add_product("bread", 1, 20)) == True
    assert (g.add_product("milk", 1, 10)) == True
    assert (g.add_to_costumer("bread", 111)) == True
    assert (g.add_to_costumer("bread", 112)) == False
    assert (g.people_in_store()) == 1
    assert (g.add_product("bread", 1, 20)) == True
    assert (g.add_to_costumer("bread", 111)) == True
    assert (g.pay_bill(111, 40)) == 0

    assert (g.add_product("Apple", 1, 5)) == True
    assert (g.add_product("Banana", 10, 8)) == True
    assert (g.add_to_costumer("apple", 123456789)) == True
    assert (g.add_to_costumer("Cheese", 123456789)) == False
    assert (g.add_to_costumer("Apple", 12336)) == False
    assert (g.people_in_store()) == 1
    assert (g.add_product("Apple", 1, 70)) == True
    assert (g.add_to_costumer("Apple", 12336)) == True
    assert (g.people_in_store()) == 2
    assert (g.pay_bill(123456789, 20)) == 15
    assert (g.pay_bill(12336, 80)) == 10
    assert (g.people_in_store()) == 0

    print("Question 4 passed all tests!")
