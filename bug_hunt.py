# Part B: Bug Hunt
count = 1
total = 0

# BUG: The while statement was missing a colon at the end.
# Added the colon to begin the while-loop block.
# BUG: The condition used "< 5", which stopped before adding 5.
# Changed it to "<= 5" so the loop includes the number 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Concatenating a string with an integer causes a TypeError.
# Changed to an f-string so the integer total is formatted as text.
print(f"Sum of 1 to 5 is: {total}")
