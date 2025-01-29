# import streamlit as st
# import requests
# import json

# # -----------------------------
# # 1) Page Config & Custom CSS
# # -----------------------------
# st.set_page_config(layout="centered")

# # Custom CSS for styling the UI components
# custom_css = """
# <style>
# /* Style the "Ask" button */
# div.stButton > button {
#     background-color: #007acc;
#     color: white;
#     border-radius: 6px;
#     border: 1px solid #005f99;
#     padding: 0.5em 1em;
#     cursor: pointer;
#     font-size: 14px;
# }
# div.stButton > button:hover {
#     background-color: #005f99;
# }

# /* Style the "Clear Chat" button */
# div.stButton > button.clear-chat {
#     background-color: #e63946;
#     color: white;
#     border-radius: 6px;
#     border: 1px solid #d62828;
#     padding: 0.3em 0.8em;
#     cursor: pointer;
#     font-size: 12px;
# }
# div.stButton > button.clear-chat:hover {
#     background-color: #d62828;
# }

# /* Improve the appearance of the text input */
# .css-16huue1.e1fqkh3o2 {
#     border: 1px solid #ccc;
#     border-radius: 4px;
#     padding: 10px;
#     font-size: 16px;
# }

# /* Hide default horizontal lines for a cleaner layout */
# hr {
#     display: none !important;
# }

# /* Ensure the chat container has a consistent look */
# .chat-container {
#     max-height: 600px;
#     overflow-y: auto;
#     background-color: #f9f9f9;
#     padding: 20px;
#     border-radius: 10px;
#     border: 1px solid #e0e0e0;
#     margin-bottom: 20px;
# }

# /* Style for the JSON view icon */
# .json-icon {
#     cursor: pointer;
#     font-size: 16px;
#     margin-left: 10px;
#     color: #555;
# }
# .json-icon:hover {
#     color: #000;
# }

# /* Style for the expanders */
# .streamlit-expanderHeader {
#     font-weight: bold;
#     font-size: 16px;
#     color: #333;
# }
# </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

# # -------------------------------------------------------
# # 2) Session State for Chat History
# # -------------------------------------------------------
# if "hybrid_chatHistory" not in st.session_state:
#     st.session_state["hybrid_chatHistory"] = []

# # -----------------------------------
# # 3) Session State for JSON Popups
# # -----------------------------------
# if "json_popups" not in st.session_state:
#     st.session_state["json_popups"] = {}  # Dictionary to store which messages have JSON popups open

# # -------------------------------------------------------
# # 4) Helper Function to Display Chat Messages
# # -------------------------------------------------------
# # -------------------------------------------------------
# # 4) Helper Function to Display Chat Messages
# # -------------------------------------------------------
# def display_chat(chat_history):
#     """
#     Display the conversation with the assistant.
#     Shows the final output and provides expandable sections for top references.
#     """
#     # Container for messages
#     container_style = """
#     <style>
#     .chat-container {
#         max-height: 600px;
#         overflow-y: auto;
#         background-color: #f9f9f9;
#         padding: 20px;
#         border-radius: 10px;
#         border: 1px solid #e0e0e0;
#         margin-bottom: 20px;
#     }
#     </style>
#     """
#     st.markdown(container_style, unsafe_allow_html=True)
    
#     # Open container div
#     st.markdown(f"<div class='chat-container'>", unsafe_allow_html=True)

#     # Display each message
#     for idx, msg in enumerate(chat_history):
#         if msg["role"] == "assistant":
#             # Display assistant message (final_output)
#             st.markdown(
#                 f"""
#                 <div style='text-align: left; background-color: #F0F0F0; 
#                 padding: 15px; margin: 10px 0; border-radius: 8px;'>
#                     <b>Assistant:</b> {msg['content']}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
            
#             # Check if 'full_response' exists and contains 'top_references'
#             full_response = msg.get("full_response", {})
#             # st.markdown(full_response)
#             top_references = full_response.get("top_references", [])
#             sources = full_response.get("source", [])
#             page_nos = full_response.get("pageNos", [])

