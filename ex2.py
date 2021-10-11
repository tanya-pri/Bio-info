def atPercentage():
    strand = input()
    a, t, g, c = 0, 0, 0, 0
    for i in strand:
        if i == 'A':
            a += 1
        elif i == 'T':
            t += 1
        elif i == 'G':
            g += 1
        elif i == 'C':
            c += 1
    at = (a + t) * 100 / (a + t + c + g)
    percentAt = round(at, 2)
    print(percentAt, sep='', end='%')


atPercentage()