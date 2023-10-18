class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          return f"Deposited ${amount}. New balance is ${self.__account_balance}."
      else:
          return "Invalid deposit amount."

  def withdraw(self, amount):
      if amount > 0 and amount <= self.__account_balance:
          self.__account_balance -= amount
          return f"Withdrew ${amount}. New balance is ${self.__account_balance}."
      elif amount > self.__account_balance:
          return "Insufficient funds."
      else:
          return "Invalid withdrawal amount."

  def display_balance(self):
      return f"Account balance for {self.__account_holder_name}'s account ({self.__account_number}) is ${self.__account_balance}."

# Testing the BankAccount class
if __name__ == "__main__":
  # Create an instance of the BankAccount class
  account1 = BankAccount("123456", "John Doe", 1000.0)

  # Test deposit and withdrawal
  print(account1.display_balance())  # Display initial balance
  print(account1.deposit(500))      # Deposit $500
  print(account1.withdraw(200))     # Withdraw $200
  print(account1.display_balance())  # Display updated balance
  print(account1.withdraw(2000))    # Attempt to withdraw $2000 (insufficient funds)
