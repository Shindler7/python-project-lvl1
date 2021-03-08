"""
Игровые модули.
"""
import secrets

import prompt

from brain_games import cli

phrase_base = {
    'welcome': 'Answer "yes" if the number is even, otherwise answer "no".',
    'conversation': {
        'question': 'Question: {figure}',
        'answer': 'Your answer: '
    },
    'reaction': {
        'correct': 'Correct!',
        'success': 'Congratulations, {name}!',
        'failed': "'{wrong}' is wrong answer ;(. Correct answer "
                  "was '{correct}'.\n"
                  "Let's try again, {name}!"
    }

}


def figures(loop: int, n_range: int = 100):
    """
    Генерирует ряд случайных чисел в диапазоне от 1 до N.

    :parameter loop: Количество повторов.
    :parameter n_range: Диапазон чисел (верхний предел).
    """

    arr = []
    range_base = range(1, n_range + 1)
    one = 0
    while one < loop:
        num = secrets.choice(range_base)
        if num in arr:
            continue

        one += 1
        arr.append(num)

        yield num


def is_even(figure: int) -> bool:
    """
    Проверяет чётность числа (True).
    """

    return figure % 2 == 0


def is_correct(answer: str, figure: int) -> tuple:
    """
    Проверка, что пользователь ответил верно.

    :param answer: Ответ пользователя.
    :param figure: Загаданное число.
    """

    answer_base = {
        'yes': {'bool': True, 'antidote': 'no'},
        'no': {'bool': False, 'antidote': 'yes'}
    }

    is_figure_even = is_even(figure)

    answer = answer.lower()
    user_check = answer_base.get(answer, answer_base['no'])

    return (is_figure_even == user_check['bool'],
            user_check['antidote'])


def main(name: str = None):
    """
    Распордяитель игры "Проверка на чётность".
    """

    if name is None:
        name = cli.welcome_user()
        print(f'Hello, {name}!')

    print(phrase_base['welcome'])

    for figure in figures(3, 100):
        message = phrase_base['conversation']['question'].format(figure=figure)
        print(message)

        answer = prompt.string(phrase_base['conversation']['answer'])
        correct, antidote = is_correct(answer, figure)
        if not correct:
            message = phrase_base['reaction']['failed'].format(
                name=name,
                wrong=answer,
                correct=antidote
            )
            return print(message)

        message = phrase_base['reaction']['correct']
        print(message)

    else:
        message = phrase_base['reaction']['success'].format(name=name)
        print(message)


if __name__ == '__main__':
    main()
