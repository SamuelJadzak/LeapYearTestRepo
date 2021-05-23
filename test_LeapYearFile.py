from LeapYearFile import LeapYear

def test_GoodLeapYear():
    assert LeapYear(2004) == True

def test_BadLeapYear():
    assert LeapYear(1999) == False
