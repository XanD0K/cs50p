# This code has the purpose of check is_valid() function from plates.py

from plates import is_valid


# Check for plate length (between 2 and 6 characters)
def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCD") == True


# Check if first 2 characters are letters
def test_first_two_characters():
    assert is_valid("11AB") == False
    assert is_valid("1ABC") == False
    assert is_valid("1A1B") == False
    assert is_valid("A1B1") == False
    assert is_valid("123456") == False
    assert is_valid("AB11") == True
    assert is_valid("ABCD11") == True



# Check if there is no whitespaces, periods or punctuations
def test_only_alnum():
    assert is_valid("AB D") == False
    assert is_valid("A.CD") == False
    assert is_valid("AB!D") == False
    assert is_valid("ABC;") == False
    assert is_valid("AAAA") == True


# Check if first decimal, when any, is not a zero
def test_no_zero_beggining():
    assert is_valid("AB01") == False
    assert is_valid("ABC0") == False
    assert is_valid("ABC012") == False
    assert is_valid("AB10") == True
    assert is_valid("AB1000") == True

# Check if numbers only appears at the end of the plate, not in the middle
def test_numbers_at_end():
    assert is_valid("AB12EF") == False
    assert is_valid("ABC1EF") == False
    assert is_valid("ABCD1F") == False
    assert is_valid("AB1234") == True
    assert is_valid("ABCDE1") == True
