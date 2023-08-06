

name = input("What is your name? ")

student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y", "yes")

age = int(input("How old are you? "))

message = "Hello " + name

def get_message(student,age,message):
    if student and (age <= 18 or age > 65):
        message += " - congratulations, you are entitled to a 20% discount"
    elif student or (age <= 18 or age > 65):
        message += " - congratulations, you are entitled to a 10% discount"
    else:
        message += " - sorry, you must pay the regular price"
    print(message)

get_message(student,age,message)

print()
input("Press return to continue ...")
