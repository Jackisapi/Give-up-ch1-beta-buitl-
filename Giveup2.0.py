def game(decisiontext,outputtext1,outputtext2,outputtext3,decisionx,decisiony,decisionz,usrinput):
    usrinput = input(decisiontext)
    if usrinput == decisionx:
        print(outputtext1)
    elif usrinput == decisiony:
        print(outputtext2)
    elif usrinput == decisionz:
        print(outputtext3)
texttest = "This is text for a decision press 1 2 or 3"
testoutput1 = "This is output option 1"
testoutput2 = "The is output option 2"
testoutput3 = "This is output option 3"
option1 = "1"
option2 = "1"
option3 = "3"
decision = input()
game(texttest,testoutput1,testoutput2,testoutput3,option1,option2,option3,decision)