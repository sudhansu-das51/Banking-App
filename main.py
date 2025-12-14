class BankAccount:
  
  # initialize account with pin and history
  def __init__(self, name, pin, balance=0):
    self.name = name
    self.pin = pin
    self.balance = balance
    self.history = []

  # deposit money 
  def deposit(self, amount):
    self.balance += amount
    self.history.append(f"Deposited ${amount}")
    print(f"${amount} deposited! New balance: ${self.balance}")

  # withdraw money
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount  
      self.history.append(f"Withdrew ${amount}")
      print(f"${amount} withdrawn! New balance: ${self.balance}")
    else:
      print("Insufficient balance!")   

  # show balance
  def show_balance(self):   
    print(f"Account Holder: {self.name}, Balance: ${self.balance}")   

  # show transaction history
  def show_history(self):
    print("\n***** Transaction History *****")
    if not self.history:
      print("No transactions yet!")
    else:
      for t in self.history:
        print(t)


# ---------------- MAIN PROGRAM ----------------     

name = input("Enter your name: ")
pin = input("Set a 4-digit PIN: ")
account = BankAccount(name, pin)

# ask pin before access
if input("Enter PIN to login: ") != account.pin:
  print("Wrong PIN! Access Denied.")
  exit()

while True:
  print("\n1. Deposit  2. Withdraw  3. Show Balance  4. History  5. Exit")
  choice = input("Choose: ")

  if choice == "1":
    account.deposit(int(input("Enter amount: ")))
  elif choice == "2":
    account.withdraw(int(input("Enter amount: ")))
  elif choice == "3":
    account.show_balance()
  elif choice == "4":
    account.show_history()
  elif choice == "5":
    print("Goodbye!")
    break
  else:
    print("Invalid choice!")
