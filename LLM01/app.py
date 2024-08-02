import streamlit as st
import model as md

st.title("Short Story Generator")
st.write("Create a shor story based on 5 simple descriptions.")

# Create 5 text inputs
character_descriptions = st.text_input("Describe your Character.")
goals = st.text_input("Describe the character's goal.")
dilemma = st.text_input("Describe the dilemma that the character is facing.")
decision = st.text_input("Describe the action that the character takes.")
outcome = st.text_input("Describe your desired ending.")

# Generate button
if st.button("Generate Story"):
    output = md.generateStory(character_descriptions, goals, dilemma, decision, outcome)
    st.write(output)