#             if top_references and sources and page_nos:
#                 # Ensure all lists are of the same length
#                 if len(top_references) == len(sources) == len(page_nos):
#                     with st.expander("🔍 Top References"):
#                         for i in range(len(top_references)):
#                             st.markdown(
#                                 f"**Reference {i+1}:** {top_references[i]}<br>"
#                                 f"*Source:* `{sources[i]}` | *Page:* {page_nos[i]}",
#                                 unsafe_allow_html=True
#                             )
#                             st.markdown("---")
#                 else:
#                     # Handle mismatched list lengths
#                     st.warning("Warning: The lengths of 'top_references', 'source', and 'pageNos' do not match.")
#             else:
#                 st.info("No additional references available.")
        
#         elif msg["role"] == "user":
#             # Display user message
#             st.markdown(
#                 f"""
#                 <div style='text-align: right; background-color: #D0F0FF; 
#                 padding: 15px; margin: 10px 0; border-radius: 8px;'>
#                     <b>You:</b> {msg['content']}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#     # Close container div
#     st.markdown(f"</div>", unsafe_allow_html=True)

# # -------------------------------------------------------
# # 5) Function to Update Base URL (Remove trailing '/')
# # -------------------------------------------------------
# def update_base_url(new_url):
#     if new_url:
#         # Remove trailing slash if present
#         clean_url = new_url.rstrip("/")
#         st.session_state["base_url"] = clean_url
#         st.success(f"API base URL updated successfully to: {clean_url}")
#     else:
#         st.warning("Please enter a valid URL.")


# # -------------------------------------------------------
# # 6) Main Layout
# # -------------------------------------------------------
# st.title("Hybrid Bot Chat Interface")

# # -------------------------------------------------------
# # 7) Input Section for API Base URL
# # -------------------------------------------------------
# st.markdown("### API Endpoint Configuration")

# with st.form(key='base_url_form'):
#     base_url_input = st.text_input(
#         "Enter API base URL (e.g., http://127.0.0.1:8000 or https://<ngrok_link>):",
#         value=st.session_state.get("base_url", "http://127.0.0.1:8000")
#     )
#     submit_button = st.form_submit_button(label='Save')

#     if submit_button:
#         update_base_url(base_url_input)

# st.markdown("---")
# st.write(f"**Current API Base URL:** {st.session_state.get('base_url', 'Not Set')}")

# # -------------------------------------------------------
# # 8) User Input for the Question
# # -------------------------------------------------------
# user_question = st.text_input("Enter your question:", "")

# st.markdown("### Ask the Hybrid Bot")

# # Endpoint for Hybrid Bot
# base_url = st.session_state.get("base_url", "http://127.0.0.1:8000").rstrip('/')  # Remove trailing slash if any
# url_hBot = f"{base_url}/chatbotazure/hybrid-bot-response/"

# # Button to query the Hybrid Bot
# if st.button("Ask Hybrid Bot"):
#     if user_question.strip() == "":
#         st.warning("Please enter a question before asking the bot.")
#     else:
#         # Append user message to chat history
#         st.session_state["hybrid_chatHistory"].append({
#             "role": "user",
#             "content": user_question
#         })

#         payload = {
#             "question": user_question,
#             "chat_history": st.session_state["hybrid_chatHistory"],
#             "index_name": "358deb70-f5fb-441b-94f5-aac63e574a99",
#             "prompt":"You are a helpful assistant working for Bajaj Allianz Life Insurance Company also known as Bajaj Allianz. Use the question, source documents, and the conversation history to answer the question in a conversational manner. If any information is missing in the question, ask a followup question to get those values before any calculations. Your role is to provide accurate, concise answers about Bajaj Allianz products, services, and internal content. You cannot take independent actions; you may only respond to questions and offer guidance. You will always stay in your character no matter what. Respond in the language in which user asked the question. If the user asked the question in English, respond strictly in English. If the user asked the question in Hinglish, respond in Hinglish. Do not exceed 50 words in your initial response. If the user asks for more details, expand your response for up to 150 words. While replying in Hinglish, make sure translation is context-aware and spoken as a female. Answer strictly based on the provided context. Do not incorporate information from outside sources or hallucinate. For questions that are too general, ask follow-up questions to gain clarity and then respond with an appropriate answer. For unrelated questions: 'I'm here to assist with Bajaj Allianz Life-related questions. Let me know if there's something specific about Bajaj Allianz Life I can help with.' For inappropriate language: 'I'm here to provide helpful support. Let's keep our conversation positive. How can I assist you with Bajaj Allianz Life offerings?' Answer the question based on the relevant chunks and tables retrieved. First, see if the chunks and tables answer the sub-questions properly, then only answer the main question using the answers for sub-questions. Finally answer the main question only.",
#             "language":"English"
#         }
#         with st.spinner("Waiting for the Hybrid Bot to respond... max 13 sec"):
#             try:
#                 response = requests.post(url_hBot, json=payload)
#                 response.raise_for_status()  # Raise exception for HTTP errors
#                 response_data = response.json()
#                 final_output = response_data.get("final_output", "")
#                 top_references = response_data.get("top_references", [])
#                 updated_chat_history = response_data.get("chat_history", [])

