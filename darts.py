print("Good luck!\n")


#Number of players

def num_players():

    players = "default"

    while players not in ["1","2","3","4"]:

        players = input("Please type in the number of players (1-4): ")


    return int(players)


#Name of the players

def players_name(players):

    if players == 1:
        player1 = input("Player1 name: ")
        return player1, "default", "default", "default"
    elif players == 2:
        player1 = input("Player1 name: ")
        player2 = input("Player2 name: ")
        return player1, player2, "default", "default"
    elif players == 3:
        player1 = input("Player1 name: ")
        player2 = input("Player2 name: ")
        player3 = input("Player3 name: ")
        return player1, player2, player3, "default"
    elif players == 4:
        player1 = input("Player1 name: ")
        player2 = input("Player2 name: ")
        player3 = input("Player3 name: ")
        player4 = input("Player4 name: ")
        return player1, player2, player3, player4

#The players shot

def current_point():

    shot = "default"

    while shot.isnumeric() != True:

        shot = input("\nPlease type in your current shot: ")

        if shot.isnumeric() == True:

            if int(shot) <= 0 or int(shot) > 60:
        
                shot = input("\nPlease type in your current shot: ")

    return int(shot)

#Single double or triple

def single_double_triple():

    times = "default"

    while times not in ["S", "D", "T"]:

        times = input("Was it a single, double or triple? (Type S, D or T) ").upper()

    if times == "S":
        times = 1
    elif times == "D":
        times = 2
    elif times == "T":
        times = 3
    return times

#The counter

def the_game(player1 = "default", player2 = "default", player3 = "default", player4 = "default"):


#1 player

    if player1 != "default" and player2 == "default" and player3 == "default" and player4 == "default" :
        print(f"{player1}'s turn!\n")

        point1 = 301
        while point1 > 0:

       
            if point1 > 0:
                print("\n"*100)
                print(f"\nYou have {point1} points!")
                times = single_double_triple()
                save1 = current_point() * times
                point1 = point1 - save1
                if point1 < 0:
                    point1 = point1 + save1
            if point1 == 0:
                    print("You WON!")
                    break 
                    

#2 players

    if player1 != "default" and player2 != "default" and player3 == "default" and player4 == "default":

        point2 = 301
        point1 = 301
        
        while point1 != 0 and point2 != 0:

            shot_counter1 = 3
            shot_counter2 = 3
            

            while shot_counter1 != 0 :

                if point1 > 0:
                    print("\n"*100)
                    print(f"\n{player1}'s turn! {shot_counter1} shot(s) remaining.\nYou have {point1} points!")
                    times = single_double_triple()
                    save1 = current_point() * times
                    point1 = point1 - save1
                    shot_counter1 -= 1
                    if point1 < 0:
                        point1 = point1 + save1
                        break 
                if point1 == 0:
                    print("You WON!")
                    break 

            while shot_counter2 != 0 and point1 != 0:

                if point2 > 0:
                    print("\n"*100)
                    print(f"\n{player2}'s turn! {shot_counter2} shot(s) remaining.\nYou have {point2} points!")
                    times = single_double_triple()
                    save2 = current_point() * times
                    point2 = point2 - save2
                    shot_counter2 -= 1
                    if point2 < 0:
                        point2 = point2 + save2
                        break
                if point2 == 0:
                    print("You WON!")
                    break

#3 players
    
    if player1 != "default" and player2 != "default" and player3 != "default" and player4 == "default":

        point2 = 301
        point1 = 301
        point3 = 301
        
        while point1 != 0 and point2 != 0 and point3 != 0:

            shot_counter1 = 3
            shot_counter2 = 3
            shot_counter3 = 3

            while shot_counter1 != 0 :

                if point1 > 0:
                    print("\n"*100)
                    print(f"\n{player1}'s turn! {shot_counter1} shot(s) remaining.\nYou have {point1} points!")
                    times = single_double_triple()
                    save1 = current_point() * times
                    point1 = point1 - save1
                    shot_counter1 -= 1
                    if point1 < 0:
                        point1 = point1 + save1
                        break
                if point1 == 0:
                    print("You WON!")
                    break 

            while shot_counter2 != 0 and point1 != 0:

                if point2 > 0:
                    print("\n"*100)
                    print(f"\n{player2}'s turn! {shot_counter2} shot(s) remaining.\nYou have {point2} points!")
                    times = single_double_triple()
                    save2 = current_point() * times
                    point2 = point2 - save2
                    shot_counter2 -= 1
                    if point2 < 0:
                        point2 = point2 + save2
                        break
                if point2 == 0:
                    print("You WON!")
                    break 

            while shot_counter3 != 0 and point1 != 0 or point2 != 0:

                if point3 > 0:
                    print("\n"*100)
                    print(f"\n{player3}'s turn! {shot_counter3} shot(s) remaining.\nYou have {point3} points!")
                    times = single_double_triple()
                    save3 = current_point() * times
                    point3 = point3 - save3
                    shot_counter3 -= 1
                    if point3 < 0:
                        point3 = point3 + save3
                        break
                if point3 == 0:
                    print("You WON!")
                    break 


#4 players

    if player1 != "default" and player2 != "default" and player3 != "default" and player4 != "default":

        point2 = 301
        point1 = 301
        point3 = 301
        point4 = 301
        
        while point1 != 0 and point2 != 0 and point3 != 0 and point4 != 0:

            shot_counter1 = 3
            shot_counter2 = 3
            shot_counter3 = 3
            shot_counter4 = 3

            while shot_counter1 != 0 :

                if point1 > 0:
                    print("\n"*100)
                    print(f"\n{player1}'s turn! {shot_counter1} shot(s) remaining.\nYou have {point1} points!")
                    times = single_double_triple()
                    save1 = current_point() * times
                    point1 = point1 - save1
                    shot_counter1 -= 1
                    if point1 < 0:
                        point1 = point1 + save1
                        break
                if point1 == 0:
                    print("You WON!")
                    break 

            while shot_counter2 != 0 and point1 != 0 :

                if point2 > 0:
                    print("\n"*100)
                    print(f"\n{player2}'s turn! {shot_counter2} shot(s) remaining.\nYou have {point2} points!")
                    times = single_double_triple()
                    save2 = current_point() * times
                    point2 = point2 - save2
                    shot_counter2 -= 1
                    if point2 < 0:
                        point2 = point2 + save2
                        break
                if point2 == 0:
                    print("You WON!")
                    break 

            while shot_counter3 != 0 and point1 != 0 and point2 != 0 :

                if point3 > 0:
                    print("\n"*100)
                    print(f"\n{player3}'s turn! {shot_counter3} shot(s) remaining.\nYou have {point3} points!")
                    times = single_double_triple()
                    save3 = current_point() * times
                    point3 = point3 - save3
                    shot_counter3 -= 1
                    if point3 < 0:
                        point3 = point3 + save3
                        break
                if point3 == 0:
                    print("You WON!")
                    break 

            while shot_counter4 != 0 and point1 != 0 and point2 != 0 and point3 != 0 :

                if point4 > 0:
                    print("\n"*100)
                    print(f"\n{player4}'s turn! {shot_counter4} shot(s) remaining.\nYou have {point4} points!")
                    times = single_double_triple()
                    save4 = current_point() * times
                    point4 = point4 - save4
                    shot_counter4 -= 1
                    if point4 < 0:
                        point4 = point4 + save4
                        break
                if point4 == 0:
                    print("You WON!")
                    break 





#Function that asks number of players
num_players = num_players()

#Variant that equals the players names (tuple)
name = players_name(num_players)

#The point counter
the_game(name[0], name[1], name[2], name[3])
