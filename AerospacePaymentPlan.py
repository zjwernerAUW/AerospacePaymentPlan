import streamlit as st
import numpy as np


st.title("Aerospace Payment Plan Text Generator")

risktype = st.multiselect("Select The Risk Type:",["*Select*","Launch","In-Orbit"],key="risktype")

result = ""

if risktype == "Launch":
  with st.form(key="launchform"):
    despositPercent = st.number_input("Enter Deposit Percent: (If there is no deposit enter 0",0,100, step=0.1,key="launchdeposit")
    if depositPercent != 0:
      depositdue = st.date_input("Select Deposit Due Date",key="launchdepositdue")
      remainingDue = st.number_input("Enter How Many Days Before Launch Remaining Payment Is Due:",0,365,step = 1,key="launchremainingdue")
      totalDue = 0
    else:
      totalDue = st.number_input("Enter How Many Days Before Launch Payment Is Due:",0,365,step = 1,key='launchtotaldue')
    endorsementsCheck = st.checkbox("Select Checkbox If There Are Endorsements On This Spacecraft",False,key='endorsementcheck')
    if endorsementsCheck == True:
      endorsementpremium = st.number_input("Enter the Premium Amount Associated with the Endorsement:",-1000000,1000000,step = .01,key='endorsementpremium')
      endorsementduedate = st.date_input("Enter the Date Payment for the Endorsement is Due:",key='endorsementduedate')
  submitlaunch = st.form_submit_button("Generate",key="generatelaunch")

if submitlaunch == True:
  result = "L"
  if depositPercent == 0:
    result += f"1{endorsementCheck.map({True:'E:',False:'N:'})} 100% Due {totalDue} Days Before Launch"
  else:
    result += f"2{endorsementCheck.map({True:'E:',False:'N:'})} {(depositPercent/100):.2%} Due on {depositdue.strftime("%m/%d/%Y")}. {(1-(depositPercent/100)):.2%} Due {remainingDue} Days Before Launch"
  
  