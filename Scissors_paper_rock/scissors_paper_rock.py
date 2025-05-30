import random

def game():
    options = ["scissors ✂️", "paper 📃", "rock 🪨"]
    h_points = 0
    m_points = 0
    draw = 0
    m_choice = random.choice(options)
    h_choice_index = None
    n_iterations = None

    while True:
        try:
            n_iterations = int(input("Enter the number of rounds: "))
            if n_iterations <= 0 or n_iterations > 10:
                print("Out of range Number, number must be between 0 and 11.")
            else:
                break
        except(ValueError):
            print("!? Invaild Input, Enter a number between 3 and 10 .")

    for z in range(n_iterations):

        for choice in range(len(options)):
            print(f"({choice + 1})- {options[choice]}")

        while True:
            try:
                h_choice_index = input("choose from the options [ 1 , 2 , 3 ]: ")
                
                if h_choice_index.lower().strip() == "exit":
                    print("❗ Your choice is out of range !!!")
                    print("Try again with a vaild choice")
                elif int(h_choice_index) > 3 or int(h_choice_index) < 0:
                    print("# Game Terminated #")
                    quit()
                else:
                    break
            except(ValueError):
                print("❌ Invalid Input !!!, Enter a number from 1:3.")
        h_choice = options[int(h_choice_index) - 1]

        if h_choice == m_choice:
            print(" === Draw === ")
            draw += 1
            print(f"round {z+1} is draw")
        elif h_choice == "scissors ✂️" and m_choice == "paper 📃":
            print(f"Player wins round {z+1} ")
            h_points += 1
        elif h_choice == "paper 📃" and m_choice == "rock 🪨":
            print(f"Player wins round {z+1}")
            h_points += 1
        elif h_choice == "rock 🪨" and m_choice == "paper 📃":
            print(f"Player wins round {z+1}")
            h_points += 1
        else:
            print(f"Machine wins round {z+1}")
            m_points += 1
    return h_points, m_points, draw

def result(hp, mp, d):
    if hp > mp:
        result = f"🎉🎊 Player Wins 👨‍💻 🎉🎊"
    elif hp < mp:
        result = f"💻 Machine Wins 💻"
    else:
        result = f"♟️ === DRAW === ♟️"
    print("    ")
    print(f"* --#- Game Analysis -#-- *")
    print(f"Player Score = {hp}")
    print(f"Machine Score = {mp}")
    print(f"Draw times = {d}")
    return result

def main():

    print(" ### (Scissors, Paper, Rock) Game ### ".title())
    print("----" * 10)
    print("This will be a 10 times iteration Game, Then the result appers")
    print("you will first Enter the nubmer of rounds, then the games starts")
    print("In case you want to exit just type Exit instead of an option number")
    print("Have a good game 😉")
    print(" ")
    hp,mp,d = game()
    print(result(hp,mp,d))

main()