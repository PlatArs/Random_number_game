"""Мой подход: Угадывание с сокращением диапазона
"""

import numpy as np

def game_core_MY(number: int = 1) -> int:
    """ Алгоритм с каждой итерацией сокращает диапозон возможных значений загадоного числа. 
        Сначала алгоритм задаёт случайное число, которое будет являтся границей диапазона.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    np.random.seed(1)
    min_ = 1
    max_ = 101

    while True:
        predict_number = np.random.randint(min_, max_) # предполагаемое число
        count += 1
        if predict_number == number: 
            return count
        elif predict_number < number: # устанавливаем наименьшее возможное значение
            min_ = predict_number
        elif predict_number > number: # устанавливаем максимально возможное значение
           max_ = predict_number