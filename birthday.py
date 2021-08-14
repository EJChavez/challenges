import random

def main():
    hits = 0
    loops = 10000
    people = 23
    for i in range(0,loops):
        birthdays = {}
        for i in range(0,people):
            birthdays[f'Person {i}'] = random.randint(1,365)
        for item in birthdays.items():
            person,birthday = item
            success = False
            for items in birthdays.items():
                second_person, check_birthday = items
                if person != second_person:
                    if birthday == check_birthday:
                        hits += 1
                        success = True
                        break
            if success:
                break
    print(f'People shared a birthday {hits} times, they failed to share a birthday {loops-hits} times.')


main()