a=int(input(''))
e=int(input(''))
d=int(input(''))
c=int(input(''))
b=int(input(''))
sum = a + b + c + d + e
print(sum)
perc = (sum/500)*100
print('= Percentage mark = ', perc)
if perc >= 80:
    print('Grade: A')
elif perc >= 60: 
    print('Grade: B')
elif perc >= 40:
    print('Grade: C')
elif perc >= 20:    
    print('Grade: D')
else:
    print('Grade: F')