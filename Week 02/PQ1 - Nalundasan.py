"""
PQ1
"""

family_name = str(input('Enter family name: '))
gender = str(input('Male or Female? '))
marriage = str(input('Married? Yes or No '))

if gender == 'Male':
    salutation = 'Mr.'
elif marriage == 'Yes':
    salutation = 'Mrs.'
elif marriage == 'No':
    salutation = 'Miss'

print('{} {}'.format(salutation, family_name))
