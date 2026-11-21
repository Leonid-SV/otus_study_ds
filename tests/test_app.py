# -*- encode: utf8 -*-

''' test modules'''
from pathlib import Path
import sys
# Добавляем папку уровнем выше в sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from src.app import calc_regr

@pytest.mark.parametrize(
    '''x,weight,bias,expected''',
    [
        [1,20,3,23],
        [0,2,3,3],
        [0,2,3,10],
    ]
)
def test_calc_regr(x,weight,bias,expected):
    ''' --- '''
    assert calc_regr(x,weight,bias)==expected