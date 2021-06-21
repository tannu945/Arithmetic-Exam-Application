
import random
count = 0
choice_name = ""
print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
choice = int(input())
if choice == 1:
    choice_name = "simple operations with numbers 2-9"
    for i in range(0, 5):
        a = random.randint(2, 9)
        b = random.choice('+-*')
        c = random.randint(2, 9)
        my_math = str(a) + " " + b + " " + str(c)
        print(my_math)
        while True:
            try:
                d = int(input())
                break
            except (ValueError, NameError):
                print("Incorrect format.")
        if eval(my_math) == d:
            print("Right!")
            count += 1
        else:
            print("Wrong!")
    print("Your mark is " + str(count) + "/ 5. Would you like to save the result? Enter yes or no.")
elif choice == 2:
    choice_name = "integral squares of 11-29"
    for i in range(0, 5):
        integral_sq = random.randint(11, 29)
        print(integral_sq)
        while True:
            try:
                square = int(input())
                break
            except (ValueError, NameError):
                print("Incorrect format.")
        if integral_sq ** 2 == square:
            print("Right!")
            count += 1
        else:
            print("Wrong!")
    print("Your mark is " + str(count) + "/ 5. Would you like to save the result? Enter yes or no.")
choice_2 = input()
if choice_2 == 'YES' or choice_2 == 'yes' or choice_2 == 'y' or choice_2 == 'Yes':
    print("What is your name?")
    name = input()
    result_file = open('results.txt', 'a+')
    result_file.write('{name}: {count}/5 in level {choice} ({description})'.format(name=name, count=count, choice=choice, description=choice_name))
    print('The results are saved in "results.txt".')
else:
    exit()
