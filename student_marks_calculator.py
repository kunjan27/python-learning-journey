name = input('Enter student name: ')
a  = int(input("Enter marks in python: "))
b = int(input("Enter marks in physics: "))
c  = int(input("Enter marks in maths: "))
print()
print()

print("----------------STUDENT MARKS REPORT----------------")

print(f"student: {name}")
print(f"python: {a}")
print(f"physics: {b}")
print(f"maths: {c} ")
d = a+b+c
print(f"total marks: {d}/300")
e = (d)/3
print(f"average marks: {e}")
print()
print("--------------------------------")