"""Account class - revisit this..."""


class Account(object):
    """Account class (revisited from Worksheet 14).
    This one has a __repr__ method, too.
    It also returns the object's balance from most methods for convenience.
    """
    count = 0
    division = 'NA'
    branch = 38

    def __init__(self, owner, initial_balance=0.0):
        """Construct an Account object for the given owner, given number,
        and initial balance, in US Dollars (defaults to $0.00).
        """
        Account.count += 1
        self.owner = owner
        self.account_number = '%sXY-%s-%08d' % (Account.division,
                                                Account.branch, Account.count)
        self.balance = initial_balance

    def __str__(self):
        """Returns a string that is suitable for a client to identify
        this object.
        """
        return 'a/c %s (%s)' % (self.account_number, self.owner)

    def __repr__(self):
        return "Account('%s', %f)" % (self.owner, self.balance)

    def __eq__(self, other):
        return self.owner == other.owner and self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self < other or self.balance == other.balance

    def deposit(self, amount):
        """Add amount, in US Dollars, to this account"""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Subtract given amount, in US Dollars, from this account.
        Raises ValueError if there are insufficient funds in this account
        to make the withdrawal.
        """
        if amount > self.balance:
            raise ValueError('insufficient funds to withdraw $%.2f' % amount)
        self.balance -= amount
        return self.balance

    def transfer(self, transferee, transfer_amount):
        """Withdraw the transfer amount from this account and deposit it in the
        transferee account.
        Raises ValueError if there are insufficient funds in this account
        to make the transfer.
        """
        self.withdraw(transfer_amount)
        transferee.deposit(transfer_amount)
        return self.balance

