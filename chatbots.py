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
#         background-color: #FFFFFF;
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
#             # Display assistant message
#             st.markdown(
#                 f"""
#                 <div style='text-align: left; background-color: #F0F0F0; 
#                 padding: 15px; margin: 10px 0; border-radius: 8px;'>
#                     <b>Assistant:</b> {msg['content']}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#             # Add expander for detailed response
#             with st.expander("View Detailed Response"):
#                 full_response = msg.get("full_response", {})
#                 final_output = full_response.get("final_output", "")
#                 top_references = full_response.get("top_references", [])

#                 # Display Final Output
#                 # st.markdown(f"**Final Output:**\n\n{final_output}\n\n---")

#                 # Iterate through top_references
#                 for ref_idx, reference in enumerate(top_references, start=1):
#                     question = reference.get("question", "No question provided.")
#                     top_sections = reference.get("top_sections", [])
#                     top_chunks = reference.get("top_chunks", [])
#                     top_tables = reference.get("top_tables", [])

#                     st.markdown(f"### Reference {ref_idx}: {question}\n")

#                     # Display Top Sections
#                     if top_sections:
#                         st.markdown("**Top Sections:**")
#                         for sec in top_sections:
#                             sec_title = sec.get("title", "No title")
#                             sec_text = sec.get("section_text", "No section text available.")
#                             sec_page = sec.get("page_idx", "N/A")
#                             similarity = sec.get("similarity", "N/A")
#                             st.markdown(
#                                 f"- **Title:** {sec_title}\n"
#                                 f"  - **Page Index:** {sec_page}\n"
#                                 f"  - **Similarity:** {similarity}\n\n"
#                                 f"  ```\n"
#                                 f"{sec_text}\n"
#                                 f"  ```\n"
#                             )

#                     # Display Top Chunks
#                     if top_chunks:
#                         st.markdown("**Top Chunks:**")
#                         for chk in top_chunks:
#                             chk_id = chk.get("chunk_id", "N/A")
#                             chk_text = chk.get("text", "No text available.")
#                             chk_score = chk.get("score", "N/A")
#                             chk_page = chk.get("page_idx", "N/A")
#                             st.markdown(
#                                 f"- **Chunk ID:** {chk_id}\n"
#                                 f"  - **Score:** {chk_score}\n"
#                                 f"  - **Page Index:** {chk_page}\n\n"
#                                 f"  ```\n"
#                                 f"{chk_text}\n"
#                                 f"  ```\n"
#                             )

#                     # Display Top Tables
#                     if top_tables:
#                         st.markdown("**Top Tables:**")
#                         for tbl in top_tables:
#                             tbl_id = tbl.get("table_id", "N/A")
#                             tbl_text = tbl.get("text", "No table text available.")
#                             tbl_score = tbl.get("score", "N/A")
#                             tbl_page = tbl.get("page_idx", "N/A")
#                             st.markdown(
#                                 f"- **Table ID:** {tbl_id}\n"
#                                 f"  - **Score:** {tbl_score}\n"
#                                 f"  - **Page Index:** {tbl_page}\n\n"
#                                 f"  ```\n"
#                                 f"{tbl_text}\n"
#                                 f"  ```\n"
#                             )
#                     st.markdown("---")  # Separator between references

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
# url_hBot = f"{base_url}/chatbotazure/retrieve-response-new-bot/"

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
#             "chat_history": st.session_state["hybrid_chatHistory"]
#         }
#         with st.spinner("Waiting for the Hybrid Bot to respond... max 7 sec..."):
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
st.set_page_config(layout="wide")

