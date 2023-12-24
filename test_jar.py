from jar import Jar


def test_init():
    jar = Jar(12)
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar = Jar(100)
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(4)
    assert jar.size == 4
    jar.withdraw(4)
    assert jar.size == 0
