from datetime import datetime

risktype = 0 #setup risk type
result = "" #setup result
endorsementMap = {True:'E:',False:'N:'} #dictionary used for endorsements

while risktype == 0: #ensure risk type entered is correct
    riskcheck = int(input("Enter the value associated with the risk type: (1) Launch, (2) In-Orbit")) #user input risk type
    if riskcheck == 1 or riskcheck == 2:
        risktype = {1:"Launch",2:"In-Orbit"}[riskcheck] #convert to risk type

if risktype == "Launch": #if risk type is launch
  depositPercent = float(input("Enter Deposit Percent: (If there is no deposit enter 0. EX 10.0)")) #get the deposit amount associated with the launch risk
  if depositPercent != 0: #if deposit is non-zero
    depositdue = datetime.strptime(input("Select Deposit Due Date. Format MM/DD/YYYY"), '%m/%d/%Y') #get date the deposit is due
    remainingDue = int(input("Enter How Many Days Before Launch Remaining Payment Is Due")) #get the number of days pre launch the remaining premium is due
    totalDue = 0
  else: #if deposit is 0
    totalDue = int(input("Enter How Many Days Before Launch Payment Is Due:")) #get the number of days pre launch the premium is due
  endorsementsCheck = {0:False,1:True}[int(input("If There Are Endorsements On This Spacecraft, enter 1, if not enter 0"))] #check if there is an endorsement associated
  if endorsementsCheck: #if there is an endorsement
    endorsementpremium = float(input("Enter the Premium Amount Associated with the Endorsement: (Format ###.##)")) #dollar amount associated with endorsement
    endorsementduedate = input("Enter the Date Payment for the Endorsement is Due: (MM/DD/YYYY)") #date the payment for the endorsement is due
  if depositPercent == 0: # result if deposit is 0
    result = f"L1{endorsementMap[endorsementsCheck]} 100% Due {totalDue} Days Before Launch." + f"{f' END ${endorsementpremium:.2f} Due {endorsementduedate}' if endorsementsCheck else ''}"
  else: #result if deposit is non-zero
    result = f"L2{endorsementMap[endorsementsCheck]} {(depositPercent/100):.2%} Due on {depositdue.strftime('%m/%d/%Y')}. {(1-(depositPercent/100)):.2%} Due {remainingDue:02d} Days Before Launch." + f"{f' END ${endorsementpremium:,.2f} Due {endorsementduedate}' if endorsementsCheck else ''}"
  print(result) #return result
elif risktype == "In-Orbit": # if risk type is in-orbit
  orbitInstallments = int(input("Enter the Number of Installments There Will Be To Full Pay:")) #user input number of installments
  if orbitInstallments == 1: #if there is only one installment
    date1 = datetime.strptime(input("Select Date the Payment is Due (Format MM/DD/YYYY)"), '%m/%d/%Y') #date the single installment is due
    percent1 = 100
  else: #if there are multiple installments
    notequalinstallments = {0:False,1:True}[int(input("If Installments are NOT Equally Distributed, enter 1, otherwise enter 0"))] #check if installments are paid in equal portions
    for installment in range(orbitInstallments): #loop over number of installments
      exec(f'date{installment+1} = datetime.strptime(input("Select Date for Installment {installment+1} (Format MM/DD/YYYY)"),"%m/%d/%Y")') #date identified installment is due
      if notequalinstallments: #if installments are not paid equally
        exec(f'percent{installment+1} = float(input("Select Percent Allocated to Installment {installment+1}"))') #user input percent of total premium associated with identified installment
      else: #if installments are paid equally
        exec(f'percent{installment+1} = float({100/orbitInstallments})') 
  endorsementsCheck = {0:False,1:True}[int(input("If There Are Endorsements On This Spacecraft, enter 1, othewise enter 0"))] #check if endorsement present
  if endorsementsCheck: #if endorsement
    endorsementpremium = float(input("Enter the Premium Amount Associated with the Endorsement: (Format ###.##)")) #premium associated with endorsement
    endorsementduedate = input("Enter the Date Payment for the Endorsement is Due: (Format MM/DD/YYYY)") #date endorsement premium is due
  result = f"O{orbitInstallments:02d}{endorsementMap[endorsementsCheck]} Payment 1: {date1.strftime('%m/%d/%Y')} @ {(percent1/100):.2%}" #start of result based on single installment
  sumofpercentages = percent1
  percent = 0
  date = "01/01/1900"
  for installment in range(orbitInstallments): # if more installments, add data to result
    if installment !=0: #skip installment 0
      exec(f"date = date{installment+1}")
      exec(f"percent = percent{installment+1}")
      sumofpercentages += percent
      result += f", Payment {installment+1}: {date.strftime('%m/%d/%Y')} @ {percent/100:.2%}" #concatenate data to result
    if installment == orbitInstallments-1: #if endorsement present
      result += f"{f'. END ${endorsementpremium:,.2f} Due {endorsementduedate}' if endorsementsCheck else '.'}" #concatenate endorsement data to result
  if round(sumofpercentages,2) == 100: #check that total of all endorsement equals 100%
    print(result) #if 100%, return result
  else:
    print("Percentages Do Not Equal 100%") #if not 100% return error.