import math
import random

# This is my quiz game
# I'm going to put my test functions and stuff in here

def get_addition_question (level):
    addend1 = random.randint(1,10*level)
    addend2 = random.randint(1,10*level)
    return '%i+%i'%(addend1,addend2),addend1+addend2


def test_get_addition_question ():
    for l in range(1,10):
        print 'Level ',l,'questions:'
        for tst in range(3):
            q,a = get_addition_question(l)
            print 'Question: ',q,'Answer:',a

test_get_addition_question()            
