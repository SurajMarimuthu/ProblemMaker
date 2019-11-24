import os
import operator as op
import random

completed = {"addition": False, "subtraction": False, "multiplication": False, "division": False}
math_dict = {"addition": op.add, "subtraction": op.sub, "multiplication": op.mul, "division": op.truediv}



def main():
    print("""Welcome to the best math game on the planet!!!!!
If you want to win this game and beat the system, do the following:
\t*Don't slack off
\t*Stay focused and pay attention 
\t*Take your time for each question, remember that this is just a game; you don't necessarily have to try hard
Stay focused! If you answer any questions incorrectly for a stage, you will have to restart that whole stage again!
The questions will get harder as you advance further.""")


    input("To start please press enter")
    clear_screen()

    print("Good Luck.")
    begin_math_stage()

    print("You have reached the end! Good Job!")


def display_incomplete_stages():
    for stage, status in completed.items():
        if not status:
            print("\t*{}".format(stage))


def begin_math_stage():
    display_incomplete_stages()
    stage = input("Please choose a stage:\n> ").strip().lower()

    try:
        if not completed[stage]:
            math_stage(stage)
    except KeyError:
        print("{} is not a valid choice.".format(stage))
        begin_math_stage()


def math_symbol(choice):
    if choice == "addition":
        return "+"
    elif choice == "subtraction":
        return "-"
    elif choice == "multiplication":
        return "*"
    elif choice == "division":
        return "/"


def math_stage(stage):
    print("You have entered the {} room.".format(stage))
    print("You will now have to answer the following questions.")

    input("To start please press enter")

    for question in range(1, 6):
        num1 = random.randint(0, 25)
        num2 = random.randint(0, 25)

        if num1 < num2:
            num1, num2 = num2, num1

        while True:
            try:

                user_answer = float(input(
                    "Question number {}: What is {} {} {}: ".format(question, num1, math_symbol(stage), num2)))
                break
            except TypeError:
                print("Wrong, try again! Don't Give up.\n> ")

        if round(math_dict[stage](num1, num2), 1) != user_answer:
            print("Incorrect! This the right answer was {}".format(num1 * num2))
            math_stage(stage)

    print("{} has been finished!".format(stage))
    completed[stage] = True

    if not stages_complete():
        begin_math_stage()
    else:
        return False


def stages_complete():
    for status in completed.values():
        if not status:
            return False

    return True



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")



if __name__ == "__main__":
    main()



    # Math game made in python, this can be used for kids through the ages of 5-10.
    # This game can help kids sharpen their basic arithmetical skills.
    #Including multiplication,addition,subtraction, and division.