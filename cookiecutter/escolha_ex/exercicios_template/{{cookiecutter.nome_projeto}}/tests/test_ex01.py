import sys
from pathlib import Path

from arquivos.ex01 import soma_q1;

def test_soma_q1():
    assert soma_q1(1,0) == 1
    assert soma_q1(1,1) == 2
    assert soma_q1(1,2) == 3
    assert soma_q1(2,2) == 4
    assert soma_q1(10,10) == 20

def test_soma_q1_b():
    assert soma_q1(0,0) == 0
    assert soma_q1(-1,-1) == -2
    assert soma_q1(-1,1) == 0
    assert soma_q1(-10,-10) == -20
    assert soma_q1(-10,10) == 0
    assert soma_q1(-100,90) == -10

def test_soma_q1_c():
    assert soma_q1(1,1) == 2
    assert soma_q1(0,0) == 0
    assert soma_q1(1,2) == 3
    assert soma_q1(2,2) == 4
    assert soma_q1(-1,-1) == -2
    assert soma_q1(-1,1) == 0