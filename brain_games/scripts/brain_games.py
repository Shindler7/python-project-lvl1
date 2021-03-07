#!/usr/bin/env python

"""
Учебный основной модуль.
"""
from brain_games.cli import welcome_user


def main():
    """
    Стартовая функция.
    """

    print('Welcome to the Brain Games!')

    welcome_user()


if __name__ == '__main__':
    main()
