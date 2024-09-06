from typing import Dict, Any

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Draco": 74,
    "Sean": 95,
    "Or": 54
}
# TODO - Write a program that converts their scores to grades. for exp - - Scores 91 - 100: Grade = "Outstanding" - Scores 81 - 90: Grade = "Exceeds Expectations" - Scores 71 - 80: Grade = "Acceptable" - Scores 70 or lower: Grade = "Fail"
 #first option
for grade in student_scores:
    if student_scores[grade] in range(91, 100):
        student_scores[grade] = "outstanding"
    elif student_scores[grade] in range(81, 90):
        student_scores[grade] = "good"

    elif student_scores[grade] in range(71, 80):
        student_scores[grade] = "ok"

    elif student_scores[grade] in range(0, 55):
        student_scores[grade] = "failed"

print(student_scores)

#second option: as a method,
def grade_calculator(grades: Dict[str, Any]) -> None:

    student_scores = grades

    for grade in student_scores:

        if student_scores[grade] in range(91, 100):
            student_scores[grade] = "outstanding"

        elif student_scores[grade] in range(81, 90):
            student_scores[grade] = "good"

        elif student_scores[grade] in range(71, 80):
            student_scores[grade] = "ok"

        elif student_scores[grade] in range(0, 55):
            student_scores[grade] = "failed"
    print(student_scores)


grade_calculator(student_scores)

# third usage : 2 separate methods - first one that converts the score to a grade,
# second that loops through it and prints the grade

def get_grade(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    else:
        return "Fail"


def print_the_student_grades(student_score_dict: Dict[str, int]):
    student_scores = student_score_dict
    for student, score in student_scores:
        grade = get_grade(score)
        print(f"{student} got {grade} in the test")


print_the_student_grades(student_score_dict=student_scores)