#                 # Append the assistant message with full_response
#                 st.session_state["hybrid_chatHistory"].append({
#                     "role": "assistant",
#                     "content": final_output,
#                     "full_response": response_data  # Store the entire response as full_response
#                 })

#             except Exception as e:
#                 # Log error message in the chat as "assistant"
#                 st.session_state["hybrid_chatHistory"].append({
#                     "role": "assistant",
#                     "content": f"❌ Error: Unable to reach the Hybrid Bot. Please try again later.",
#                     "full_response": {}
#                 })
#                 st.error(f"An error occurred: {e}")

# # -------------------------------------------------------
# # 9) Display the Chat History
# # -------------------------------------------------------
# st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line before chat section

# st.subheader("Conversation with Hybrid Bot")
# display_chat(st.session_state["hybrid_chatHistory"])

# # -------------------------------------------------------
# # 10) Clear Chat Button
# # -------------------------------------------------------
# if st.button("Clear Chat", key="clear_hybrid"):
#     st.session_state["hybrid_chatHistory"] = []
#     st.success("Hybrid Bot chat has been cleared.")

# # -----------------------------------------
# # 11) Auto-scroll to page bottom if needed
# # -----------------------------------------
# # This section ensures the page scrolls to the latest message
# if 'asked_any_bot' not in st.session_state:
#     st.session_state['asked_any_bot'] = False

# if 'asked_any_bot' in st.session_state and st.session_state['asked_any_bot']:
#     # Use a script to scroll to the bottom of the page
#     scroll_script = """
#     <script>
#     window.scrollTo(0, document.body.scrollHeight);
#     </script>
#     """
#     st.markdown(scroll_script, unsafe_allow_html=True)
#     st.session_state['asked_any_bot'] = False  # Reset the flag

import streamlit as st
import requests
import json

# -----------------------------
# 1) Page Config & Custom CSS
# -----------------------------
st.set_page_config(layout="wide")  # Use wide layout for side-by-side columns

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

/* Style the "Clear Chat" buttons */
div.stButton > button.clear-chat {
    background-color: #e63946;
    color: white;
    border-radius: 6px;
    border: 1px solid #d62828;
    padding: 0.3em 0.8em;
    cursor: pointer;
    font-size: 12px;
}
div.stButton > button.clear-chat:hover {
    background-color: #d62828;
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
    max-height: 600px;
    overflow-y: auto;
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    margin-bottom: 20px;
}

