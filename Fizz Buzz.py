#FizzBuzz 問題

a = int(input())

b = 1
while b < a:
    if b % 3 and b % 5 == 0:
        print("FizzBuzz")
    elif b % 3 == 0:
        print("Fizz")
    elif b % 5 == 0:
        print("Buzz")
    else:
        print(b)
    b += 1
print(b)
