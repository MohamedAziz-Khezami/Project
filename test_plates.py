from plates import is_valid

def test_is_valid():
    assert is_valid("hello")==True
    assert is_valid("CS50") ==True
    assert is_valid("23342") ==False
    assert is_valid("aziz34212") ==False
    assert is_valid("aziz343j") == False
    assert is_valid("12aaag") ==False
    assert is_valid("helo334ai") == False
    assert is_valid("HOLA") == True
    assert is_valid("2342") == False
    assert is_valid("az012")  == False
    assert is_valid("") == False
    assert is_valid("ABC12") == True
    assert is_valid("h23a") == False
    assert is_valid("Excel2") == True
    assert is_valid("HI1.2") == False
    assert is_valid("1,2")==False
    assert is_valid("1,3.4")==False
    assert is_valid("hi12.3")==False
    assert is_valid("123456") ==False
    assert is_valid("aqs1") == True
    assert is_valid("B2MAN") == False
    assert is_valid("2AA") == False
    assert is_valid("hi3y") == False