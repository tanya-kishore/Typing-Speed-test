import time
import random as r

def count_wpm(text, time_taken):
    words = text.split()
    num_words = len(words)
    wpm = (num_words / time_taken) * 60
    return wpm

def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        if i >= len(usertest) or paratest[i] != usertest[i]:
            error += 1

    return error


def accuracy(paratest,usertest):
    error=mistake(paratest,usertest)
    total_characters = len(paratest)
    acc = 1 - (error / total_characters) if total_characters > 0 else 0
    acc_perc=acc*100

    return acc_perc



test=["the quick brown fox jumps over the lazy dog sphinx of black quartz, judge my vow five hexing wizard bots jump quickly,pack my box with five dozen liquor jugs."," jiving crazy fox nymph grabs quick waltz","quick brown foxes jump over the lazy dog",
    "lazy dog jumps over the quick brown fox jackdaws love my big sphinx of quartz mr. jock, tv quiz phd, bags few lynx quick wafting zephyrs vex bold jim going round above the world garden looks beautiful",
    "five big quacking zephyrs jolt my wax bed the five boxing wizards jump quickly the quick onyx goblin jumps over the lazy dwarf helping out there also a good work happily ever after",
    "quartz glyph job vex'd cwm finks quick zephyrs blow, vexing daft jim my girl wove six dozen plaid jackets before she quitquick zephyrs blow going out works more ring and roses"," vexing daft jim my girl wove six dozen plaid jackets before she quit cwm fjord bank glyphs vext quiz glyphs quietly joke on the zephyrs the jay, pig, fox, zebra, and my wolves quack sphinx of black quartz, judge my vow how razorback-jumping frogs can level six piqued gymnasts"]

test1 = r.choice(test)

print(test1)
start_time = time.time()
testinput = input("Please enter the given text: ")
end_time = time.time()
time_taken = end_time - start_time

wpm =count_wpm(testinput, time_taken)

mis = mistake(test1, testinput)
check =accuracy(test1, testinput)


print("Total words per minute is: ",wpm)
print("Your accuracy is: ",check)
