from dataclasses import dataclass

@dataclass
class BankAccount:
    firstname: str
    lastname: str
    account_number: int = 0
    # Note: an integer balance in pennies would be better to avoid rounding errors
    balance: float = 0.0
    interest_rate: float = 0.0

my_bank_account = BankAccount("Julie", "Smertna", 71325499)

my_bank_account.balance += float(input("Enter a deposit in pounds: "))
my_bank_account.balance -= float(input("Enter a withdrawal in pounds: "))

print(f"Your current balance is £{my_bank_account.balance:.2f}")
