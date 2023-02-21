"""
https://exercism.org/tracks/python/exercises/rest-api
"""
from __future__ import annotations

import json
from typing import Iterable, Optional, TypedDict


class Lend(TypedDict):
    """
    Type for dict Lend.
    """

    lender: str
    borrower: str
    amount: float


class Database(TypedDict):
    """
    Type for dict Database.
    """

    users: list[UserDict]


class UserDict(TypedDict):
    """
    Tyepe for dict User.<
    """

    name: str
    balance: float
    owes: dict[str, float]
    owed_by: dict[str, float]


class User:
    """
    User of a IOU system. Track IOUs from other users.
    """

    def __init__(
        self,
        name: str,
        owes: Optional[dict[str, float]] = None,
        owed_by: Optional[dict[str, float]] = None,
        balance: float = 0.0,
    ) -> None:
        self.name = name
        if owes:
            self.owes = owes
        else:
            self.owes = {}
        if owed_by:
            self.owed_by = owed_by
        else:
            self.owed_by = {}
        self.balance = balance

    def __json__(self) -> UserDict:
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance,
        }

    def send_money(self, lend: Lend) -> None:
        """
        Register a lend to another user.
        """
        amount = lend["amount"]
        borrower = lend["borrower"]
        self.balance += amount
        if borrower in self.owes:
            adjust = self.owes[borrower] - amount
            if adjust > 0:
                self.owes[borrower] = adjust
            elif adjust == 0:
                del self.owes[borrower]
            else:
                del self.owes[borrower]
                self.owed_by[borrower] = abs(adjust)
        else:
            self.owed_by[borrower] = amount

    def receive_money(self, lend: Lend) -> None:
        """
        Register a lend from another user.
        """
        amount = lend["amount"]
        lender = lend["lender"]
        self.balance -= amount
        if lender in self.owed_by:
            adjust = self.owed_by[lender] - amount
            if adjust > 0:
                self.owed_by[lender] = adjust
            elif adjust == 0:
                del self.owed_by[lender]
            else:
                del self.owed_by[lender]
                self.owes[lender] = abs(adjust)
        else:
            self.owes[lender] = amount


class RestAPI:
    """
    RESTful API for tracking IOUs.
    """

    def __init__(self, database: Database) -> None:
        self.database: dict[str, User] = {
            user["name"]: User(**user) for user in database["users"]
        }

    def __json__(self, users: Optional[Iterable[str]] = None) -> Database:
        return {
            "users": [
                user.__json__()
                for name, user in self.database.items()
                if not users or name in users
            ]
        }

    def add_user(self, user: dict[str, str]) -> str:
        """
        Add user to the database.
        """
        name = user["user"]
        self.database[name] = User(name)
        return json.dumps(self.database[name].__json__())

    def make_lend(self, lend: Lend) -> str:
        """
        Register a lend on the users involved.
        """
        lender = lend["lender"]
        borrower = lend["borrower"]
        self.database[lender].send_money(lend)
        self.database[borrower].receive_money(lend)
        return json.dumps(self.__json__({lender, borrower}))

    def get(self, url: str, payload: Optional[str] = None) -> str:
        """
        GET requests.
        """
        if url != "/users":
            raise NotImplementedError()
        if payload:
            payload = json.loads(payload)["users"]
        return json.dumps(self.__json__(payload))

    def post(self, url: str, payload: Optional[str] = None) -> str:
        """
        POST requests.
        """
        if payload:
            d_payload = json.loads(payload)
        match url:
            case "/add":
                return self.add_user(d_payload)
            case "/iou":
                return self.make_lend(d_payload)
        return ""
