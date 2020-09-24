def computer_turn(boom, turn):
    if turn % boom == 0:
        print("boom")
    else:
        print(turn)

def xboom(x):
    is_computer_turn = False
    for i in range(1, 1000):
        if is_computer_turn:
           computer_turn(x, i)
           is_computer_turn = False
        else:
            user_input = input("Next Number: ")
            if i % x == 0:
                if user_input == "boom":
                    is_computer_turn = True
                    continue
                else:
                    print("Wrong Answer!")
                    break
            else:
                try:
                    if int(user_input) == i:
                        is_computer_turn = True
                        continue
                    else:
                        print("Wrong Answer!")
                        break
                except ValueError:
                   print("Wrong Answer!")
                   break

xboom(5)

#def user_turn(number, message, turn):
#   user_input = input(message)
#   if number % 7 == 0:
#        if user_input == "boom":
#            turn = not turn
#            continue
#   else:
#        if int(user_input) == i:
#           turn = not turn
#           continue
#       else:
#           print("Wrong number!")
#            break

#def game_over(message):
#    print(message)
#    break