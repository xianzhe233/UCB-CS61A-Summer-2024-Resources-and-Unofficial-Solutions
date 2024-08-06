passphrase = 'REPLACE_THIS_WITH_PASSPHRASE'

def midsem_survey(p):
    """
    You do not need to understand this code.
    >>> midsem_survey(passphrase)
    'c20d4e5854c4c9cdfd14626aad39bd5a1e2ed9bb30dca56d5643a3ad'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


class Account:
    """An account has a balance and a holder.
    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25)  # 10 -> 10.2 -> 10.404
    2
    >>> a.balance                # Calling time_to_retire method should not change the balance
    10
    >>> a.time_to_retire(11)     # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        # balance * (1 + interest_rate) ^ n >= amount
        # n = log(base(1+interest_rate), amount/balance)
        from math import log, ceil
        return ceil(log((amount/self.balance), (1+self.interest)))



class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free. Still counts as a free withdrawal even though it was unsuccessful
    'Insufficient funds'
    >>> ch.withdraw(3)    # Second withdrawal is also free
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough, as free_withdrawals is only 2
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    "*** YOUR CODE HERE ***"
    def __init__(self, account_holder):
        super().__init__(account_holder)

    def withdraw(self, amount):
        if self.free_withdrawals:
            self.free_withdrawals -= 1
            return super().withdraw(amount)
        else:
            return super().withdraw(amount + self.withdraw_fee)


class Transaction:
    def __init__(self, id, before, after):
        self.id = id
        self.before = before
        self.after = after

    def changed(self):
        """Return whether the transaction resulted in a changed balance."""
        "*** YOUR CODE HERE ***"
        return self.before != self.after

    def report(self):
        """Return a string describing the transaction.

        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        msg = 'no change'
        if self.changed():
            "*** YOUR CODE HERE ***"
            if self.before > self.after:
                msg = f'decreased {self.before}->{self.after}'
            else:
                msg = f'increased {self.before}->{self.after}'
        else:
            msg = 'no change'
        return str(self.id) + ': ' + msg

class BankAccount:
    """A bank account that tracks its transaction history.

    >>> a = BankAccount('Eric')
    >>> a.deposit(100)    # Transaction 0 for a
    100
    >>> b = BankAccount('Erica')
    >>> a.withdraw(30)    # Transaction 1 for a
    70
    >>> a.deposit(10)     # Transaction 2 for a
    80
    >>> b.deposit(50)     # Transaction 0 for b
    50
    >>> b.withdraw(10)    # Transaction 1 for b
    40
    >>> a.withdraw(100)   # Transaction 3 for a
    'Insufficient funds'
    >>> len(a.transactions)
    4
    >>> len([t for t in a.transactions if t.changed()])
    3
    >>> for t in a.transactions:
    ...     print(t.report())
    0: increased 0->100
    1: decreased 100->70
    2: increased 70->80
    3: no change
    >>> b.withdraw(100)   # Transaction 2 for b
    'Insufficient funds'
    >>> b.withdraw(30)    # Transaction 3 for b
    10
    >>> for t in b.transactions:
    ...     print(t.report())
    0: increased 0->50
    1: decreased 50->40
    2: no change
    3: decreased 40->10
    """

    # *** YOU NEED TO MAKE CHANGES IN SEVERAL PLACES IN THIS CLASS ***
    transaction_idx = 0

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def transaction_decorator(f):
        def wrapper(self, amount):
            before = self.balance
            res = f(self, amount)
            after = self.balance
            self.transactions.append(Transaction(self.transaction_idx, before, after))
            self.transaction_idx += 1
            return res
        return wrapper

    @transaction_decorator
    def deposit(self, amount):
        """Increase the account balance by amount, add the deposit
        to the transaction history, and return the new balance.
        """
        self.balance = self.balance + amount
        return self.balance

    @transaction_decorator
    def withdraw(self, amount):
        """Decrease the account balance by amount, add the withdraw
        to the transaction history, and return the new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance




