#Tired of the system on the cash register I work with.
#A customer gives me an amount of money, and lists a currency amount they want in the change.
#This function will create change from 20 bills to the lower parameter given.
#current function designed with USD in mind
def changeWMin(amount, smallest):
    #listing out the different currency amounts and how many of each to return
    amtList = [20,10,5,1,.25,.1,.05,.01]
    returnList = [0, 0, 0, 0, 0, 0, 0, 0]

    #take the total amount, and remove the requested amount from a customer
    if smallest == "ten":
        if amount >= 10:
            amount-=10
            returnList[1]+=1
    elif smallest == "five":
        if amount >= 5:
            amount -= 5
            returnList[2]+=1
    elif smallest == "one":
        if amount >= 1:
            amount -=1
            returnList[3]+=1
    elif smallest == "quarter":
        if amount >= .25:
            amount -= .25
            returnList[4] +=1
    elif smallest == "dime":
        if amount >= .1:
            amount -= .1
            returnList[5] +=1
    elif smallest == "nickel":
        if amount >= .05:
            amount -= .05
            returnList[6] +=1
    elif smallest == "penny":
        if amount >= .01:
            amount -= .01
            returnList[7] +=1
    #make exact change with the rest
    returnList=exactChange(amount, amtList, returnList)
    return returnList
#function to turn any amount into any currency based on inputted list
def exactChange(start, currencyVal, change=[0,0,0,0,0,0,0,0]):
    for i in range(len(currencyVal)):
        while start>= currencyVal[i]:
            change[i]+=1
            #rounding off to prevent any calculation errors
            #no current currency requires more than two digits past the decimal point anyway
            start = round( start -currencyVal[i], 2)
    return change

#simple tip calculator
def tipCalc(total, tipPercent):
    tip = total*(tipPercent/100)
    print("You will be adding "+str(round(tip,2))+" to your check")
    print("Your total bill will be "+ str(round((tip+total),2)) +".")

