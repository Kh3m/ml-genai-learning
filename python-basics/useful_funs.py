def find_mean(numbers):
    return sum(numbers) / len(numbers)

def add_five(numbers):
    return [ n + 5 for n in numbers if not(n < 0)  ]


print("This code is ran whenever this module is imported")

def main():
    print("This code is ran only when this script/module is executed")
    print("======================")
    
    print("Testing find_mean function...")
    numbs = [1,2,3,4]
    correct_mean = 2.5
    assert(find_mean(numbs) == correct_mean)

    print("Testing add_five function...")
    correct_numbs = [6,7,8,9]
    assert(add_five(numbs) == correct_numbs)

    print("All tests passed!")

print("__name__", __name__)
if __name__ == "__main__":
    main()
