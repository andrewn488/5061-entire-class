"""Worksheet 14
Deep Dive into Classes
Need to learn how to do this.
11/13/2020
"""

# straight up hard coding everything

owner1 = 'Sally'
owner2 = 'Daphne'
number1 = 89023818181
number2 = 89023110107
balance1 = 9281.14
balance2 = 8148.99
transfer_amt = 1000.00

if balance1 >= transfer_amt:
    balance1 -= transfer_amt
    balance2 += transfer_amt
    print('transferred $%.2f from a/c %d (%s) to a/c %d (%s)' %
          (transfer_amt, number1, owner1, number2, owner2))

else:
    print('insufficient funds in a/c %d (%s) for transfer of $%.2f' %
          (number1, owner1, transfer_amt))


# put it into a function

def transfer(owner1, number1, balance1,
             owner2, number2, balance2, transfer_amt):
    if balance1 >= transfer_amt:
        balance1 -= transfer_amt
        balance2 += transfer_amt
        print('transferred $%.2f from a/c %d (%s) to a/c %d (%s)' %
              (transfer_amt, number1, owner1, number2, owner2))
    else:
        print('insufficient funds in a/c %d (%s) for transfer of $%.2f' %
              (number1, owner1, transfer_amt))

sally_bal, daphne_bal = 9281.14, 8148.99
transfer('Sally', 89023818181, sally_bal,
         'Daphne', 89023110107, daphne_bal, 1000.00)
print(sally_bal)    # BAD: no lasting effects to the account balances


# use a dictionary because it's mutable. previously, the balances didn't save changes

def transfer(ac1, ac2, transfer_amt):
    if ac1['balance'] >= transfer_amt:
        ac1['balance'] -= transfer_amt
        ac2['balance'] += transfer_amt
        print('transferred $%.2f from a/c %d (%s) to a/c %d (%s)' %
              (transfer_amt, ac1['number'],
               ac1['owner'], ac2['number'], ac2['owner']))
    else:
        print('insufficient funds in a/c %d (%s) for transfer of $%.2f' %
              (ac1['number'], ac1['owner'], transfer_amt))
sally = {'owner': 'Sally', 'number': 89023818181, 'balance': 9281.14}
daphne = {'owner': 'Daphne', 'number': 89023110107, 'balance': 8148.99}

transfer(sally, daphne, 1000.00)
print(sally['balance'])     # GOOD: correctly says 8281.14


# yes, this function works well now. But let's make a class to make it even better

class Account(object):
    def __init__(self, ac_owner, ac_number, initial_balance):
        self.owner = ac_owner
        self.number = ac_number
        self.balance = initial_balance

    def __str__(self):
        return 'a/c %d (%s)' % (self.number, self.owner)

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if self.balance < amt:
            raise ValueError('insufficient funds')
        self.balance -= amt

    def transfer(self, other_ac, amt):
        self.withdraw(amt)
        other_ac.deposit(amt)


sally = Account('Sally', 89023818181, 9281.14)
daphne = Account('Daphne', 89023110107, 8148.99)
amt = 1000.00

try:
    sally.transfer(daphne, amt)
    print('transferred $%.2f from %s to %s' % (amt, sally, daphne))
except ValueError:
    print('failed to transfer $%.2f from %s to %s'
          % (amt, sally, daphne))
print(sally.balance)    # GOOD: sally's balance is correct
