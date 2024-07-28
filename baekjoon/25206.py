import sys

grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0,
}

total_credits = 0
total_score = 0

for _ in range(20):
    n, credit, grade = sys.stdin.readline().rstrip().split(" ")
    credit = float(credit)
    if grade != "P":
        total_credits += credit
        total_score += grade_dict[grade] * credit

grade = total_score / total_credits

print(grade)
