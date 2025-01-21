import streamlit as st
import requests

# -----------------------------
# 1) Page Config & Custom CSS
# -----------------------------
st.set_page_config(layout="wide")

# Custom CSS for vertical dividers, button styling, and overall UI improvements
custom_css = """
<style>
/* Vertical divider for columns */
.column-wrapper {
    border-right: 1px solid #ccc;
    padding-right: 20px;
}
.column-wrapper:last-child {
    border-right: none;  /* Remove right border on last column */
}

/* Style the "Ask" buttons */
div.stButton > button {
    background-color: #007acc;
    color: white;
    border-radius: 6px;
    border: 1px solid #005f99;
    padding: 0.5em 1em;
    cursor: pointer;
    font-size: 14px;
}
div.stButton > button:hover {
    background-color: #005f99;
}

/* Improve the appearance of the text input */
.css-16huue1.e1fqkh3o2 {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 10px;
    font-size: 16px;
}

/* Hide default horizontal lines for a cleaner layout */
hr {
    display: none !important;
}

/* Ensure the chat containers have a consistent look */
.chat-container {
    max-height: 450px;
    overflow-y: auto;
    background-color: #f9f9f9;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #e0e0e0;
    margin-bottom: 10px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------------------------------
# 2) Define the initial chat history (same for all 3 bots)
# -------------------------------------------------------
initial_chat_history = [
    
]

# -----------------------------------
# 3) Session State for Chat Histories
# -----------------------------------
if "col1_chatHistory" not in st.session_state:
    st.session_state["col1_chatHistory"] = initial_chat_history.copy()
if "col2_chatHistory" not in st.session_state:
    st.session_state["col2_chatHistory"] = initial_chat_history.copy()
if "col3_chatHistory" not in st.session_state:
    st.session_state["col3_chatHistory"] = initial_chat_history.copy()

# -----------------------------------
# 4) Session State for Base URL
# -----------------------------------
if "base_url" not in st.session_state:
    st.session_state["base_url"] = "http://127.0.0.1:8000"

# -------------------------------------------------------
# 5) Helper function to display chat messages
# -------------------------------------------------------
def display_chat(chat_history, container_id):
    """
    Display the conversation with assistant on the left,
    and user on the right using basic HTML alignment.
    """
    # Container for messages
    container_style = f"""
    <style>
    #{container_id} {{
        max-height: 450px;
        overflow-y: auto;
        background-color: #FFFFFF;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #e0e0e0;
        margin-bottom: 10px;
    }}
    </style>
    """
    st.markdown(container_style, unsafe_allow_html=True)
    
    # Open container div
    st.markdown(f"<div id='{container_id}'>", unsafe_allow_html=True)
    
    # Display each message
    for msg in chat_history:
        if msg["role"] == "assistant":
            st.markdown(
                f"<div style='text-align: left; background-color: #F0F0F0; "
                f"padding: 8px; margin: 5px 0; border-radius: 5px;'>"
                f"<b>Assistant:</b> {msg['content']}</div>",
                unsafe_allow_html=True
            )
        elif msg["role"] == "user":
            st.markdown(
                f"<div style='text-align: right; background-color: #D0F0FF; "
                f"padding: 8px; margin: 5px 0; border-radius: 5px;'>"
                f"<b>You:</b> {msg['content']}</div>",
                unsafe_allow_html=True
            )
    
    # Close container div
    st.markdown(f"</div>", unsafe_allow_html=True)

# -------------------------------------------------------
# 6) Function to update base_url
# -------------------------------------------------------
def update_base_url(new_url):
    if new_url:
        st.session_state["base_url"] = new_url
        st.success("API base URL updated successfully!")
    else:
        st.warning("Please enter a valid URL.")

# -------------------------------------------------------
# 7) Main Layout
# -------------------------------------------------------
st.title("Compare Chatbots Side by Side")

# -------------------------------------------------------
# 8) Input Section for API Base URL
# -------------------------------------------------------
st.markdown("### API Endpoint Configuration")

with st.form(key='base_url_form'):
    base_url_input = st.text_input(
        "Enter API base URL (e.g., http://127.0.0.1:8000 or https://<ngrok_link>):",
        value=st.session_state["base_url"]
    )
    submit_button = st.form_submit_button(label='Save')

    if submit_button:
        update_base_url(base_url_input)

st.markdown("---")
st.write(f"**Current API Base URL:** {st.session_state['base_url']}")

# -------------------------------------------------------
# 9) User input for the question
# -------------------------------------------------------
user_question = st.text_input("Enter your question:", "")

st.write("**Click one of the buttons below** to ask a single bot at a time.")

# Endpoints based on base_url
base_url = st.session_state["base_url"].rstrip('/')  # Remove trailing slash if any

url_nBot = f"{base_url}/chatbotazure/normal-bot-response/"
url_nBotMemory = f"{base_url}/chatbotazure/normal-bot-response-with-memory/"
url_hBot = f"{base_url}/chatbotazure/hybrid-bot-response/"

# ------------------------------
# Buttons to query each endpoint
# ------------------------------
col_button1, col_button2, col_button3 = st.columns(3)

# Flag to determine if any bot was asked
if 'asked_any_bot' not in st.session_state:
    st.session_state['asked_any_bot'] = False

with col_button1:
    if st.button("Ask Normal Bot"):
        st.session_state['asked_any_bot'] = True
        payload1 = {
            "question": user_question,
            "index_name": "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8",
            "chat_history": st.session_state["col1_chatHistory"]
        }
        try:
            response1 = requests.post(url_nBot, json=payload1)
            response1.raise_for_status()  # Raise exception for HTTP errors
            response1_data = response1.json()
            updated_chat_history1 = response1_data.get("chat_history", [])
            st.session_state["col1_chatHistory"] = updated_chat_history1
        except Exception as e:
            # Log error message in the chat as "assistant"
            st.session_state["col1_chatHistory"].append({
                "role": "assistant",
                "content": f"Error calling Normal Bot: {e}"
            })

with col_button2:
    if st.button("Ask Normal Bot + Memory"):
        st.session_state['asked_any_bot'] = True
        payload2 = {
            "question": user_question,
            "index_name": "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8",
            "chat_history": st.session_state["col2_chatHistory"]
        }
        try:
            response2 = requests.post(url_nBotMemory, json=payload2)
            response2.raise_for_status()
            response2_data = response2.json()
            updated_chat_history2 = response2_data.get("chat_history", [])
            st.session_state["col2_chatHistory"] = updated_chat_history2
        except Exception as e:
            st.session_state["col2_chatHistory"].append({
                "role": "assistant",
                "content": f"Error calling Normal Bot + Memory: {e}"
            })

with col_button3:
    if st.button("Ask Hybrid Bot"):
        st.session_state['asked_any_bot'] = True
        payload3 = {
            "question": user_question,
            "chat_history": st.session_state["col3_chatHistory"]
        }
        try:
            response3 = requests.post(url_hBot, json=payload3)
            response3.raise_for_status()
            response3_data = response3.json()
            updated_chat_history3 = response3_data.get("chat_history", [])
            st.session_state["col3_chatHistory"] = updated_chat_history3
        except Exception as e:
            st.session_state["col3_chatHistory"].append({
                "role": "assistant",
                "content": f"Error calling Hybrid Bot: {e}"
            })

# -------------------------------------------------------
# 10) Display the chat histories in 3 columns with borders
# -------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line before chat sections

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Normal Bot")
    display_chat(st.session_state["col1_chatHistory"], container_id="chat-container-1")

with col2:
    st.subheader("Normal Bot + Memory")
    display_chat(st.session_state["col2_chatHistory"], container_id="chat-container-2")

with col3:
    st.subheader("Hybrid Bot")
    display_chat(st.session_state["col3_chatHistory"], container_id="chat-container-3")

# -----------------------------------------
# 11) Auto-scroll to page bottom if needed
# -----------------------------------------
if st.session_state['asked_any_bot']:
    # Use a script to scroll to the bottom of the page
    scroll_script = """
    <script>
    window.scrollTo(0, document.body.scrollHeight);
    </script>
    """
    st.markdown(scroll_script, unsafe_allow_html=True)
    st.session_state['asked_any_bot'] = False  # Reset the flag
