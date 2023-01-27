"""
https://exercism.org/tracks/python/exercises/ledger
"""
# -*- coding: utf-8 -*-
from datetime import datetime
from dataclasses import dataclass
from typing import Callable, TypedDict


def us_currency(value: float, symbol: str) -> str:
    """
    Returns the str of the value in us style.
    """
    str_curr = f"{symbol}{abs(value):,.2f}"
    if value < 0:
        return f"({str_curr})"
    return str_curr + " "


def nl_currency(value: float, symbol: str) -> str:
    """
    Returns the str of the value in nl style.
    """
    return f"{symbol} {value:_.2f} ".replace(".", ",").replace("_", ".")


class Locale(TypedDict):
    """
    Specific formats for differents locales.
    """

    header: tuple[str, str, str]
    date: str
    currency: Callable[[float, str], str]


LOCALE: dict[str, Locale] = {
    "en_US": {
        "header": ("Date", "Description", "Change"),
        "date": "%m/%d/%Y",
        "currency": us_currency,
    },
    "nl_NL": {
        "header": ("Datum", "Omschrijving", "Verandering"),
        "date": "%d-%m-%Y",
        "currency": nl_currency,
    },
}


CURRENCY_SYMBOL = {"USD": "$", "EUR": "€"}


@dataclass(order=True, frozen=True)
class Description:
    """
    Description of a Ledger.
    """

    text: str

    def __str__(self) -> str:
        return f"{self.text:.22}..." if len(self.text) > 25 else f"{self.text:<25}"


@dataclass(order=True, frozen=True)
class LedgerEntry:
    """
    Represents a ledger. With order=True, it has total ordering.
    """

    date: datetime
    change: int
    description: Description


def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    """
    Factory constructor for LedgerEntry.
    """
    return LedgerEntry(
        datetime.strptime(date, "%Y-%m-%d"), change, Description(description)
    )


def create_header(header: tuple[str, str, str]) -> str:
    """
    Creates the header for the table.
    """
    column_a, column_b, column_c = header
    return f"{column_a:<11}| {column_b:<25} | {column_c:<13}"


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    """
    Creates a table with the Ledgers.
    """
    conf: Locale = LOCALE[locale]
    table = create_header(conf["header"])
    for entry in sorted(entries):
        table += "\n"
        table_date = entry.date.strftime(conf["date"])
        table_change = conf["currency"](entry.change / 100, CURRENCY_SYMBOL[currency])
        table += f"{table_date} | {entry.description} | {table_change:>13}"
    return table
