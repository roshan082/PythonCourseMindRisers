

order_products = []
product_cart = []

def showProducts():
    products = ["Pen", "Book", "Geomentry Box", "Copy", "Guess Papers", "Note Book"]
    return products

def orderProducts(cart):
    order_products.append(cart)
    return order_products

def cart(product):
    product_cart.append(product)
    return product_cart

def userList(user, password):
    user_list = ["roshansth11@gmail.com", "ram", "shikha"]
    password_list = ["roshan123", "ram123", "shikha123"]
    if user in user_list:
        # go to check password
        if password in password_list:
            return True
    else:
        return False

def userLogin():
    user = input("Enter your Email address: ")
    password = input("Enter your password: ")
    if userList(user, password):
        print("Logged In")
        userDashboard()
    else:
        print("Email and password incorrect..")
        userLogin()



def userDashboard():
    print("---------------------------------")
    print("View Product | Order Product | Add to cart | Cart ")
    mode = input("What do you want to do? | view | order | add | cart : ")
    if mode == "view":
        print(showProducts())
        userDashboard()
    elif mode == "order":
        print(showProducts())
        order_product = input("Enter a product name: ")
        if order_product in showProducts():
            print("Do you want to confirm your order? YES or NO")
            confirm_order = input("Enter YES or NO : ")
            if confirm_order == "YES":
                print("Order Successfull..")
                order_products.append(order_product)
                print(f"Your order products: {order_products}")
                userDashboard()
            else:
                print("Order Denied..")
                userDashboard()
        else:
            print("No product found.")
            userDashboard()
        # print(orderProducts(cart))
        # print("Here are your orders..")
    elif mode == "add":
        print(showProducts())
        print("What product do you want to add.")
        add_product = input("Enter a product name: ")
        if add_product in showProducts():
            print("Product is added to cart..")
            product_cart.append(add_product)
            userDashboard()
        else:
            print("No product found.")
            userDashboard()
    elif mode == "cart":
        print("Here are your product in the cart..")
        print(product_cart)
        # product = input("Select product : ")
        # print(cart(product))
        userDashboard()
    else:
        print("Select correct mode.")


userLogin()

# def showProduct():
