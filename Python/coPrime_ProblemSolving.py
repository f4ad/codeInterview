'''
Name:Fahad Al summan
job: interviewAthar
'''


#This function will ask from  users many times to enter two integers until user enter 0. Also, this function will pass two numbers to next function coprime() function
def coprime_test_loop():

    while True:
        continueCount = eval(input('Do you want to exit ? press 0 if you want to continue press 1 '))
        if continueCount == 0:
            print('GoodBye!')
            break
        number1 = input('Enter the first number please? ')
        if number1.isnumeric():
            number1=int(number1)
        else:
            print('you must enter integer number')
            break
        number2 = input('Enter the second number please? ')
        if number2.isnumeric():
            number2=int(number2)
        else:
            print('you must enter integer number')
            break
        coprime(number1, number2)

# this Function will take two values from previous function
def coprime(firstNumber,secondNumber):
    # I define factor1 and factor2 to get factor number !20
    factorNumber1 = []
    factorNumber2 = []
    #to store similar integers in these factor to get the result of coprime
    simmilarNum = []
    for ai in range(1, firstNumber + 1):  # ai to store the data which come from first number that user input iterate
        if firstNumber % ai == 0:
            factorNumber1.append(ai)

    for bi in range(1, secondNumber + 1):  # bi to store the data which come from second number that user input iterate
        if secondNumber % bi == 0:
            factorNumber2.append(bi)

    for fact1 in factorNumber1:
        for fact2 in factorNumber2:
            if fact1 == fact2:
                simmilarNum.append(fact1)
    print('Factor for first number = ' + str(factorNumber1))
    print('Factor for second number= ' + str(factorNumber2))
    print('These two numbers have similar in = ' + str(simmilarNum))

    if len(simmilarNum) > 1:
        print('Not Coprime')
    elif len(simmilarNum) == 1:
        if 1 in simmilarNum:
            print('Coprime!!')
        else:
                print('Not-coprime')

coprime_test_loop()

