three, five, total = 3, 5, 0

while three < 1000 or five < 1000:
    if three < five:
        total += three
        three += 3
    elif five < three:
        total += five
        five += 5
    else:
        total += three
        three += 3
        five += 5

print total
