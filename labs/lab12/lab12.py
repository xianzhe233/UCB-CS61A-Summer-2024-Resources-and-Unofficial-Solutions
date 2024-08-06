from tree import *

def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assume that
     nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    "*** YOUR CODE HERE ***"
    return [[item] + e for e in nested_list]

def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if len(s) == 0:
        return [[]]
    else:
        sub_s = subseqs(s[1:])
        return sub_s + insert_into_all(s[0], sub_s)

def non_decrease_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = non_decrease_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0])
            b = subseq_helper(s[1:], prev)
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, -float('inf'))


def num_trees(n):
    """Returns the number of unique full binary trees with exactly n leaves. E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    if n == 1:
        return 1
    cnt = 0
    for i in range(1, n):
        cnt += num_trees(i) * num_trees(n - i)
    return cnt


def partition_gen(n):
    """
    >>> partitions = [sorted(p) for p in partition_gen(4)]
    >>> for partition in sorted(partitions): # note: order doesn't matter
    ...     print(partition)
    [1, 1, 1, 1]
    [1, 1, 2]
    [1, 3]
    [2, 2]
    [4]
    """
    def yield_helper(num, segment):
        if num == 0:
            yield []
        elif num > 0:
            for i in range(1, segment + 1):
                for small_part in yield_helper(num - i, i):
                    yield [i] + small_part

    yield from yield_helper(n, n)


class CucumberGame:
    """Play a round and return all winners so far. Cards is a list of pairs.
    Each (who, card) pair in cards indicates who plays and what card they play.
    >>> g = CucumberGame()
    >>> g.play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    >>> g.winners
    [1]
    >>> g.play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It is not your turn, player 3
    It is not your turn, player 0
    The round is over, player 1
    >>> g.winners
    [1, 3]
    >>> g.play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed
    It is not your turn, player 2
    >>> g.winners
    [1, 3]
    """
    def __init__(self):
        self.winners = []
        
    def play_round(self, starter, cards):
        r = Round(starter)
        for who, card in cards:
            try:
                r.play(who, card)
            except AssertionError as e:
                print(e)
        if r.winner != None:
            self.winners.append(r.winner)


class Round:
    players = 4

    def __init__(self, starter):
        self.starter = starter
        self.next_player = starter
        self.highest = -1
        self.temp_winner = None
        self.winner = None
        self.count = 0

    def play(self, who, card):
        assert not self.is_complete(), f'The round is over, player {who}'
        assert who == self.next_player, f'It is not your turn, player {who}'
        self.next_player = (who + 1) % 4
        self.count += 1
        # print("DEBUG:", self.count)
        if card >= self.highest:
            self.highest = card
            self.temp_winner = who
        if self.is_complete():
            self.winner = self.temp_winner
            return

    def is_complete(self):
        """ Checks if a game could end. """
        return self.count >= 4

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    empty_tips = 'Nothing left to vend. Please restock.'

    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0

    def vend(self):
        if self.stock == 0:
            return VendingMachine.empty_tips
        elif self.balance < self.price:
            return f'Please add ${self.price - self.balance} more funds.'
        else:
            self.stock -= 1
            if self.balance == self.price:
                self.balance = 0
                return f'Here is your {self.product}.'
            else:
                change = self.balance - self.price
                self.balance = 0
                return f'Here is your {self.product} and ${change} change.'
            
    def add_funds(self, money):
        if self.stock == 0:
            return VendingMachine.empty_tips + ' ' + f'Here is your ${money}.'
        else:
            self.balance += money
            return f'Current balance: ${self.balance}'
        
    def restock(self, amount):
        self.stock += amount
        return f'Current {self.product} stock: {self.stock}'

class MissManners:
    """A container class that only forwards messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'Please add $10 more funds.'
    >>> m.ask('please add_funds', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('add_funds', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please add_funds', 10)
    'Thanks for asking, but I know not how to add_funds.'
    >>> double_fussy.ask('please please add_funds', 10)
    'Thanks for asking, but I know not how to please add_funds.'
    >>> double_fussy.ask('please ask', 'please add_funds', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        "*** YOUR CODE HERE ***"
        real_msg = message[7:]
        if not hasattr(self.obj, real_msg):
            return f'Thanks for asking, but I know not how to {real_msg}.'
        else:
            return getattr(self.obj, real_msg)(*args)
                

def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    >>> d = [1, 1]
    >>> e = [2]
    >>> trade(d, e)
    'Deal!'
    >>> d
    [2]
    >>> e
    [1, 1]
    """
    m, n = 1, 1

    equal_prefix = lambda: sum(first[:n]) == sum(second[:m])
    while not equal_prefix() and n <= len(first) and m <= len(second):
        # print("DEBUG:", first[:n], second[:m])
        if sum(first[:n]) > sum(second[:m]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:n], second[:m] = second[:m], first[:n]
        return 'Deal!'
    else:
        return 'No deal!'


def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['H', 'D', 'S', 'C']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    >>> cards[26:30]
    ['7S', '7C', '8H', '8D']
    >>> shuffle(cards)[:12]
    ['AH', '7S', 'AD', '7C', 'AS', '8H', 'AC', '8D', '2H', '8S', '2D', '8C']
    >>> shuffle(shuffle(cards))[:12]
    ['AH', '4D', '7S', '10C', 'AD', '4S', '7C', 'JH', 'AS', '4C', '8H', 'JD']
    >>> cards[:12]  # Should not be changed
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    half = cards[len(cards)//2:]
    shuffled = []
    for i in range(len(cards)//2):
        shuffled.append(cards[i])
        shuffled.append(half[i])
    return shuffled


def link_pop(lnk, index=-1):
    '''Implement the pop method for a Linked List.
    
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> removed = link_pop(lnk)
    >>> print(removed)
    5
    >>> print(lnk)
    <1 2 3 4>
    >>> link_pop(lnk, 2)
    3
    >>> print(lnk)
    <1 2 4>
    >>> link_pop(lnk)
    4
    >>> link_pop(lnk)
    2
    >>> print(lnk)
    <1>
    '''
    if index == -1:
        while lnk.rest.rest is not Link.empty:
            lnk = lnk.rest
        removed = lnk.rest.first
        lnk.rest = Link.empty
    else:
        while index != 1 and lnk.rest is not Link.empty:
            lnk = lnk.rest
            index -= 1
        removed = lnk.rest.first
        lnk.rest = lnk.rest.rest
    return removed
        


def deep_len(lnk):
    """ Returns the deep length of a possibly deep linked list.

    >>> deep_len(Link(1, Link(2, Link(3))))
    3
    >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
    4
    >>> levels = Link(Link(Link(1, Link(2)), \
            Link(3)), Link(Link(4), Link(5)))
    >>> print(levels)
    <<<1 2> 3> <4> 5>
    >>> deep_len(levels)
    5
    """
    if lnk is Link.empty:
        return 0
    elif isinstance(lnk, int):
        return 1
    else:
        return deep_len(lnk.first) + deep_len(lnk.rest)


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    def step(lnk, idx):
        if lnk is Link.empty:
            return
        step(lnk.rest, idx+1)
        if idx % 2 == 0 and lnk.rest is not Link.empty:
            lnk.rest = lnk.rest.rest

    step(s, 0)

def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth)
    level have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def reverse_tree(t, idx):
        if t.is_leaf():
            return
        for b in t.branches:
            reverse_tree(b, idx+1)
        if idx % 2 == 0:
            label_list = reversed([b.label for b in t.branches])
            for b in t.branches:
                b.label = next(label_list)
    
    reverse_tree(t, 0)


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def count_partitions(n, m):
    """Counts the number of partitions of a positive integer n, 
    using parts up to size m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

def is_palindrome(s):
    """Return whether a list of numbers s is a palindrome."""
    return all([s[i] == s[len(s) - i - 1] for i in range(len(s))])

def binary_search(lst, n):
    """Takes in a sorted list lst and returns the index where integer n
    is contained in lst. Returns -1 if n does not exist in lst."""
    low = 0
    high = len(lst)
    while low <= high:
        middle = (low + high) // 2
        if lst[middle] == n:
            return middle
        elif n < lst[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1