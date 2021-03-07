#!/usr/bin/env python

"""
Вспомогательный модуль учебного проекта.
"""
import prompt


def welcome_user():
    """
    Приветствие пользователя.
    """

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
