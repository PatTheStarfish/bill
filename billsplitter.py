import random


print("Enter the number of friends joining (including you):")
guest_list = {}
try:
    number_of_guests = int(input())
except ValueError:
    print("No one is joining for the party")
else:
    if number_of_guests <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for x in range(number_of_guests):
            guest_name = input()
            guest_list.update({guest_name: 0})
        print("Enter the total bill value:")
        bill = int(input())
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        user_input = input()
        if user_input == "Yes":
            lucky_friend = random.choice(list(guest_list.keys()))
            print(f"{lucky_friend} is the lucky one!")
            cost = round(bill / (len(guest_list) - 1), 2)
            for x in guest_list:
                guest_list[x] = cost
            guest_list[lucky_friend] = 0
            print(guest_list)
        else:
            print("No one is going to be lucky")
            cost = round(bill / len(guest_list), 2)
            for x in guest_list:
                guest_list[x] = cost
            print(guest_list)
