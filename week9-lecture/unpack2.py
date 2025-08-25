def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# Indexes into a dict
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts", end="\n\n")


# Dict unpack
print(total(**coins), "Knuts")
# It unpackles like: galleons=100, sickles=50, knuts=25