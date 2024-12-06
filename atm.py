class ATM:
    def __init__(self, balance = 100, pin = '1234'):
        self.balance = balance
        self.pin = pin
        self.max_attempts = 3
        self.attempts = 0
        self.is_authenticated = False
        self.is_account_active = True

    def insert_card(self):
        print('Card inserted!')
        self.authenticate()

    def authenticate(self):
        if not self.is_account_active:
            print('Account has been closed.')
            return
        
        while self.attempts < self.max_attempts:
            entered_pin = input('Enter your PIN: ')
            if entered_pin == self.pin:
                self.is_authenticated = True
                print('Authentication Successful.')
                self.select_transaction()
                return
            else:
                self.attempts += 1
                print(f'Incorrect PIN. Attempts left: {self.max_attempts - self.attempts}')
        
        if self.attempts >= self.max_attempts:
            self.reject_customer()

    def reject_customer(self):
        print('Too many incorrect attempts. Card blocked.')
        self.reset()

    def select_transaction(self):
        if not self.is_authenticated:
            print('Authentication required.')
            return

        print('1. Withdraw Money')
        print('2. Check Balance')
        choice = input('Select 1 or 2: ')

        if choice == '1':
            self.withdraw_money()
        elif choice == '2':
            self.check_balance()
        else:
            print('Invalid Choice!')
            self.select_transaction()

    def withdraw_money(self):      
        amount = float(input('Enter amount to withdraw: '))
        if amount <= self.balance:
            self.balance -= amount
            print(f'${amount} withdrawn. Remaining balance: ${self.balance}')
            if self.balance == 0:
                self.close_account()
                return
        else:
            print('Insufficient balance.')

        self.redo()

    def check_balance(self):
        print(f'Your balance is ${self.balance}.')
        self.redo()

    def close_account(self):
        print('Your balance is zero. Account closed.')
        self.is_account_active = False
        self.reset()

    def reset(self):
        self.is_authenticated = False
        self.attempts = 0
        print('Returning to idle state.\n')

    def redo(self):
        redo = True
        while redo == True:
            print('1. New Transaction')
            print('2. Exit')
            choice = input('Select 1 or 2: ')

            if choice == '1':
                redo = False
                self.select_transaction()
                return
            elif choice == '2':
                redo = False
                self.reset()
            else:
                print('Invalid Choice!')
    
# Program Start!!!
atm = ATM(pin='4321')
start = True
while start == True:
    card = input('Would you like to enter an ATM card? Yes or No:')
    if card.lower() == 'no':
        start = False
    elif card.lower() == 'yes':
        atm.insert_card()
    else:
        print('Please choose Yes or No!')