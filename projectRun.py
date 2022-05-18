from Periodic_Table_Top_Trumps import random_element

print(" _____________________________________ ")
print("|                                     |")
print("|      Periodic Table Top Trumps      |")
print("|_____________________________________|")
print("")

def run():
    my_element = random_element()
    print('You were given {}'.format(my_element['name']))
    stat_choice = input('Which element do you want to use? (atomicNumber, boilingPoint, density) ')
    opponent_element = random_element()
    print('The opponent chose {}'.format(opponent_element['name']))
    my_stat = my_element[stat_choice]
    opponent_stat = opponent_element[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
run()