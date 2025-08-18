# This code has the purpose of testing shorten() function from 'twttr.py'

from twttr import shorten

# Test full names
def test_name():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Alexandre") == "lxndr"
    assert shorten("David") == "Dvd"


# Test whitespaces and punctuations
def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("How are you?") == "Hw r y?"
    assert shorten("Lots, of. punctuations! to# be@ teste?") == "Lts, f. pncttns! t# b@ tst?"


# Test lower and upper case words
def test_case_sensitivity():
    assert shorten("CS50") == "CS50"
    assert shorten("cs50") == "cs50"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"