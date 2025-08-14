tweet = input("Tweet: ")
# Get every character in user's input if not a vowel
shorten_tweet = "".join(c for c in tweet if c.lower() not in 'aeiou')

print("Output: " + shorten_tweet)