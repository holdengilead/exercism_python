"""
https://exercism.org/tracks/python/exercises/bank-account
"""
import threading


class BankAccount:
    """
    Bank acccount with support for concurrents deposits and withdrawals
    """

    def __init__(self) -> None:
        self._balance: int = 0
        self._active: bool = False
        self._mutex = threading.Lock()

    def get_balance(self) -> int:
        """
        Returns the balance of the account.
        """
        if not self._active:
            raise ValueError("account not open")
        return self._balance

    def open(self) -> None:
        """
        The account becomes active.
        """
        if self._active:
            raise ValueError("account already open")
        self._active = True

    def deposit(self, amount: int) -> None:
        """
        Put money in the account.
        """
        if not self._active:
            raise ValueError("account not open")
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        with self._mutex:
            self._balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Retrieve money from the account.
        """
        if not self._active:
            raise ValueError("account not open")
        if self._balance < amount:
            raise ValueError("amount must be less than balance")
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        with self._mutex:
            self._balance -= amount

    def close(self) -> None:
        """
        The account becomes closed.
        """
        if not self._active:
            raise ValueError("account not open")
        self._active = False
        self._balance = 0
