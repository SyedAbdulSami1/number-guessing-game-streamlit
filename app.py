import streamlit as st
import random

if "random_number" not in st.session_state:
    st.session_state.random_number= random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 5

st.title("Guessing Number Game")
st.write("I have a number between 1 and 100. Can you guess it?")
st.write(F"Attempts left: , {st.session_state.attempts} / 5")

upper_suggession = st.session_state.random_number + random.randint(2, 10)
lower_suggession = st.session_state.random_number - random.randint(2, 10)

guess = st.number_input("Enter your guess", min_value=1, max_value=100, value=50)

if st.button("Submit"):
    if st.session_state.attempts ==0:
        st.write(f"Game Over, Please Try Again. The number was {st.session_state.random_number}")
    else:
        st.session_state.attempts -= 1
        if guess < st.session_state.random_number:
            st.write("Too Low")
            st.write(f"Hint: Try a number between {lower_suggession} and {upper_suggession}")
        elif guess > st.session_state.random_number:
            st.write("Too High")
            st.write(f"Hint: Try a number between {lower_suggession} and {upper_suggession}")
        else:
            st.success("Congratulations! You have guessed the number")
            st.balloons()
if st.button("Reset Game"):
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 5
st.write("Created by: Syed Abdul Sami")