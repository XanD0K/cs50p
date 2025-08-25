# https://harrypotter.fandom.com/wiki/Wizarding_currency

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# Passes positional arguments as usual
print(total(100, 50, 25), "Knuts", end="\n\n")


# Indexes into a list
coins = [100, 50, 25]
print(total(coins[0], coins[1], coins[2]), "Knuts", end="\n\n")


# List unpack
print(total(*coins), "Knuts", end="\n\n")


# Passes name arguments → allows to pass in any order we like
print(total(galleons=100, sickles=50, knuts=25), "Knuts")