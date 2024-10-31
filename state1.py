# /Users/tenzindhonden/Desktop/RokpaWeb/state1.py

import streamlit as st


def get_state1():
    returnState1 = {
        
        st.title("This is the title for the Rokpa page. You are already logged in!"),
        st.write("There will be many other nights like this, where I'll be standing here with someone new"),
        st.write("There will be other songs to sing, another fall, another spring"),
        st.write("But there will never be another you"),
        st.write("There will be other lips that I may kiss, but they won't thrill me like yours used to do"),
        st.write("Yes, I may dream a million dreams, but how can they come true"),
        st.write("If there will never ever be another you"),
        st.write("There will be other lips that I may kiss, but they won't thrill me like yours used to do"),
        st.write("Yes, I may dream a million dreams, but how can they come true"),
        st.write("If there will never ever be another you"),
        st.write("If there will never ever be another you"),
        st.write("If there will never ever be another you"),
    }
    return returnState1

class State1:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"State name is {self.name}"