import streamlit as st
st.balloons()
st.title("Hello , This Is My first App")
st.write("let us create app")
st.text_input("Please Enter your Name")
st.number_input("Please Enter your Marks")
x=st.radio("Are you working", options=["Yes","No"])
if x=="Yes":
    st.write("You can Choose Weekend Batch")
else:
    st.write("you can Choose Weekdays Batch")
st.sidebar.markdown("Test Results")
y = st.sidebar.checkbox("Are you Intrested in IT")
if y ==1:
    st.sidebar.write("You can opt Python Course")
else:
    st.sidebar.write("You Can Choose Another Courses")




