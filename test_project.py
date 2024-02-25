import pytest
from project import clean_input
from project import validate_input_yes_no
from project import validate_input_general


def test_clean_input():
    assert clean_input(" TEST") == "TEST"
    assert clean_input("TEST ") == "TEST"
    assert clean_input("test") == "TEST"
    assert clean_input("T E S T") == "T E S T"
    assert clean_input("T.E.S.T") == "T.E.S.T"
    assert clean_input("TEST!") == "TEST!"
    assert clean_input("TEST1") == "TEST1"
    assert clean_input("") == ""
    assert clean_input(" ") == ""


def test_validate_input_yes_no():
    assert validate_input_yes_no("Y") == True
    assert validate_input_yes_no("YES") == True
    assert validate_input_yes_no("Y E S") == True
    assert validate_input_yes_no("YABC") == True
    assert validate_input_yes_no("Y123") == True
    assert validate_input_yes_no("Y.!?") == True
    assert validate_input_yes_no("N") == True
    assert validate_input_yes_no("NO") == True
    assert validate_input_yes_no("N O") == True
    assert validate_input_yes_no("NABC") == True
    assert validate_input_yes_no("Nabc") == True
    assert validate_input_yes_no("N123") == True
    assert validate_input_yes_no("N.!?") == True
    assert validate_input_yes_no("R") == False
    assert validate_input_yes_no("!") == False
    assert validate_input_yes_no("JES") == False
    assert validate_input_yes_no("MO") == False
    assert validate_input_yes_no("y") == False
    assert validate_input_yes_no("n") == False
    assert validate_input_yes_no("123") == False


def test_validate_input_general():
    assert validate_input_general("TEST") == True
    assert validate_input_general("test") == True
    assert validate_input_general("Test1") == True
    assert validate_input_general("Test_1") == True
    assert validate_input_general("TEST-1") == True
    assert validate_input_general("TEST 1") == False
    assert validate_input_general("TEST.1") == False
    assert validate_input_general("TEST/1") == False
    assert validate_input_general("(TEST)") == False
    assert validate_input_general("'TEST'") == False
    assert validate_input_general("TEST,TEST") == False
    assert validate_input_general("TEST!") == False
    assert validate_input_general("TEST&TEST") == False
    assert validate_input_general(" ") == False
    assert validate_input_general("") == False
