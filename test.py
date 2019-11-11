is_underage = int(input('What is your age:'))
if is_underage >= 21:
    print('you may drink, smoke, and drive if you wish!')
elif is_underage >= 18:
    print('You may smoke and drive!')
elif is_underage >= 16:
    print('you may drive!')
else :
    print('Enjoy your bike and the buss kid!')