import streamlit as st
import requests

def get_random_trivia():
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = response.json()
    question = data["results"][0]["question"]
    options = data["results"][0]["incorrect_answers"]
    correct_option = data["results"][0]["correct_answer"]
    options.append(correct_option)
    options.sort()
    return question, options, correct_option

def main():
    st.title("Random Trivia Quiz")
    st.write("Test your knowledge with random trivia questions!")

    question, options, correct_option = get_random_trivia()

    st.write(question)

    selected_option = st.selectbox("Select an option", options)

    if selected_option == correct_option:
        st.write("Correct answer!")
    else:
        st.write("Incorrect answer. The correct answer is:", correct_option)

if __name__ == "__main__":
    main()
