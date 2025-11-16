
from __future__ import annotations

class BankAccount:

	def __init__(self, owner: str, starting_balance: float = 0.0) -> None:
		self.owner = owner
		self.__balance = float(starting_balance)

	@property
	def balance(self) -> float:
		"""Return the current account balance (read-only)."""
		return self.__balance

	def deposit(self, amount: float) -> None:
		"""Deposit a positive `amount` into the account.

		Raises `ValueError` if `amount` is not positive.
		"""
		amount = float(amount)
		if amount <= 0:
			raise ValueError("Deposit amount must be positive")
		self.__balance += amount

	def withdraw(self, amount: float) -> None:
		"""Withdraw a positive `amount` from the account.

		Raises `ValueError` for non-positive amounts or insufficient funds.
		"""
		amount = float(amount)
		if amount <= 0:
			raise ValueError("Withdrawal amount must be positive")
		if amount > self.__balance:
			raise ValueError("Insufficient funds")
		self.__balance -= amount

	def __repr__(self) -> str:
		return f"BankAccount(owner={self.owner!r}, balance={self.__balance:.2f})"


def _demo() -> None:
	acc = BankAccount("Alice", 50)
	print(acc)
	print("Initial balance:", acc.balance)

	acc.deposit(100)
	print("After depositing 100:", acc.balance)

	try:
		acc.withdraw(30)
		print("After withdrawing 30:", acc.balance)
	except ValueError as exc:
		print("Withdraw failed:", exc)

	try:
		acc.withdraw(1000)
	except ValueError as exc:
		print("Expected failure (insufficient funds):", exc)

	try:
		acc.deposit(-20)
	except ValueError as exc:
		print("Expected failure (invalid deposit):", exc)

	# Attempt to modify the "private" attribute directly creates a new attribute
	acc.__balance = 9999
	print("After setting acc.__balance = 9999 (creates new attribute):")
	print("acc.__balance attribute exists on instance:", hasattr(acc, "__balance"))
	print("Actual balance property still:", acc.balance)

	# Show name-mangled private attribute (discouraged to access directly)
	print("(Discouraged) Accessing name-mangled attribute:", getattr(acc, "_BankAccount__balance"))


if __name__ == "__main__":
	_demo()
