import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("outputLog.log"))


def fibonacciCount(number):
    first_number = 0
    second_number = 1

    while number > 0:
        first_number, second_number = second_number, first_number + second_number
        number -= 1

    return second_number


def main():
    logger.info(fibonacciCount(2))


if __name__ == "__main__":
    main()
