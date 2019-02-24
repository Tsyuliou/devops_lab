def print_formatted(number):
    if number >= 1 and number <= 99:
        width = len("{0:b}".format(number))
        for i in range(number):
            i += 1
            print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))
