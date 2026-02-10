"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class BankAccount:
    def __init__(self,owner,pin):
        self.owner = owner
        self.balance = 0
        self.__pin = pin #En Python, usar doble guion bajo __ hace que el atributo sea privado, nadie puede verlo desde fuera fácilmente).
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount,pin_input):
        if pin_input != self.__pin:
            return "PIN INCORRECTO"
        if amount > self.balance:
            return "FONDOS_INSUFICIENTES"
        self.balance -= amount
        return self.balance
    
    def get_balance(self,pin_input):
        if pin_input == self.__pin:
            return self.balance
        else:
            None