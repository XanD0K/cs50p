from seasons import validate_date, minutes_since_birth


def test_format():
    assert validate_date("01-12-1994") == False
    assert validate_date("06-30-1962") == False
    assert validate_date("1962-30-06") == False


def test_str():
    assert validate_date("December 1, 1994") == False
    assert validate_date("I was born on 1994-12-01") == False


def test_punctuation():
    assert minutes_since_birth("1994-12-01") == 16161120
    assert minutes_since_birth("1962-06-30") == 33213600

