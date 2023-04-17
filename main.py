def reverse_number(num: int):
    return int(str(num)[::-1])

def sum_number(num: int):
    return num + reverse_number(num)

def test_palindrome(num: int):
    return str(num) == str(num)[::-1]

def lycrel_test_on_range(start: int, end: int, max_steps: int): 
    results = []

    for x in range(start, end):
        num = x
        steps = 0

        while test_palindrome(num) is not True and steps < max_steps:
            steps += 1
            num = sum_number(num)
        
        result = {
            "number" : x,
            "isPalindrome": True if steps < max_steps else False,
            "steps" : steps
        }

        results.append(result) 

    return results

start = 0 # Where to start
end = 2000 # Where to end
max_steps = 500 # Max attempts before making a failure to prevent infinite loops

results = lycrel_test_on_range(start, end, max_steps)

print("Failed: {}".format(list(filter(lambda x : x["isPalindrome"] == False, results))))