# 316539196
# 20

import copy


# Q4 - The class will include the following methods in addition to the constructor(see home exam for details)
# 1. add_product
# 2. add_to_customer
# 3. pay_bill
# 4. people_in_store
class GroceryStore(object):
    # Abstract class for a GroceryStore.
    def __init__(self):
        self.d_inventory = {}  # dict of the Stores Products. (can't be static - relative to a Stores Object.)
        self.d_customers = {}  # dict of the Stores Customers. (can't be static - relative to a Stores Object.)

    def add_product(self, p_name_id, p_amount, p_price):
        """
        This method adds a product to an inventory bank of the store.
        Args:
            p_name_id (): one-by-one id for a product.
            p_amount (): product units amount.
            p_price (): product's price.

        Returns:
            Boolean. if the process was successful.
        """
        name_product = str.lower(p_name_id)
        if name_product not in self.d_inventory.keys():
            self.d_inventory[name_product] = Product(name_product, p_amount, p_price)
            return True
        else:
            return False

    def add_to_customer(self, p_name_id, c_customer_id):
        """
         This method adds a product for a customer.
        Args:
            p_name_id (): one-by-one id for a product.
            c_customer_id (): one-by-one id for a customer.

        Returns:
            Boolean. if the process was successful.
        """
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
        """
        This method implements a customer payment process.
        Args:
            c_customer_id (): one-by-one id for a customer.
            customer_payment (): the monet the customer gave to pay with.

        Returns:
            excess
        """
        sum_shopping_cart = self.d_customers[c_customer_id].calc_sc_products_price()
        excess = customer_payment - sum_shopping_cart
        del self.d_customers[c_customer_id]
        return excess

    def people_in_store(self):
        """
            This method Calc and returns the amount of people i the store.
        Returns:
            Int, the amount of people.
        """
        return len(self.d_customers.keys())

    def update_inventory(self, p_name_id):
        """
         Updates the inventory of the shop.
         A customer took a product, the inventory.product amount+=-1
         In case the product amount is 0, the product gets delete from the inventory.
        Args:
            p_name_id (): one-by-one id for a product.

        Returns:
            nothing. only print - as logger.
        """
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
    # Abstract class for a Product.
    def __init__(self, name_id, amount, price):
        """
            Constractor for a new Product in our Grocery Store.
        Args:
            name_id ():  <String> name of the product. (one-to-one variable)
            amount (): <Int> the amount of units from a given product in the store.
            price (): <Flout> the price of the product.
        """
        self.name_id = name_id
        self.amount = amount
        ''' 
            I can create another level of abstraction and create a List of products,
            and use the amount as the lists length. But it will create alot of design problems. 
            Each customer will have a list of lists of products, And each product will need to be represented as
            a list of itself times the amount. 
            On one hand, this design isn't saving in memory. But the other design will create an OOP Complexity, 
            which will drive us far from the simplicity of the question.
        '''
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
    # Abstract class for a Customer.
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
        """
            Calcs shopping cart products prices.
        Returns:
            p_price_sum.
        """
        p_price_sum = 0
        for p_name_id in self.shopping_cart.keys():
            p_price_sum += (self.shopping_cart[p_name_id].get_price() *
                            self.shopping_cart[p_name_id].get_amount())
            '''Another time, I see how I can put here a list to replace
             the amount variable and create a for by for, loop design instead.'''
        return p_price_sum

    def add_product_to_shopping_cart(self, p_product):

        if p_product.get_name_id() in self.shopping_cart.keys():
            self.update_shopping_cart(p_product.get_name_id(), 1)
        else:
            self.shopping_cart[p_product.get_name_id()] = Product(p_product.get_name_id(), 1, p_product.get_price())
            ''' creating multiplication of objects. If the inventory was managed as a dictionary of 
                lists of products so I would just move objects between lists and wouldn't have to create another 
                object for the shopping cart of each customer. I HOPE that by describing my design thoughts and ideas,  
                and why its good and why its bad to implement them, i showed my OOP understanding.'''

    def update_shopping_cart(self, p_name_id, p_amount):
        self.shopping_cart[p_name_id].update_amount(p_amount)