/* Style for the expanders */
.streamlit-expanderHeader {
    font-weight: bold;
    font-size: 16px;
    color: #333;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# -----------------------------------------------------
# 2) Initialize session state for 2 chat histories
# -----------------------------------------------------
if "bot1_chatHistory" not in st.session_state:
    st.session_state["bot1_chatHistory"] = []
if "bot2_chatHistory" not in st.session_state:
    st.session_state["bot2_chatHistory"] = []

# -----------------------------------
# 3) Function to display chat history
# -----------------------------------
def display_chat(chat_history, container_id):
    """
    Display the conversation messages in a scrollable container.
    Each user message is right-aligned and assistant message is left-aligned.
    Also includes expanders for top references if present.
    """
    container_style = f"""
    <style>
    #{container_id} {{
        max-height: 600px;
        overflow-y: auto;
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }}
    </style>
    """
    st.markdown(container_style, unsafe_allow_html=True)
    
    # Open container div
    st.markdown(f"<div id='{container_id}'>", unsafe_allow_html=True)

    for msg in chat_history:
        if msg["role"] == "assistant":
            st.markdown(
                f"""
                <div style='text-align: left; background-color: #F0F0F0; 
                padding: 15px; margin: 10px 0; border-radius: 8px;'>
                    <b>Assistant:</b> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Expanders for top references
            full_response = msg.get("full_response", {})
            top_references = full_response.get("top_references", [])
            sources = full_response.get("source", [])
            page_nos = full_response.get("pageNos", [])

            # Only show expander if references are present
            if top_references and sources and page_nos:
                if len(top_references) == len(sources) == len(page_nos):
                    with st.expander("🔍 View Top References"):
                        for i in range(len(top_references)):
                            st.markdown(
                                f"**Reference {i+1}:** {top_references[i]}<br>"
                                f"*Source:* `{sources[i]}` | *Page:* {page_nos[i]}",
                                unsafe_allow_html=True
                            )
                            st.markdown("---")
                else:
                    st.warning("Mismatch in lengths of top_references, source, and pageNos.")
            else:
                st.info("No additional references available.")
        
        elif msg["role"] == "user":
            st.markdown(
                f"""
                <div style='text-align: right; background-color: #D0F0FF; 
                padding: 15px; margin: 10px 0; border-radius: 8px;'>
                    <b>You:</b> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )

    # Close container div
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------
# 4) Function to update base URL (with trailing slash off)
# -------------------------------------------------------
def update_base_url(new_url):
    if new_url:
        clean_url = new_url.rstrip("/")
        st.session_state["base_url"] = clean_url
        st.success(f"API base URL updated successfully: {clean_url}")
    else:
        st.warning("Please enter a valid URL.")

# -------------------------------------------------------
# 5) Page Title and Base URL Configuration
# -------------------------------------------------------
st.title("Compare Two Hybrid Bot Endpoints Side by Side")

# Default or existing base URL
default_base_url = st.session_state.get("base_url", "http://127.0.0.1:8000")

st.markdown("#### API Endpoint Configuration")
with st.form("base_url_form"):
    base_url_input = st.text_input(
        "Enter API base URL (e.g., http://127.0.0.1:8000)",
        value=default_base_url
    )
    submitted = st.form_submit_button("Save")
    if submitted:
        update_base_url(base_url_input)

st.markdown("---")
current_base_url = st.session_state.get("base_url", "Not Set")
st.write(f"**Current API Base URL:** {current_base_url}")

# -------------------------------------------------------
# 6) User question input
# -------------------------------------------------------
st.markdown("## Enter Your Question (Will Be Sent to Both Bots)")
user_question = st.text_input("Your question here:", "")

# Define the old & new endpoints
base_url = st.session_state.get("base_url", "http://127.0.0.1:8000").rstrip('/')
url_bot1 = f"{base_url}/chatbotazure/hybrid-bot-response-old/"
url_bot2 = f"{base_url}/chatbotazure/hybrid-bot-response/"

# Common payload values that both bots share
common_payload = {
    "index_name": "358deb70-f5fb-441b-94f5-aac63e574a99",
    "prompt": (
        "You are a helpful assistant working for Bajaj Allianz Life Insurance Company also known as Bajaj Allianz. "
        "Use the question, source documents, and the conversation history to answer the question in a conversational manner. "
        "If any information is missing in the question, ask a followup question to get those values before any calculations. "
        "Your role is to provide accurate, concise answers about Bajaj Allianz products, services, and internal content. "
        "You cannot take independent actions; you may only respond to questions and offer guidance. "
        "You will always stay in your character no matter what. Respond in the language in which user asked the question. "
        "If the user asked the question in English, respond strictly in English. If the user asked the question in Hinglish, respond in Hinglish. "
        "Do not exceed 50 words in your initial response. If the user asks for more details, expand your response for up to 150 words. "
        "While replying in Hinglish, make sure translation is context-aware and spoken as a female. "
        "Answer strictly based on the provided context. Do not incorporate information from outside sources or hallucinate. "
        "For questions that are too general, ask follow-up questions to gain clarity and then respond with an appropriate answer. "
        "For unrelated questions: 'I'm here to assist with Bajaj Allianz Life-related questions. Let me know if there's something specific about Bajaj Allianz Life I can help with.' "
        "For inappropriate language: 'I'm here to provide helpful support. Let's keep our conversation positive. How can I assist you with Bajaj Allianz Life offerings?' "
        "Answer the question based on the relevant chunks and tables retrieved. "
        "First, see if the chunks and tables answer the sub-questions properly, then only answer the main question using the answers for sub-questions. "
        "Finally answer the main question only."
    ),
    "language": "English"
}

# -------------------------------------------------------
# 7) Two Columns for the Two Bots
# -------------------------------------------------------
col_left, col_right = st.columns(2)

with col_left:
    st.header("Bot 1: (No Specific Page Ranges and Plan Summary)")
    # Ask Bot 1
    if st.button("Ask Old Hybrid Bot"):
        if user_question.strip() == "":
            st.warning("Please enter a question first.")
        else:
            # Add user question to chat history
            st.session_state["bot1_chatHistory"].append({
                "role": "user",
                "content": user_question
            })

            payload_bot1 = {
                "question": user_question,
                "chat_history": st.session_state["bot1_chatHistory"],
                **common_payload
            }

            with st.spinner("Old Hybrid Bot is thinking..."):
                try:
                    response1 = requests.post(url_bot1, json=payload_bot1, timeout=30)
                    response1.raise_for_status()
                    data1 = response1.json()

                    final_output1 = data1.get("final_output", "")
                    # Add assistant response to chat history
                    st.session_state["bot1_chatHistory"].append({
                        "role": "assistant",
                        "content": final_output1,
                        "full_response": data1
                    })

                except Exception as e:
                    st.session_state["bot1_chatHistory"].append({
                        "role": "assistant",
                        "content": f"❌ Error: {str(e)}",
                        "full_response": {}
                    })
                    st.error(f"Error calling Old Hybrid Bot: {e}")

    # Display Bot 1 Chat
    display_chat(st.session_state["bot1_chatHistory"], container_id="bot1_container")

    # Clear chat for Bot 1
    if st.button("Clear Chat (Bot 1)", key="clear_bot1", help="Clear Old Bot chat history"):
        st.session_state["bot1_chatHistory"] = []
        st.success("Cleared Bot 1 chat.")

with col_right:
    st.header("Bot 2: (With Specific Page Ranges and Plan Summary)")
    # Ask Bot 2
    if st.button("Ask New Hybrid Bot"):
        if user_question.strip() == "":
            st.warning("Please enter a question first.")
        else:
            # Add user question to chat history
            st.session_state["bot2_chatHistory"].append({
                "role": "user",
                "content": user_question
            })

            payload_bot2 = {
                "question": user_question,
                "chat_history": st.session_state["bot2_chatHistory"],
                **common_payload
            }

            with st.spinner("New Hybrid Bot is thinking..."):
                try:
                    response2 = requests.post(url_bot2, json=payload_bot2, timeout=30)
                    response2.raise_for_status()
                    data2 = response2.json()

                    final_output2 = data2.get("final_output", "")
                    # Add assistant response to chat history
                    st.session_state["bot2_chatHistory"].append({
                        "role": "assistant",
                        "content": final_output2,
                        "full_response": data2
                    })

                except Exception as e:
                    st.session_state["bot2_chatHistory"].append({
                        "role": "assistant",
                        "content": f"❌ Error: {str(e)}",
                        "full_response": {}
                    })
                    st.error(f"Error calling New Hybrid Bot: {e}")

    # Display Bot 2 Chat
    display_chat(st.session_state["bot2_chatHistory"], container_id="bot2_container")

    # Clear chat for Bot 2
    if st.button("Clear Chat (Bot 2)", key="clear_bot2", help="Clear New Bot chat history"):
        st.session_state["bot2_chatHistory"] = []
        st.success("Cleared Bot 2 chat.")

# -----------------------------------------
# 8) Optional: Auto-scroll to bottom
# -----------------------------------------
# If you want automatic scrolling when a message arrives,
# you can add a small JavaScript snippet to scroll to bottom.
# For example:
# scroll_script = """
# <script>
# window.scrollTo(0, document.body.scrollHeight);
# </script>
# """
# st.markdown(scroll_script, unsafe_allow_html=True)

