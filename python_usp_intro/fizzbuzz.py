def fizzbuzz(a):
    if a%3 == 0 and a%5 == 0:
        return 'FizzBuzz'
    elif a%3 != 0 and a%5 == 0:
        return 'Buzz'
    elif  a%3 == 0 and a%5 != 0:
        return 'Fizz'
    else:
        return (a)

