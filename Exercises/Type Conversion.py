birth_year = int(input('what year where you born? '))
birth_month = input('what month where you born? ')
birth_day = int(input('what day where you born? '))
current_year = 2019
if birth_month == 'dec':
    print(current_year - birth_year - 1)
elif birth_month == 'nov' and birth_day == 26:
    print(current_year - birth_year -1)
else:
    print(f'your age is {current_year - birth_year}')



