import sys
from pathlib import Path

from arquivos.ex02 import soma_q2;

def test_soma_q2():
    assert soma_q2(1,0) == 1
    assert soma_q2(1,1) == 2
    assert soma_q2(1,2) == 3
    assert soma_q2(2,2) == 4
    assert soma_q2(10,10) == 20

def test_soma_q1_b():
    assert soma_q2(0,0) == 0
    assert soma_q2(-1,-1) == -2
    assert soma_q2(-1,1) == 0
    assert soma_q2(-10,-10) == -20
    assert soma_q2(-10,10) == 0
    assert soma_q2(-100,90) == -10

def test_soma_q2_c():
    assert soma_q2(1,1) == 2
    assert soma_q2(0,0) == 0
    assert soma_q2(1,2) == 3
    assert soma_q2(2,2) == 4
    assert soma_q2(-1,-1) == -2
    assert soma_q2(-1,1) == 0