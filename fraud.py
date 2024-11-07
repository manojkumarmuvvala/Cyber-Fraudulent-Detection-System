import pickle
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
model1=pickle.load(open("detector.pkl","rb"))

def run():
    st.title("Online Payments Fraud Detection")
    step=st.number_input("Enter number of steps taken to perform the whole transaction")
    amount=st.number_input("Enter amount of the transaction.")
    old_src=st.number_input("Enter Balance of Origin account before the transaction")
    new_src=st.number_input("Enter Balance of Origin account after the transaction")
    old_dest=st.number_input("Enter Balance of Recipient account before the transaction")
    new_dest=st.number_input("Enter Balance of Recipient account after the transaction")
    payment = st.radio("Type of payment",['CASH_IN','CASH_OUT','DEBIT','PAYMENT','TRANSFER'])

    if payment=='CASH_IN':
        input=[step,amount,old_src,new_src,old_dest,new_dest,1,0,0,0,0]
    elif payment=='CASH_OUT':
        input=[step,amount,old_src,new_src,old_dest,new_dest,0,1,0,0,0]
    elif payment=='DEBIT':
        input=[step,amount,old_src,new_src,old_dest,new_dest,0,0,1,0,0]
    elif payment=='PAYMENT':
        input=[step,amount,old_src,new_src,old_dest,new_dest,0,0,0,1,0]
    elif payment=='TRANSFER':
        input=[step,amount,old_src,new_src,old_dest,new_dest,0,0,0,0,1]

    pred=st.button("Predict")

    if pred:
        output=model1.predict([input])
        if output>=0.5:
            st.write("Transaction is Fraud")
        else:
            st.write("Transaction is Legit")

run()