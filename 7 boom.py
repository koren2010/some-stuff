is_computer_turn = False

for i in range(1, 51):
    if is_computer_turn:
        if i % 7 == 0:
           print("boom")
        else:
            print(i)
        is_computer_turn = False

    else:
        entered_number = input("Next Number: ")
        if i % 7 == 0:
            if entered_number == "boom":
                is_computer_turn = True
                continue
        else:
            if int(entered_number) == i:
                is_computer_turn = True
                continue
            else:
                print("Wrong number!")
                break



