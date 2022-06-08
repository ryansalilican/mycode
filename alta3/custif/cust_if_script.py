#!/usr/bin/env python3
import time
print("Mr. Feeser, your class grade is standing on the precipice of either failure or passing.\n ")
time.sleep(5)
print("Our class took the final exam last week.\n")
time.sleep(3)
print("I handed out your test scores. Your score will determine if you passed or failed the class.\n")
time.sleep(5)
print("So...")
time.sleep(2)

message = 'You received a score of '
score = int(input("What score did you get?"))
time.sleep(2)

if score >= 79:
    message = message + str(score) + '? Well well, Mr. Feeser! You need not worry at all!\nGreat job, sir! Great job!'
elif score >= 60:
    message = message + str(score) + '? Mr. Feeser. A little bit of more practice and you would have passed the class.\nThere is no curve and there are no handouts.\nI will see you next semester.'
elif score >= 49:
    message = message + str(score) + '? Do you hate me, Mr. Feeser?\nAre you doing this to spite me? Apply yourself.'
else:
    message = message + str(score) + '? Get out.\nNope. Do not speak.\nGood day, Mr. Feeser'
print(message)
