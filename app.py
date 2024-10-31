import streamlit as st
from state1 import get_state1
from state2 import get_state2

 
# Set the page layout to wide
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .navbar {
        background-color: #4CAF50;
        overflow: hidden;
        margin-top: 20px; /* Add margin to create space between the button and the navbar */
    }
    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 20px 16px;
        text-decoration: none;
        font-size: 17px;
    }
    </style>
    <div class="navbar">
        <a href="#home"><img src="https://images.squarespace-cdn.com/content/v1/60d3cf6c4b8d584f9a248ddf/c0ee6c14-b1af-4169-8d8e-90cd525e21a6/3.png?format=1500w" alt="Logo" style="vertical-align:middle;"width="50" height="50"></a>
        <a href="#home">ROKPA</a>
    </div>
    """,
    unsafe_allow_html=True
)
# Create two columns for the buttons
state = 1
col1, col2, col3 = st.columns([1, 6, 1])

# Add buttons to the columns
st.write("         ")
with col1:
    if st.button('Home'):
        state = 1

        # Add a horizontal navbar for the logo and organization name
        

with col3:
    if st.button('Login'):
        state = 2




if state == 1:
    get_state1()
if state == 2:
    get_state2()
    
# Add some content to the main page
st.title("Welcome to the Webpage")
st.write("This is a simple webpage with Home and Login buttons.")