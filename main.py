print("Exam Grade Calculator")
exam = input("What is the name of your Exam: ")
ps = int(input("What is the max score: "))
ys = int(input("What is your score: "))

p1 = ys / ps
p2 = p1 * 100

print("You got a", p2)
if p2 >= 90 and p2 <= 100:
  print("You got an A")
elif p2 <= 89 and p2 >= 80:
  print("You got a B")
elif p2 <= 79 and p2 >= 70:
  print("You got a C")
else:
  print("You got a F")
  print("BOOOOOO")
