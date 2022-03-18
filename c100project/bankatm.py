class atm(object):
    def __init__(self,atmCardNumber, pinNumber):
        self.atmCardNumber = atmCardNumber,
        self.pinNumber = pinNumber
    def balance_enquiry(self):
        print("Your balance is $1000")
    def cash_withdrawl(self):
     print("Your cash has been withdrawn")

new_user = atm(123, 321)

print(new_user.balance_enquiry())