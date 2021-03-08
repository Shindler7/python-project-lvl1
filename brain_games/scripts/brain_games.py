#!/usr/bin/env python

"""
Учебный основной модуль.
"""
from .brain_even import main as main_even
from brain_games import cli


def main():
    """
    Стартовая функция.
    """

    print('Welcome to the Brain Games!')

    name = cli.welcome_user()
    print(f'Hello, {name}!')

    main_even(name)


if __name__ == '__main__':
    main()
