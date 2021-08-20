'''
Name:Fahad Al summan
Job:Interview
'''


def checkFile():
    checkPomot = input('Does student submit the file correctly (\'insert 1 if he does  or 0 if doesn\'t) ?')
    if checkPomot.isnumeric():
        checkPomot = int(checkPomot)
    else:
        print('you must not enter string, you will start from the beginning!')
        return 0
    return checkPomot


def checkName():
    checkNameStudnet = input('Does student write his name (\'insert 1 if he does or 0 if doesn\'t)?')
    if checkNameStudnet.isnumeric():
        checkNameStudnet = int(checkNameStudnet)
    else:
        print('you must not enter string, you will start from the beginning!')
        return 0
    return checkNameStudnet


def checkHonorStatement():
    checkHonor = input('Does student write honor statement (\'insert 1 if he does or 0 if doesn\'t)?')
    if checkHonor.isnumeric():
        checkHonor = int(checkHonor)
    else:
        print('you must not enter string, you will start from the beginning!')
        return 0
    return checkHonor


def checkVideoYouTube():
    checkVideo = input('Does student upload video in the YouTube (\'insert 1 if he does or 0 if doesn\'t)?')
    if checkVideo.isnumeric():
        checkVideo = int(checkVideo)
    else:
        print('you must not enter string, you will start from the beginning!')
        return 0
    return checkVideo


def computingStudentScore():
    finalStudentScore = 0
    if checkFile() != 0:
        print('Student Upload correct file!!')
        pass
    else:
        finalStudentScore = 0
        print('Student don\'t upload correct file, and his final grade is ' + str(finalStudentScore))
        # return 0
        return finalStudentScore

    if checkName() != 0:
        print('Student wrote his name.')
        pass
    else:
        finalStudentScore = 0
        print('Student didn\'t  write his name , and his final grade is ' + str(finalStudentScore))
        return finalStudentScore

    if checkHonorStatement() != 0:
        print('Student wrote the honor statement.')
        pass
    else:
        finalStudentScore = 0
        print('The student didn\'t wrote the honor statement')
        return finalStudentScore

    if checkVideoYouTube() != 0:
        print('The student uploaded video on the YouTube ! ')
        pass
    else:
        print('The student did\'t upload  his video on the YouTube !and his final grade is ' + str(finalStudentScore))
        # finalStudentScore = 0  # Here I assign the score to 0 because of his grade will be ZERO.
        #return 0
        return finalStudentScore


def criteriaEvaluation():
    print('Is the code is correct, and it\'s meet all the given specification? ')
    correctCodeGrade = input('Enter the grade (from 0 to 10)')
    if correctCodeGrade.isnumeric():
        correctCodeGrade = int(correctCodeGrade)
    else:
        print("you must not enter string, you will start from the beginning")
        return 0
    if correctCodeGrade > 10:
        print('You enter more than expected..You will start from beginning!')
        return 0

    # Second criteria Evaluation
    print(
        'Is the code has an elegance? Such as (\data structure selection,algorithm efficiency, function implementation, etc) ')
    eleganceCode = input('Enter the grade (from 0 to 10)')
    if eleganceCode.isnumeric():
        eleganceCode = int(eleganceCode)
    else:
        print("you must not enter string, you will start from the beginning")
        return 0
    if eleganceCode > 10:
        print('You enter more than expected..You will start from beginning!')
        return 0
    # Third criteria Evaluation
    print('Is the code clean or hygiene ?')
    cleanCode = input('Enter the grade (from 0 to 10)')
    if cleanCode.isnumeric():
        cleanCode = int(cleanCode)
    else:
        print("you must not enter string, you will start from the beginning")
        return 0
    if cleanCode > 10:
        print('You enter more than expected..You will start from beginning!')
        return 0
    # Fourth criteria evaluation
    print('Is the student has a quality of the discussion in the YouTube video? ')
    qualityDiscuss = input('Enter the grade (from 0 to 10)')
    if qualityDiscuss.isnumeric():
        qualityDiscuss = int(qualityDiscuss)
    else:
        print("you must not enter string, you will start from the beginning")
        return 0
    if qualityDiscuss > 10:
        print('You enter more than expected..You will start from beginning!')
        return 0
    totalCriteriaEvaluationScore = [correctCodeGrade, eleganceCode, cleanCode, qualityDiscuss]
    print(totalCriteriaEvaluationScore)
    sumScoreTotal = sum(totalCriteriaEvaluationScore)
    # The Final Question
    isLate = eval(input('Does Student late to submit the assignment ? (you can use 1 to yes or 0 to no)'))
    if isLate != 0:
        timeLate = eval(input('Enter how much hour is late ?'))
        computingTotalScore = sumScoreTotal - (0.4 * timeLate)
        print('The Final  score is: ' + str(computingTotalScore))
        print('The Final  grade is:' + str((computingTotalScore / 40) * 100) + '%')
    else:
        finalScore = (sumScoreTotal / 40) * 100
        print('The Final  score is ' + str(sumScoreTotal) + '/40')
        print('The Final  grade is ' + str(finalScore) + '%')


if computingStudentScore() != 0:

    criteriaEvaluation()
else:
    pass
