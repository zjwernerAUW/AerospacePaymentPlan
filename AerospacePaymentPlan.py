import streamlit as st
import numpy as np


st.title("Aerospace Payment Plan Text Generator")

risktype = st.selectbox("Select The Risk Type:",["*Select*","Launch","In-Orbit"],key="risktype")

result = ""
endorsementMap = {True:'E:',False:'N:'}

if risktype == "Launch":
  depositPercent = st.number_input("Enter Deposit Percent: (If there is no deposit enter 0)",0.0,100.0, step=0.1,key="launchdeposit")
  if depositPercent != 0:
    depositdue = st.date_input("Select Deposit Due Date",key="launchdepositdue")
    remainingDue = st.number_input("Enter How Many Days Before Launch Remaining Payment Is Due:",0,365,step = 1,key="launchremainingdue")
    totalDue = 0
  else:
    totalDue = st.number_input("Enter How Many Days Before Launch Payment Is Due:",0,365,step = 1,key='launchtotaldue')
  endorsementsCheck = st.toggle("Select Checkbox If There Are Endorsements On This Spacecraft",False,key='endorsementcheck')
  if endorsementsCheck:
    endorsementpremium = st.number_input("Enter the Premium Amount Associated with the Endorsement:",-1000000.00,1000000.00,value = 0.00,step = .01,key='endorsementpremium')
    endorsementduedate = st.date_input("Enter the Date Payment for the Endorsement is Due:",key='endorsementduedate')
  submitlaunch = st.button("Submit",key='submitlaunch')
  if submitlaunch:
    if depositPercent == 0:
      result = f"L1{endorsementMap[endorsementsCheck]} 100% Due {totalDue} Days Before Launch." + f"{' END ${endorsementpremium:.2f} Due {endorsementduedate}' if endorsementsCheck else ''}"
    else:
      result = f"L2{endorsementMap[endorsementsCheck]} {(depositPercent/100):.2%} Due on {depositdue.strftime('%m/%d/%Y')}. {(1-(depositPercent/100)):.2f} Due {remainingDue} Days Before Launch." + f"{' END ${endorsementpremium:.2f} Due {endorsementduedate}' if endorsementsCheck else ''}"
    st.divider()
    st.header(result)
    
  
