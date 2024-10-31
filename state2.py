import streamlit as st
def get_state2():
    returnState2 = {
        st.title("This is the title for the Rokpa page, please login to continue"),
        st.write("Hello and welcome to Rokpa"),
        st.markdown("<h1 style='text-align: center; color: white;'>Log In</h1>", unsafe_allow_html=True)

    }
    return returnState2

class State2:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"State name is {self.name}"