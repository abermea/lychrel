def reverse_number(num: int):
    return int(str(num)[::-1])

def sum_number(num: int):
    return num + reverse_number(num)

def test_palindrome(num: int):
    return str(num) == str(num)[::-1]

max_steps = 500
successful = []
failure = []

for x in range(1,2000):
    num = x
    steps = 0

    while test_palindrome(num) is not True and steps < max_steps:
        steps += 1
        num = sum_number(num)

    if steps < max_steps:
        # print("Palindrome for {} found after {} operations! Final number was {}".format(x, steps, num))
        successful.append((x, steps))
    else:
        # print("Palindrome for {} NOT found after exceeding max operations! Final number was {}".format(x, num))
        failure.append((x, steps))

print("Failed: {}".format(failure))