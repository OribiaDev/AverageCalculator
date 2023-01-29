import time

numberslist = []


def FirstCalculations():
    print("Please enter the first number of the list you would like to average")
    fnum = input()
    try:       
        fnum = int(fnum)
        numberslist.append(fnum)
        print("Added: " + str(fnum))
        time.sleep(0.5)
        ExtendedCalculations()

    except ValueError:
        try:
            fnum = float(fnum)
            numberslist.append(fnum)
            print("Added: " + str(fnum))
            time.sleep(0.5)
            ExtendedCalculations()
        except ValueError:
            print("Invalid Syntax | Please enter a number!")
            time.sleep(0.5)
            FirstCalculations()
            
    fnum = int(fnum)
    numberslist.append(fnum)
    print("Added: " + str(fnum))
    time.sleep(0.5)
    ExtendedCalculations()

def ExtendedCalculations():
    print("Please enter the next number \n If you're done with your list " + str(numberslist) + " enter 'done' \n If you would like to delete the last number in the list, enter 'delete'")
    num = input()
    if num == str("done"):
        numberlength = len(numberslist)
        numbertotal = sum(numberslist)
        average = numbertotal / numberlength
        print('Average: ' + str(average))
        exit()
    if num == str("delete"):
        if numberslist ==  []:
            print("There is no numbers in the list")
            time.sleep(0.5)
            ExtendedCalculations()
        del numberslist[-1]
        print("Deleted the last number in the list")
        time.sleep(0.5)
        ExtendedCalculations()
    
    try:       
        num = int(num)
        numberslist.append(num)
        print("Added: " + str(num))
        time.sleep(0.5)    
        ExtendedCalculations()

    except ValueError:
        try:
            num = float(num)
            numberslist.append(num)
            print("Added: " + str(num))
            time.sleep(0.5)
            ExtendedCalculations()
        except ValueError:
            print("Invalid Syntax | Please enter a number!")
            time.sleep(0.5)
            ExtendedCalculations()

FirstCalculations()

# If you see this, ur gay :3