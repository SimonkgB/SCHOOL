# multiple accounts in one
# catigorizing payments
# loans
# currency transfer and exhange, real time
# split up the payment into diffrent accounts

class Bank:
    def __init__(self, account_number, account_holder_name):
        self.n = account_number
        self.a = account_holder_name

    def login(self):
        if self.a in Users and self.n == Users[self.a][0]:
            return "Access granted"
        else:
            return "Incorrect username or password"


class Youruser(Bank):
    def __init__(self):
        super().__init__(account_number, account_holder_name)
        self.i = Users[account_holder_name][1]

    def deposit(self):
        amount = int(input("How much do you want to deposit: "))
        return f"You now have {self.i + amount}kr in your account"

    def withdraw(self):
        amount = int(input("How much do you want to withdraw: "))
        if self.i >= amount:
            return f"You now have {self.i - amount}kr in your account"
        else:
            print("Insufficient balance")

    def get_balance(self):
        return f"You have {self.i}kr in your account"

    def send(self):
 
        reciver = str(input("who are you sending to: "))
        self.rec = Users[reciver][1]
        sending_amount= float(input("How much are you sending: "))
        if self.i-sending_amount<0:
            return f"get rich bitch"
        else:
            if reciver in Users:
                new_value = (Users[reciver][0], self.rec+sending_amount)
                Users[reciver] = new_value
                return f"{self.a} har nå {self.i - sending_amount}kr, {reciver} har fått pengene"
            else:
                return "this is not a user"


Users = {"Joe_Doe" : (11111, 1100),
         "Ola_Kar" : (22222, 200),
         "Per_Ser" : (33333, 10000)
         }


account_holder_name = input("Username: ")
account_number = int(input("Account number: "))


bank = Bank(account_number, account_holder_name)


if bank.login() == "Access granted":
    user = Youruser()
    do = input("What do you want to do? Enter a number (1. Deposit, 2. Withdraw, 3. Get Balance, 4. Send): ")
else:
    print(bank.login())
    quit()


user_actions = {
    "1": user.deposit,
    "2": user.withdraw,
    "3": user.get_balance,
    "4": user.send
}

if do in user_actions:
    result = user_actions[do]()
    print(result)
else:
    print("Invalid input. Please enter a valid number.")