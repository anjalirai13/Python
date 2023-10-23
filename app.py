import logging
import random

def app():
    number1 = random.randint(1,100)
    number2 = random.randint(200,500)
    logging.info("number1: %s, number2: %s", number1, number2)
    ans = input("enter sum of {} and {}: ".format(number1, number2))
    logging.info("received answer: %s", ans)
    try:
        if int(ans) != number1+number2:
            raise ValueError
        logging.info("{} is the correct answer".format(ans))
    except (ValueError,TypeError):
        logging.info("{} is incorrect answer".format(ans))

def main():
    logging.basicConfig(level=logging.DEBUG, filename='log.log')
    for x in range(10):
        app()

if __name__ == '__main__':
    main()