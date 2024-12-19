class BankAccount:
    """
    Attributes:
    - 
    Methods:
    - 
    """
    def __init__(self, holder, balance=0):
        self._balance = balance
        self.holder = holder
    
    def deposit(self, amount, source='unknown'):
        """
        
        """
        if amount > 0:            
            self._balance += amount
            print(f'Deposit of {amount} from {source}')
    
    def withdraw(self, amount, source='unknown'):
        """"
        
        """
        if amount > 0:            
            self._balance -= amount
            print(f'Withdraw of {amount} from {source}')
    
    def info(self):
        """
        
        """
        return self._balance, self.holder


b = BankAccount('Jan', 1000000) # BankAccount.__init__(b, 'Jan', 1000000)
b.deposit(50)
b.deposit(50)
b.deposit(50)
print(b.info())

b2 = BankAccount('Pietje', 500000)