class Bank:
    accountType="Business account"
    def __init__(self,accountBalance,accountNumber,accountName):
        self.accountBalance=accountBalance
        self.accountNumber=accountNumber
        self.accountName=accountName
    def withdraw(self):   
        return f"Hello your balance is {self.accountBalance}, your accountNumber is{self.accountNumber},your accountName is {self.accountName}"
       

