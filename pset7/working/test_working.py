from working import convert, convert_hours

import pytest


# Check convert_hour() function properly converting based on period
def test_convert_hour():
    assert convert_hours(12 ,"AM") == 0
    assert convert_hours(5 ,"AM") == 5
    assert convert_hours(12 ,"PM") == 12
    assert convert_hours(5 ,"PM") == 17


# Check 'to' in user's input
def test_to():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
        convert("9 AM - 5 PM")
        convert("5 PM - 9 AM")


# Check valid hour
def test_hour():
    with pytest.raises(ValueError):
        convert("21 AM to 5 PM")
        convert("9 AM to 17 PM")


# Check valid minutes
def test_minute():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
        convert("9 AM to 5:60 PM")
        convert("9:70 AM to 5 PM")


# Check time format
def test_format():
    with pytest.raises(ValueError):
        convert("21 to 5")
        convert("9:00 to 17")


# Check valid results
def test_valid():    
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"