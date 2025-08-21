from um import count


# Check if 'um' is part of a word
def test_word():
    assert count("Album") == 0
    assert count("Yummy") == 0
    assert count("Yum") == 0
    assert count("Umbrella") == 0

def test_punctuation():
    assert count("...um") == 1
    assert count("um, I think I forgot my umbrella") == 1
    assert count("Um, thanks, um...") == 2

def test_counter():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um um um") == 3
    assert count("um um um um") == 4