for i in range(1, 31):
    if i%5 == 0:
        if i%3 == 0:
            print('fizzbuzz')
        else:
            print('buzz')
    if i%3 == 0:
        print('fizz')
