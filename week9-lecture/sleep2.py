# Returns a list of sheep


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()


# This function works, but it might stops working if we ask for a big number os sheep
# In that case, the computer ran out of memory