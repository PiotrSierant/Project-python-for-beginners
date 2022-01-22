import calendar


def check_date(year):
    date = calendar.isleap(year)
    return printer_result(date, year)


def printer_result(result, year):
    try:
        if result == True:
            print("The year {} is leap!".format(year))
        elif result == False:
            print("The year {} isn't leap!".format(year))

    except:
        print('Oops, something went wrong!')


def input_date():
    try:
        x = int(input('Give the date: '))
        if x < 0:
            print('Please, take me the correct date! (The date must be not negative)')
            input_date()

        else:
            return check_date(x)

    except ValueError:
        print('Please, take me the correct date!')
        input_date()


input_date()
