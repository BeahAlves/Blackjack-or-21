import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_hand = random.choices(cards, k=2)
pc_hand = random.choices(cards, k=2)

my_value = sum(my_hand)
pc_value = sum(pc_hand)

print(f"Your cards: {my_hand}, current score: {my_value}")
print(f"Computer's first card: {pc_hand[0]}")

while True:
    another_card = input(f"Would you want another card? Type [Y/N]. ")
    if another_card in "yY":
        my_hand.append(random.choice(cards))
        my_value = sum(my_hand)
        print(f"Your cards {my_hand}, current score: {my_value}")
        if my_value > 21:
            print(f"You went over 21, your score was: {my_value}. You lost! ")
            break
    elif another_card in 'nN':
        if pc_value < 17:
            while pc_value < 17:
                pc_hand.append(random.choice(cards))
                pc_value = sum(pc_hand)
        print(f"Your final hand was: {my_hand}, final score: {my_value}")
        print(f"Pc hand was {pc_hand}, total score of {pc_value}")
        if pc_value > 21:
            print("The computer went over 21. Congratulations, you won!")
            print(f"Your final hand was: {my_value}, agains {pc_value} from the computer")
            break
        elif my_value > pc_value:
            print("Congratulations, you won! ")
            print(f"Your final hand was: {my_value}, agains {pc_value} from the computer")
            break
        elif pc_value > my_value:
            print("Oh no, you lost! ")
            print(f"Your final hand was: {my_value}, agains {pc_value} from the computer")
            break
        elif pc_value == my_value:
            print("That's a tie ")
            break

