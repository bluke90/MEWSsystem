body = "there is a solar flare coming!"
bodyx = list(body.split(" "))
sfWarning = body.count('solar flare')
print(sfWarning)
warnWords = ['tornado', 'tornados', 'earthquake', 'earth quake']
warnx = frozenset(warnWords)

if bodyx in warnx:
    print("+")