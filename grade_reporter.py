# Week 3: Conditions and Loops — Grade Reporter

scores = [85, 72, 94, 58, 100]

total = 0
passed = 0

print("Grade Report")
print("-" * 30)

for score in scores:
    total += score

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    if score >= 60:
        passed += 1

    print(f"Score: {score} | Grade: {grade}")

average = total / len(scores)

print("-" * 30)
print(f"Number of students: {len(scores)}")
print(f"Total scores: {total}")
print(f"Average score: {average:.2f}")
print(f"Students passed: {passed}")
print(f"Students failed: {len(scores) - passed}")
