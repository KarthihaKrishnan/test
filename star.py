line2 = '*'
max_length = 6

i = 1
while i <= max_length:
    j = i
    while j < max_length:
        print(' ', end='')
        j += 1
    k = 1
    while k <= i:
        print(line2, end='')
        k += 1
    print()
    i += 1

i = max_length
while i >= 1:
    j = i
    while j <= max_length:
        print(' ', end='')
        j += 1
    k = 1
    while k < i:
        print(line2, end='')
        k += 1
    print('')
    i -= 1