class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to.
            email is an instance of the Email class.
        """
        self.clients[email.recipient_name].inbox.append(email)

    def register_client(self, client):
        """Add a client to the clients mapping (which is a 
        dictionary from client names to client instances).
            client is an instance of the Client class.
        """
        self.clients[client.name] = client

class Client:
    """A client has a server, a name (str), and an inbox (list).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name
    'Alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self)

    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient."""
        email = Email(message, self, recipient_name)
        self.server.send(email)


def make_change(amount, coins):
    """Return a list of coins that sum to amount, preferring the smallest coins
    available and placing the smallest coins first in the returned list.

    The coins argument is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> make_change(2, {2: 1})
    [2]
    >>> make_change(2, {1: 2, 2: 1})
    [1, 1]
    >>> make_change(4, {1: 2, 2: 1})
    [1, 1, 2]
    >>> make_change(4, {2: 1}) == None
    True

    >>> coins = {2: 2, 3: 2, 4: 3, 5: 1}
    >>> make_change(4, coins)
    [2, 2]
    >>> make_change(8, coins)
    [2, 2, 4]
    >>> make_change(25, coins)
    [2, 3, 3, 4, 4, 4, 5]
    >>> coins[8] = 1
    >>> make_change(25, coins)
    [2, 2, 4, 4, 5, 8]
    """
    if not coins:
        return None
    smallest = min(coins)
    rest = remove_one(coins, smallest)
    if amount < smallest:
        return None
    "*** YOUR CODE HERE ***"
    if amount == smallest:
        return [smallest]
    used_change = make_change(amount-smallest, rest)
    unused_change = make_change(amount, rest)
    if used_change is None and unused_change is None:
        return None
    elif used_change is None:
        return unused_change
    else:
        return [smallest] + used_change

def remove_one(coins, coin):
    """Remove one coin from a dictionary of coins. Return a new dictionary,
    leaving the original dictionary coins unchanged.

    >>> coins = {2: 5, 3: 2, 6: 1}
    >>> remove_one(coins, 2) == {2: 4, 3: 2, 6: 1}
    True
    >>> remove_one(coins, 6) == {2: 5, 3: 2}
    True
    >>> coins == {2: 5, 3: 2, 6: 1} # Unchanged
    True
    """
    copy = dict(coins)
    count = copy.pop(coin) - 1  # The coin denomination is removed
    if count:
        copy[coin] = count      # The coin denomination is added back
    return copy

class ChangeMachine:
    """A change machine holds a certain number of coins, initially all pennies.
    The change method adds a single coin of some denomination X and returns a
    list of coins that sums to X. The machine prefers to return the smallest
    coins available. The total value in the machine never changes, and it can
    always make change for any coin (perhaps by returning the coin passed in).

    The coins attribute is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> m = ChangeMachine(2)
    >>> m.coins == {1: 2}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.coins == {2: 1}
    True
    >>> m.change(2)
    [2]
    >>> m.coins == {2: 1}
    True
    >>> m.change(3)
    [3]
    >>> m.coins == {2: 1}
    True

    >>> m = ChangeMachine(10) # 10 pennies
    >>> m.coins == {1: 10}
    True
    >>> m.change(5) # takes a nickel & returns 5 pennies
    [1, 1, 1, 1, 1]
    >>> m.coins == {1: 5, 5: 1} # 5 pennies & a nickel remain
    True
    >>> m.change(3)
    [1, 1, 1]
    >>> m.coins == {1: 2, 3: 1, 5: 1}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.change(2) # not enough 1's remaining; return a 2
    [2]
    >>> m.coins == {2: 1, 3: 1, 5: 1}
    True
    >>> m.change(8) # cannot use the 2 to make 8, so use 3 & 5
    [3, 5]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(1) # return the penny passed in (it's the smallest)
    [1]
    >>> m.change(9) # return the 9 passed in (no change possible)
    [9]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(10)
    [2, 8]
    >>> m.coins == {10: 1}
    True

    >>> m = ChangeMachine(9)
    >>> [m.change(k) for k in [2, 2, 3]]
    [[1, 1], [1, 1], [1, 1, 1]]
    >>> m.coins == {1: 2, 2: 2, 3: 1}
    True
    >>> m.change(5) # Prefers [1, 1, 3] to [1, 2, 2] (more pennies)
    [1, 1, 3]
    >>> m.change(7)
    [2, 5]
    >>> m.coins == {2: 1, 7: 1}
    True
    """
    def __init__(self, pennies):
        self.coins = {1: pennies}

    def change(self, coin):
        """Return change for coin, removing the result from self.coins."""
        "*** YOUR CODE HERE ***"
        def reducer(self, s):
            for coin in s:
                self.coins[coin] -= 1
                if self.coins[coin] == 0:
                    del self.coins[coin]
        
        def adder(self, coin):
            if coin not in self.coins:
                self.coins[coin] = 1
            else:
                self.coins[coin] += 1

        change_res = make_change(coin, self.coins)
        if not change_res:
            return [coin]
        else:
            reducer(self, change_res)
            adder(self, coin)
            return change_res