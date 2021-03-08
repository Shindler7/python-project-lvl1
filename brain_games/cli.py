"""
Вспомогательный модуль учебного проекта.
"""
import prompt


def welcome_user() -> str:
    """
    Приветствие пользователя.
    """

    return prompt.string('May I have your name? ')
