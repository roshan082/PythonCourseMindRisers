# Case Study -- my purse CLI

# 1. Money Deposit
# 2. total balance
# 3. Interest
# 4. deduction
# 5. trial balance

totalBalance = 0
deposite = 0
interest = 6.5
withdrawn = 0
trialBalance = 0

dayDp = []
dayWt = []
dayTb = []
# week  one calculation
deposit = 500
withdrawn = 0
totalBalance += (deposit - withdrawn)
dayCount = 1 
# day = [totalBalance]

# here append is a method of list which adds items at the last index of the list..
dayDp.append(deposit)
dayWt.append(withdrawn)
dayTb.append(totalBalance)

print("Day 1 Balance check")

print("Deposit: ", dayDp[dayCount - 1])
print("Total Withdrawn: ", dayWt[dayCount - 1])
print("Day One Collection: ", dayTb[dayCount - 1])
dayCount +=1
print("-------------------------------------")
#Day 2
deposit = 800
withdrawn = 150
totalBalance += (deposit - withdrawn)

dayDp.append(deposit)
dayWt.append(withdrawn)
dayTb.append(totalBalance)

print("Day 2 Balance check")
print("Deposit: ", dayDp[dayCount - 1])
print("Total Withdrawn: ", dayWt[dayCount - 1])
print("Day One Collection: ", dayTb[dayCount - 1])
dayCount +=1
print("-------------------------------------")

#Day 3
deposit = 250
withdrawn = 50
totalBalance += (deposit - withdrawn)

dayDp.append(deposit)
dayWt.append(withdrawn)
dayTb.append(totalBalance)

print("Day 3 Balance check")
print("Deposit: ", dayDp[dayCount - 1])
print("Total Withdrawn: ", dayWt[dayCount - 1])
print("Day One Collection: ", dayTb[dayCount - 1])
print("-------------------------------------")


# day 3 Interest rate

ir = interest
ia = ir/12 #rate per month
iad = (ia/30) * dayCount # day 3 interest rate
amount = (totalBalance * iad) / 100 # day 3 interest amount
totalBalance += amount
dayTb.append(totalBalance)

print("Day 3 Balance check after interest rate")
print("Deposit: ", dayDp[dayCount - 1])
print("Total Withdrawn: ", dayWt[dayCount - 1])
print("Day One Collection: ", dayTb[dayCount]) # no need dayCount - 1 because interest should be shown of current day
print("Interest rate: ", ir)
print("Interest amount: ", amount)

print("-------------------------------------")

dayCount +=1
