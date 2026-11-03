a = input("Enter a value for a: ")
b = input ("Enter a value for b: ")
if a == b :
    print("a and b are the same")
else:
    print("a and b are not the same")
while 1==1:
  height = float(input("Enter your height in cm: "))
  weight = float(input("Enter your weight in kg: "))
  bmi = weight / (height/100)**2
  if bmi < 18.5:
    print("You are underweight.")
  elif bmi < 24.9:
    print("You are healthy.")
  elif bmi < 29.9:
    print("You are overweight.")
  elif bmi < 34.9:
    print("You are severely overweight.")
  elif bmi < 39.9:
    print("You are obese.")
  elif bmi < 50:
    print("You are extremely obese.")
  elif bmi < 60:
    print("You are so fat that you can't even see your toes.")
  else:
    print("You are ded.")

