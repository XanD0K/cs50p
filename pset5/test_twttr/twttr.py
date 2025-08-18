def main():
    word = input("Enter a word: ")
    shorten_word = shorten(word)
    print(shorten_word)
    

def shorten(word):
    return "".join(c for c in word if c.lower() not in 'aeiou')
    

if __name__ == "__main__":
    main()