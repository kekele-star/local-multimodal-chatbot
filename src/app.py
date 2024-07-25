# import streamlit
import streamlit as st
from llm_chains import load_chain

def load_chain():
    return load_normal_chain()

# Function to clear the input field and store the user input in session state
def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

# Function to set the 'send_input' flag to True and clear the input field
def set_send_input():
    st.session_state.send_input = True
    clear_input_field()

# Main function to run the Streamlit app
def main():
    st.title("WaterBits ChatApp")  # Set the title of the app
    chat_container = st.container()  # Create a container for the chat messages

    # Initialize session state variables if they don't exist
    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""

    # Text input field for the user to type their message
    user_input = st.text_input("Type your message here", key="user_input", on_change=set_send_input)

    # Button to send the message
    send_button = st.button("Send", key="send_button")

    # Check if the send button is pressed or if the input field change triggered sending
    if send_button or st.session_state.send_input:
        # Ensure that the user question is not empty
        if st.session_state.user_question != "":
            llm_response = "This is a response from the LLM model"  # Placeholder for the LLM response

            # Display the user's message and the response from the AI in the chat container
            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                st.chat_message("ai").write("here is an answer")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
