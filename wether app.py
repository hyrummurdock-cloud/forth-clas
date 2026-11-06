print('Hello, welcome to the weather app!')
rain = input('Is it raining today? (yes/no): ').strip().lower()
if rain == 'yes':
    hours_raining = int(input('how many hours has it been raining? '))
    if hours_raining > 3:
        print('You should stay inside and watch a movie!')
    elif hours_raining > 1:
        print('You should take an umbrella with you!')
    elif hours_raining > 1000:
        print('dont go outside, chaso is coming!')
    else:
        print('You should be ded')
else:
    print('Great! go away ')