import google.generativeai as genai
import streamlit as st

# Configure Google Generative AI
genai.configure(api_key="AIzaSyDw7UsYFZcNHBdvm7cGiV1ZSv7zbOi9Ck0")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Set the title and description
st.title("⚜️ Simple Chatbot ⚜️")
st.write("Powered By GOOGLE Generative AI")

# User input form
with st.form(key="Chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message...", max_chars=2000, key="input")
    if st.form_submit_button("Send"):
        if user_input:
            response = model.generate_content(user_input).text
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please enter a prompt.")


# Display chat history
if st.session_state.history:
    st.write("### Chat History:")
    for user_msg, bot_msg in st.session_state.history:
        # Style user messages
        st.markdown(
            f"""
            <div style='background-color: #e0f7fa; padding: 10px; margin: 5px 0; border-radius: 8px;'>
                <strong>You:</strong> {user_msg}
            </div>
            """,
            unsafe_allow_html=True
        )
        # Style bot messages
        st.markdown(
            f"""
            <div style='background-color: #ffe0b2; padding: 10px; margin: 5px 0; border-radius: 8px;'>
                <strong>Bot:</strong> {bot_msg}
            </div>
            """,
            unsafe_allow_html=True
        )

# Add a footer for a personal touch
st.markdown("<footer style='text-align: center; padding: 10px;'>Created 💙 by [Fatima Ashraf]</footer>", unsafe_allow_html=True)

# Add custom CSS for better styling
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)
