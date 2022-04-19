with open('pi_million_digits.txt') as file:
    pi = ''
    for line in file:
        pi += line.strip()

    print(pi[:52])
    print(len(pi))