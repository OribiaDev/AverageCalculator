numberslist = []
#beta

def FirstCalculations():
    print("To calculate an average of a set of numbers, please enter the first number below")
    fnum = input()
    try:       
        fnum = int(fnum)
        numberslist.append(fnum)
        print("Added: " + str(fnum))
        ExtendedCalculations()

    except ValueError:
        try:
            fnum = float(fnum)
            numberslist.append(fnum)
            print("Added: " + str(fnum))
            ExtendedCalculations()
        except ValueError:
            print("Im sorry, you cannot input a string, try again!")
            FirstCalculations()
            
    fnum = int(fnum)
    numberslist.append(fnum)
    print("Added: " + str(fnum))
    ExtendedCalculations()

def ExtendedCalculations():
    print("Please enter the next number! | If you're done with your list (" + str(numberslist) + ") enter 'done' | If you would like to delete the last number in the list, enter 'delete'")
    num = input()
    if num == str("done"):
        numberlength = len(numberslist)
        numbertotal = sum(numberslist)
        average = numbertotal / numberlength
        print('Okay, heres your average: ' + str(average))
        exit()
    if num == str("delete"):
        del numberslist[-1]
        print("Deleted the last number in the list!")
        ExtendedCalculations()
    
    try:       
        num = int(num)
        numberslist.append(num)
        print("Added: " + str(num))
        ExtendedCalculations()

    except ValueError:
        try:
            num = float(num)
            numberslist.append(num)
            print("Added: " + str(num))
            ExtendedCalculations()
        except ValueError:
            print("Im sorry, that is not a valid option, please try again!")
            ExtendedCalculations()

FirstCalculations()