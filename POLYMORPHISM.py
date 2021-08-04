#parent Class User
class User:
    name = "Chris"
    email = "chriscavsf@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        enrty_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("welcome back, {}!".fomat(enrty_name))
        else:
            print("The password or email is incorrect.")

# Child class Employee
class Employee(User):
    base_pay = 11.00
    department = "general"
    fav_color = "blue"

# this is the same method in the parent class "User"
# the differnce is that, instead of using entry_password, we're using fav_color.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        enrty_email = input("Enter your email: ")
        fav_color = input("Enter your Favorite Color: ")
        if (entry_email == self.email and fav_color == self.fav_color):
            print("welcome back, {}!".fomat(enrty_name))
        else:
            print("Your favorite color or email is incorrect.")

# The following code invokes the methods inside each class for User and Employee.

customer = User()
customer.getLogininInfo()

manager = Employee()
manager.getLoginInfo()
