print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name,". You are", age, "years old!" )


points = 10
if age >= 18:
    print("Hello", name,". At age", age, "you are old enough to play.")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Great, let's play!")
        print("You are starting with", points, "points.")

        left_or_right = input("Do you want to go left or right? (left or right) ")
        if left_or_right == "left":
            points += 5
            print("points:", points)
            ans = input("You follow a path and reach a lake. Do you swim across or go around? (swim/around) ")

            if ans == "swim":
                print("Whoops! You got bit by a stingray and lost 5 points.")
                points -= 5
                print("You have ",points, "points.")
            elif ans == "around":
                points += 5
                print("By going around, you now have", points, "points.")
                ans2 = input("You made it to the other side. Do you knock at the cottage door or walk towards town? (cottage/town) ")

                #selected cottage
                if ans2 == "cottage":
                    points -= 5
                    print("The owner does not like you. You have lost 5 points.") 
                    print("You have", points, "points.")
                    ans3 = input("Do you go into the forest to towards town? (forest/town)")

                    if ans3 == "forest":
                        points = 0
                        print("Game Over,", name, ".You were eaten by a bear! You have zero points.")
                #selected town
                else:
                    points += 5
                    print("You made the right choice. With", points,"points, you win!")

            else:
                print("You lose!")
                points = 0


#you chose right
        else:
            print("You tripped, fell and lost!")
            points = 0
    else:
        print(" you have lost your 10 points. Buh bye!")

elif age >= 14:
    print("You can play as long as you have supervision.")
else:
    print("Sorry,", name, "enjoy your youth some other way!")


