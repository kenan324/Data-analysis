import datetime

def getBirthdays():
    birthdays = []

    with open('studenti_rodjendani_in_class.txt', 'r') as f:
        for line in f:
            dt = datetime.datetime.strptime(line.strip() + "-2000", "%d-%m-%Y")
            birthdays.append(dt)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


birthdays = getBirthdays()

print("\nBirthdays from my class\n")
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Several people in my class have birthdays on', dateText)
else:
    print('No one in my class has a birthday on the same day.')
print()

