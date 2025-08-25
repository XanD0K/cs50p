# Uses yield
# In Python, you can define a function as generator
# It allows to generate a massive amount of data, by returning just a little bit of data at a time
# To do that, we use the keyword 'yield'
# It generates data 'on demand', returning one value at a time
# 'yield' returns an iterator that allows the loop to iterate over the generated values one at a time

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
