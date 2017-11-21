def get_odds():
    for number in range(10):
        if not number % 2:
            yield number

for i, odd in enumerate(get_odds(), 1):
    if i == 3:
        print(odd)
        break

