# import packages
import streamlit as st # for frontend design 
import numpy as np # use for scintific caculation
import pandas as pd # use for data analysis

st.title("Hello , streamlit")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets go started")
st.write("my name is Ayush") 

# conditional logic
name = st.text_input("Enter Your Name :")
if st.button("Greet"):
    st.success(f"Hello {name}")

#Display data and charts
df = pd.DataFrame(np.random.randn(11, 2), columns=["A","B"])
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

#File uploading and caching
upload_file = st.file_uploader("Upload File", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

# all the userinteface of streamlit
st.header("this is a header")
st.subheader("this is sub header")
st.markdown("**Bold**, **Italic*,[Link](https://www.helpdesk.com/)")
st.text_area("Write your message")
st.number_input("pick a number", min_value=0, max_value=100)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["Apple","Mango"])
st.multiselect("choose toppings",["cheese","Tomato"])
st.radio("pick one",["option A","option B"])
st.checkbox("I agree terms and condition")
st.toggle("Turn ON/OFF")
st.button("Submit")
st.date_input("Select a date")
st.color_picker("Pick a color")

# form code 
with st.form("Login Form"):
    username = st.text_input("username")
    password = st.text_input("password", type="password")
    submitted = st.form_submit_button("login")

    if submitted:
        st.success(f"welcome,{username}")

# check radio button 
option = st.radio("Choose View",["Show chart","Show Table"])
if option == "Show chart":
    st.write("Chart would be appear heare")
else:
    st.write("Table would be appear heare")

if st.checkbox("Show details"):
    st.info("here are more details")

#Media layout and advanced widget
st.sidebar.title("New chart")
st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c")
st.video("https://www.youtube.com/watch?v=qEngZ4D0r6k")

import streamlit as st

st.title("Chat History")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# New chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Simple response
    response = f"You said: {prompt}"

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)
 