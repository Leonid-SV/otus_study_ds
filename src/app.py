# -*- coding: utf8 -*-
"""Рассчитываем формулу линейной регрессии для одномерного случая"""

from typing import Union


def calc_regr(
    x: Union[int, float], weight: Union[int, float], bias: Union[int, float]
) -> Union[int, float]:
    print()
    return weight * x + bias


if __name__ == "__main__":
    x, a, b = 1, 2, 3
    calc_regr(x, a, b)