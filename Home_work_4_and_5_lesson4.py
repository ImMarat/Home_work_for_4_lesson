from Utils_for_Lesson4 import currency_rates
import sys
if __name__ == '__main__':
    valute_name = sys.argv
    print(currency_rates(valute_name))