import streamlit as st
from auth import authenticate        #Function that checks username & password
from chatbot import get_ai_response     #Function that returns chatbot responses

    #Configure the Streamlit page (tab title & icon)
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")


#SESSION STATE INITIALIZATION


        #Track whether the user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

    #Store chat messages (user + assistant)
if "messages" not in st.session_state:
    st.session_state.messages = []


        #LOGIN SCREEN
#If user is NOT logged in, show the login UI
if not st.session_state.logged_in:
    st.title("🔐 Login")

            #Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

             #Login button
    if st.button("Login"):
                     #Check credentials using auth.py
        if authenticate(username, password):
            st.session_state.logged_in = True  #Update login state
            st.success("Login successful")
            st.rerun()  #reload the app to show chatbot UI
        else:
            st.error("Invalid credentials")

        # -------------------------------
        #CHATBOT SCREEN
        # -------------------------------

        #If my user IS logged in, show the chatbot UI
else:
    st.title("🤖 AI Chatbot")

             #Display previous messages from the session
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

            #Chat input box at the bottom of the page
    user_input = st.chat_input("Ask something...")

                #If the user submits a message
    if user_input:
             #Save user's message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

                #Generate assistant response
        with st.chat_message("assistant"):
            response = get_ai_response(st.session_state.messages)
            st.markdown(response)

                #Save assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

             # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False #Reset login state
        st.session_state.messages.clear() #Clear chat history
        st.rerun()  #Reload to login screen