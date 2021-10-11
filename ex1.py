def nucleotideSymbol(strand):
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
    return str(a)+' '+str(c)+' '+str(t)+' '+str(g)


strand = input()
symbolNumber = nucleotideSymbol(strand)
print(symbolNumber)
