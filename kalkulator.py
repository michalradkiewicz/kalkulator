import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(action_text, number_1, number_2):

    if action_text == '1':
        logging.info("Dodaję = %s i %s" % (number_1, number_2))
        print("Wynik to")
        print(int(number_1) + int(number_2))
    elif action_text == '2':
        logging.info("Odejmuję = %s i %s" % (number_1, number_2))
        print("Wynik to")
        print(int(number_1) - int(number_2))
    elif action_text == '3':
        logging.info("Mnożę = %s i %s" % (number_1, number_2))
        print("Wynik to")
        print(int(number_1) * int(number_2))
    elif action_text == '4':
        logging.info("Dzielę = %s i %s" % (number_1, number_2))
        print("Wynik to")
        print(int(number_1) / int(number_2))

if __name__ == "__main__":
    if len(sys.argv) >=3:
        exit()
action_text = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
number_1 = input("Pierwszy argument = ")
number_2 = input("Drugi argument = ")
calculator(action_text, number_1, number_2)