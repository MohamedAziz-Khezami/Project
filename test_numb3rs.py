from numb3rs import validate




def test_validate():
    assert validate("255.255.255.255")==True

    assert validate("255.255.255")==False
    assert validate("255.259.255.255")==False
    assert validate("1.2.3.1000") == False