custom_css = """
<style>
/* Style the "Ask" button */
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

/* Style the "Clear Chat" button */
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

/* Chat container style */
.chat-container {
    max-height: 600px;
    overflow-y: auto;
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    margin-bottom: 20px;
}

/* Style for JSON view icon */
.json-icon {
    cursor: pointer;
    font-size: 16px;
    margin-left: 10px;
    color: #555;
}
.json-icon:hover {
    color: #000;
}

/* Style for expanders */
.streamlit-expanderHeader {
    font-weight: bold;
    font-size: 16px;
    color: #333;
}

/* Style for preformatted prompt display */
.preformatted {
    white-space: pre-wrap;
    background-color: #f0f0f0;
    padding: 10px;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 14px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------------------------------
# 2) Session State Initialization
# -------------------------------------------------------
if "hybrid_chatHistory" not in st.session_state:
    st.session_state["hybrid_chatHistory"] = []

if "json_popups" not in st.session_state:
    st.session_state["json_popups"] = {}

# Default bot prompt (multi-line) as provided
default_prompt = (
    "You are a helpful assistant working for Bajaj Allianz Life Insurance Company, also known as Bajaj Allianz.\n"
    "Use the question, source documents, and the conversation history to answer the question in a conversational manner.\n"
    "If any information is missing in the question and additional details exist in the provided source documents, ask a follow-up question to get those values before proceeding with any calculations.\n"
    "Your role is to provide accurate, concise answers about Bajaj Allianz products, services, and internal content.\n"
    "You cannot take independent actions; you may only respond to questions and offer guidance.\n"
    "You will always stay in your character no matter what. Respond in the language in which the user asked the question.\n"
    "If the user asked the question in English, respond strictly in English.\n"
    "If the user asked the question in Hinglish, respond in Hinglish.\n"
    "Do not exceed 50 words in your initial response.\n"
    "If the user asks for more details, expand your response for up to 150 words.\n"
    "While replying in Hinglish, ensure the translation is context-aware and spoken as a female.\n"
    "Answer strictly based on the provided context. Do not incorporate information from outside sources or hallucinate.\n"
    "For questions that are too general, ask follow-up questions to gain clarity and then respond with an appropriate answer.\n"
    "For unrelated questions: 'I'm here to assist with Bajaj Allianz Life-related questions. Let me know if there's something specific about Bajaj Allianz Life I can help with.'\n"
    "For inappropriate language: 'I'm here to provide helpful support. Let's keep our conversation positive. How can I assist you with Bajaj Allianz Life offerings?'\n"
    "Answer the question using the source documents and conversation history (which may be empty at the beginning).\n"
    "If it is a greeting, always welcome them and tell about yourself.\n"
    "Do not ask generic follow-up questions such as 'Would you like more details?' unless the context has those information.\n"
    "If the user replies with an affirmative such as 'yes', generate a standalone question that precisely asks for the additional information present in the source documents."
)

if "bot_prompt" not in st.session_state:
    st.session_state["bot_prompt"] = default_prompt

# -------------------------------------------------------
# 3) Layout: Two Columns (Left: Settings, Right: Chat)
# -------------------------------------------------------
col1, col2 = st.columns([1, 2])

# Left Column: Settings (API Base URL & Bot Prompt)
with col1:
    st.header("Settings")
    st.markdown("### API Endpoint Configuration")
    with st.form(key='base_url_form'):
        base_url_input = st.text_input(
            "Enter API base URL (e.g., http://127.0.0.1:8000 or https://<ngrok_link>):",
            value=st.session_state.get("base_url", "http://127.0.0.1:8000")
        )
        submit_button = st.form_submit_button(label='Save')
        if submit_button:
            def update_base_url(new_url):
                if new_url:
                    clean_url = new_url.rstrip("/")
                    st.session_state["base_url"] = clean_url
                    st.success(f"API base URL updated successfully to: {clean_url}")
                else:
                    st.warning("Please enter a valid URL.")
            update_base_url(base_url_input)
    st.markdown("---")
    st.write(f"**Current API Base URL:** {st.session_state.get('base_url', 'Not Set')}")
    
    st.markdown("### Bot Prompt Configuration")
    with st.form(key='bot_prompt_form'):
        # Increase text area height to 400 pixels
        bot_prompt = st.text_area(
            "Enter the prompt to be sent in the payload (this prompt will be used for subsequent questions until updated):",
            value=st.session_state.get("bot_prompt", default_prompt),
            height=400
        )
        save_prompt_button = st.form_submit_button(label='Save Prompt')
        if save_prompt_button:
            def save_bot_prompt(new_prompt):
                if new_prompt.strip():
                    st.session_state["bot_prompt"] = new_prompt.strip()
                    st.success("Bot prompt updated successfully.")
                else:
                    st.warning("Prompt cannot be empty.")
            save_bot_prompt(bot_prompt)
    st.markdown("---")
    st.markdown("**Current Bot Prompt:**")
    # Display the current bot prompt with preserved line breaks using preformatted text.
    st.markdown(f"<div class='preformatted'>{st.session_state.get('bot_prompt', 'Not Set')}</div>", unsafe_allow_html=True)

# Right Column: Chat Interface
with col2:
    st.header("Chat")
    user_question = st.text_input("Enter your question:", "")
    
    st.markdown("### Ask the Hybrid Bot")
    base_url = st.session_state.get("base_url", "http://127.0.0.1:8000").rstrip('/')
    url_hBot = f"{base_url}/chatbotazure/retrieve-response-new-bot/"
    
    if st.button("Ask Hybrid Bot"):
        if user_question.strip() == "":
            st.warning("Please enter a question before asking the bot.")
        else:
            st.session_state["hybrid_chatHistory"].append({
                "role": "user",
                "content": user_question
            })
            payload = {
                "question": user_question,
                "prompt": st.session_state.get("bot_prompt", ""),
                "chat_history": st.session_state["hybrid_chatHistory"],
                "index_name": "09dee44c-538d-4983-a7a0-7d7eb4360c82"
            }
            with st.spinner("Waiting for the Hybrid Bot to respond... max 7 sec..."):
                try:
                    response = requests.post(url_hBot, json=payload)
                    response.raise_for_status()
                    response_data = response.json()
                    final_output = response_data.get("final_output", "")
                    st.session_state["hybrid_chatHistory"].append({
                        "role": "assistant",
                        "content": final_output,
                        "full_response": response_data
                    })
                except Exception as e:
                    st.session_state["hybrid_chatHistory"].append({
                        "role": "assistant",
                        "content": "❌ Error: Unable to reach the Hybrid Bot. Please try again later.",
                        "full_response": {}
                    })
                    st.error(f"An error occurred: {e}")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Conversation with Hybrid Bot")
    
    def display_chat(chat_history):
        container_style = """
        <style>
        .chat-container {
            max-height: 600px;
            overflow-y: auto;
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
        }
        </style>
        """
        st.markdown(container_style, unsafe_allow_html=True)
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    
        for idx, msg in enumerate(chat_history):
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
                # Expandable section for top references
                full_response = msg.get("full_response", {})
                top_references = full_response.get("top_references", [])
                sources = full_response.get("source", [])
                page_nos = full_response.get("pageNos", [])
    
                if top_references and sources and page_nos:
                    if len(top_references) == len(sources) == len(page_nos):
                        with st.expander("🔍 Top References"):
                            for i in range(len(top_references)):
                                st.markdown(
                                    f"**Reference {i+1}:** {top_references[i]}<br>"
                                    f"*Source:* `{sources[i]}` | *Page:* {page_nos[i]}",
                                    unsafe_allow_html=True
                                )
                                st.markdown("---")
                    else:
                        st.warning("Warning: The lengths of 'top_references', 'source', and 'pageNos' do not match.")
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
    
        st.markdown("</div>", unsafe_allow_html=True)
    
    display_chat(st.session_state["hybrid_chatHistory"])
    
    if st.button("Clear Chat", key="clear_hybrid"):
        st.session_state["hybrid_chatHistory"] = []
        st.success("Hybrid Bot chat has been cleared.")
    
    # Auto-scroll to bottom if needed
    if 'asked_any_bot' not in st.session_state:
        st.session_state['asked_any_bot'] = False
    if st.session_state.get('asked_any_bot', False):
        st.markdown("""
        <script>
        window.scrollTo(0, document.body.scrollHeight);
        </script>
        """, unsafe_allow_html=True)
        st.session_state['asked_any_bot'] = False
