# import streamlit as st
# import requests
# import json

# # -----------------------------
# # 1) Page Config & Custom CSS
# # -----------------------------
# st.set_page_config(layout="wide")

# # Custom CSS for vertical dividers, button styling, and overall UI improvements
# custom_css = """
# <style>
# /* Vertical divider for columns */
# .column-wrapper {
#     border-right: 1px solid #ccc;
#     padding-right: 20px;
# }
# .column-wrapper:last-child {
#     border-right: none;  /* Remove right border on last column */
# }

# /* Style the "Ask" buttons */
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

# /* Ensure the chat containers have a consistent look */
# .chat-container {
#     max-height: 450px;
#     overflow-y: auto;
#     background-color: #f9f9f9;
#     padding: 10px;
#     border-radius: 5px;
#     border: 1px solid #e0e0e0;
#     margin-bottom: 10px;
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
# </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

# # -------------------------------------------------------
# # 2) Define the initial chat history (same for all 3 bots)
# # -------------------------------------------------------
# initial_chat_history = []

# # -----------------------------------
# # 3) Session State for Chat Histories
# # -----------------------------------
# for i in range(1, 4):
#     key = f"col{i}_chatHistory"
#     if key not in st.session_state:
#         st.session_state[key] = initial_chat_history.copy()

# # -----------------------------------
# # 4) Session State for Base URL
# # -----------------------------------
# if "base_url" not in st.session_state:
#     st.session_state["base_url"] = "http://127.0.0.1:8000"

# # -----------------------------------
# # 5) Session State for JSON Popups
# # -----------------------------------
# if "json_popups" not in st.session_state:
#     st.session_state["json_popups"] = {}  # Dictionary to store which messages have JSON popups open

# # -------------------------------------------------------
# # 6) Helper function to display chat messages
# # -------------------------------------------------------
# def display_chat(chat_history, container_id):
#     """
#     Display the conversation with assistant on the left,
#     and user on the right using basic HTML alignment.
#     Adds a JSON view expander next to assistant messages.
#     """
#     # Container for messages
#     container_style = f"""
#     <style>
#     #{container_id} {{
#         max-height: 450px;
#         overflow-y: auto;
#         background-color: #FFFFFF;
#         padding: 10px;
#         border-radius: 5px;
#         border: 1px solid #e0e0e0;
#         margin-bottom: 10px;
#     }}
#     </style>
#     """
#     st.markdown(container_style, unsafe_allow_html=True)
    
#     # Open container div
#     st.markdown(f"<div id='{container_id}'>", unsafe_allow_html=True)
    
#     # Display each message
#     for idx, msg in enumerate(chat_history):
#         if msg["role"] == "assistant":
#             # Display assistant message
#             st.markdown(
#                 f"""
#                 <div style='text-align: left; background-color: #F0F0F0; 
#                 padding: 8px; margin: 5px 0; border-radius: 5px; position: relative;'>
#                     <b>Assistant:</b> {msg['content']}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#             # Add expander for JSON
#             with st.expander("View Top Chunks", expanded=False):
#                 full_response = msg.get("full_response", {})
                
#                 # Extract required fields
#                 top_references = full_response.get("top_references", [])
#                 sources = full_response.get("source", [])
#                 metadata = full_response.get("metadata", [])
                
#                 # Check if all lists are of the same length
#                 if len(top_references) == len(sources) == len(metadata):
#                     for chunk_num in range(min(5,len(top_references))):
#                         st.markdown(f"#### Chunk {chunk_num+1}: \n\n{top_references[chunk_num]}")
#                         st.markdown(f"``` Source: {sources[chunk_num]} ```")
#                         headers = metadata[chunk_num].get("headers", {})
#                         chunk_attributes = metadata[chunk_num].get("chunk_attributes", {})
#                         if chunk_attributes:
#                             chunk_page = metadata[chunk_num].get("chunk_attributes", {}).get("page_idx",{})
#                             sibling_chunks = metadata[chunk_num].get("sibling_chunks", {})
#                             sibling_md = "\nSiblings: \n"
#                             for sibling in sibling_chunks:
#                                 sibling_md+="- "+sibling+"\n"
#                             st.markdown(f"```{sibling_md}```")
#                         elif headers:
#                             headers_md = "\nHeaders: \n"
#                             for header_key, header_value in headers.items():
#                                 headers_md += f"{header_key}: {header_value};\n\n "
#                             st.markdown(f"```{headers_md}```")
#                         else:
#                             # st.markdown("**Headers:** Not Available")
#                             pass
#                         st.markdown("___")
#                 else:
#                     st.warning("Mismatch in the lengths of top_references, source, and metadata.")
                    
#         elif msg["role"] == "user":
#             # Display user message
#             st.markdown(
#                 f"""
#                 <div style='text-align: right; background-color: #D0F0FF; 
#                 padding: 8px; margin: 5px 0; border-radius: 5px;'>
#                     <b>You:</b> {msg['content']}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
    
#     # Close container div
#     st.markdown(f"</div>", unsafe_allow_html=True)

# # -------------------------------------------------------
# # 7) Function to update base_url
# # -------------------------------------------------------
# def update_base_url(new_url):
#     if new_url:
#         st.session_state["base_url"] = new_url
#         st.success("API base URL updated successfully!")
#     else:
#         st.warning("Please enter a valid URL.")

# # -------------------------------------------------------
# # 8) Main Layout
# # -------------------------------------------------------
# st.title("Compare Chatbots Side by Side")

# # -------------------------------------------------------
# # 9) Input Section for API Base URL
# # -------------------------------------------------------
# st.markdown("### API Endpoint Configuration")

# with st.form(key='base_url_form'):
#     base_url_input = st.text_input(
#         "Enter API base URL (e.g., http://127.0.0.1:8000 or https://<ngrok_link>):",
#         value=st.session_state["base_url"]
#     )
#     submit_button = st.form_submit_button(label='Save')

#     if submit_button:
#         update_base_url(base_url_input)

# st.markdown("---")
# st.write(f"**Current API Base URL:** {st.session_state['base_url']}")

# # -------------------------------------------------------
# # 10) User input for the question
# # -------------------------------------------------------
# user_question = st.text_input("Enter your question:", "")

# st.write("**Click one of the buttons below** to ask a single bot at a time.")

# # Endpoints based on base_url
# base_url = st.session_state["base_url"].rstrip('/')  # Remove trailing slash if any

# url_nBot = f"{base_url}/chatbotazure/normal-bot-response/"
# url_nBotMemory = f"{base_url}/chatbotazure/normal-bot-response-with-memory/"
# url_hBot = f"{base_url}/chatbotazure/hybrid-bot-response/"

# # ------------------------------
# # Buttons to query each endpoint
# # ------------------------------
# col_button1, col_button2, col_button3 = st.columns(3)

# # Flag to determine if any bot was asked
# if 'asked_any_bot' not in st.session_state:
#     st.session_state['asked_any_bot'] = False

# with col_button1:
#     if st.button("Ask Normal Bot"):
#         if user_question.strip() == "":
#             st.warning("Please enter a question before asking the bot.")
#         else:
#             st.session_state['asked_any_bot'] = True
            
#             # Append user message to chat history
#             st.session_state["col1_chatHistory"].append({
#                 "role": "user",
#                 "content": user_question
#             })
            
#             payload1 = {
#                 "question": user_question,
#                 "index_name": "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8",
#                 "chat_history": st.session_state["col1_chatHistory"]
#             }
#             try:
#                 response1 = requests.post(url_nBot, json=payload1)
#                 response1.raise_for_status()  # Raise exception for HTTP errors
#                 response1_data = response1.json()
#                 # Assuming response1_data contains 'final_output' and 'chat_history'
#                 final_output1 = response1_data.get("final_output", "")
#                 updated_chat_history1 = response1_data.get("chat_history", [])
                
#                 # Append the assistant message with full_response
#                 st.session_state["col1_chatHistory"].append({
#                     "role": "assistant",
#                     "content": final_output1,
#                     "full_response": response1_data  # Store the entire response as full_response
#                 })
#             except Exception as e:
#                 # Log error message in the chat as "assistant"
#                 st.session_state["col1_chatHistory"].append({
#                     "role": "assistant",
#                     "content": f"Error calling Normal Bot: {e}",
#                     "full_response": {}
#                 })

# with col_button2:
#     if st.button("Ask Normal Bot + Memory"):
#         if user_question.strip() == "":
#             st.warning("Please enter a question before asking the bot.")
#         else:
#             st.session_state['asked_any_bot'] = True
            
#             # Append user message to chat history
#             st.session_state["col2_chatHistory"].append({
#                 "role": "user",
#                 "content": user_question
#             })
            
#             payload2 = {
#                 "question": user_question,
#                 "index_name": "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8",
#                 "chat_history": st.session_state["col2_chatHistory"]
#             }
#             try:
#                 response2 = requests.post(url_nBotMemory, json=payload2)
#                 response2.raise_for_status()
#                 response2_data = response2.json()
#                 final_output2 = response2_data.get("final_output", "")
#                 updated_chat_history2 = response2_data.get("chat_history", [])
                
#                 st.session_state["col2_chatHistory"].append({
#                     "role": "assistant",
#                     "content": final_output2,
#                     "full_response": response2_data
#                 })
#             except Exception as e:
#                 st.session_state["col2_chatHistory"].append({
#                     "role": "assistant",
#                     "content": f"Error calling Normal Bot + Memory: {e}",
#                     "full_response": {}
#                 })

# with col_button3:
#     if st.button("Ask Hybrid Bot"):
#         if user_question.strip() == "":
#             st.warning("Please enter a question before asking the bot.")
#         else:
#             st.session_state['asked_any_bot'] = True
            
#             # Append user message to chat history
#             st.session_state["col3_chatHistory"].append({
#                 "role": "user",
#                 "content": user_question
#             })
            
#             payload3 = {
#                 "question": user_question,
#                 "chat_history": st.session_state["col3_chatHistory"]
#             }
#             try:
#                 response3 = requests.post(url_hBot, json=payload3)
#                 response3.raise_for_status()
#                 response3_data = response3.json()
#                 final_output3 = response3_data.get("final_output", "")
#                 updated_chat_history3 = response3_data.get("chat_history", [])
                
#                 st.session_state["col3_chatHistory"].append({
#                     "role": "assistant",
#                     "content": final_output3,
#                     "full_response": response3_data
#                 })
#             except Exception as e:
#                 st.session_state["col3_chatHistory"].append({
#                     "role": "assistant",
#                     "content": f"Error calling Hybrid Bot: {e}",
#                     "full_response": {}
#                 })

# # -------------------------------------------------------
# # 11) Display the chat histories in 3 columns with borders
# # -------------------------------------------------------
# st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line before chat sections

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.subheader("Normal Bot")
#     display_chat(st.session_state["col1_chatHistory"], container_id="chat-container-1")

# with col2:
#     st.subheader("Normal Bot + Memory")
#     display_chat(st.session_state["col2_chatHistory"], container_id="chat-container-2")

# with col3:
#     st.subheader("Hybrid Bot")
#     display_chat(st.session_state["col3_chatHistory"], container_id="chat-container-3")

# # -----------------------------------------
# # 12) Auto-scroll to page bottom if needed
# # -----------------------------------------
# if st.session_state['asked_any_bot']:
#     # Use a script to scroll to the bottom of the page
#     scroll_script = """
#     <script>
#     window.scrollTo(0, document.body.scrollHeight);
#     </script>
#     """
#     st.markdown(scroll_script, unsafe_allow_html=True)
#     st.session_state['asked_any_bot'] = False  # Reset the flag




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import streamlit as st
import requests
import json

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
    max-height: 450px;
    overflow-y: auto;
    background-color: #f9f9f9;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #e0e0e0;
    margin-bottom: 10px;
}

/* Style for the JSON view icon */
.json-icon {
    cursor: pointer;
    font-size: 16px;
    margin-left: 10px;
    color: #555;
}
.json-icon:hover {
    color: #000;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------------------------------
# 2) Define the initial chat history (same for all 3 bots)
# -------------------------------------------------------
initial_chat_history = []

# -----------------------------------
# 3) Session State for Chat Histories
# -----------------------------------
for i in range(1, 4):
    key = f"col{i}_chatHistory"
    if key not in st.session_state:
        st.session_state[key] = initial_chat_history.copy()

# -----------------------------------
# 4) Session State for Base URL
# -----------------------------------
if "base_url" not in st.session_state:
    st.session_state["base_url"] = "http://127.0.0.1:8000"

# -----------------------------------
# 5) Session State for JSON Popups
# -----------------------------------
if "json_popups" not in st.session_state:
    st.session_state["json_popups"] = {}  # Dictionary to store which messages have JSON popups open

# -------------------------------------------------------
# 6) Helper function to display chat messages
# -------------------------------------------------------
def display_chat(chat_history, container_id):
    """
    Display the conversation with assistant on the left,
    and user on the right using basic HTML alignment.
    Adds a JSON view expander next to assistant messages.
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
    
    # # Display each message
    # for idx, msg in enumerate(chat_history):
    #     if msg["role"] == "assistant":
    #         # Display assistant message
    #         st.markdown(
    #             f"""
    #             <div style='text-align: left; background-color: #F0F0F0; 
    #             padding: 8px; margin: 5px 0; border-radius: 5px; position: relative;'>
    #                 <b>Assistant:</b> {msg['content']}
    #             </div>
    #             """,
    #             unsafe_allow_html=True
    #         )
    #         # Add expander for JSON
    #         with st.expander("View Top Chunks", expanded=False):
    #             full_response = msg.get("full_response", {})
                
    #             # Extract required fields
    #             top_references = full_response.get("top_references", [])
    #             sources = full_response.get("source", [])
    #             metadata = full_response.get("metadata", [])
                
    #             # Check if all lists are of the same length
    #             if len(top_references) == len(sources) == len(metadata):
    #                 # Limit to top 5 chunks to keep it concise
    #                 for chunk_num in range(min(5, len(top_references))):
    #                     st.markdown(f"### Chunk {chunk_num + 1}")
    #                     st.markdown(f"**Source:** {sources[chunk_num]}")
                        
    #                     headers = metadata[chunk_num].get("headers", {})
    #                     chunk_attributes = metadata[chunk_num].get("chunk_attributes", {})
    #                     sibling_chunks = metadata[chunk_num].get("sibling_chunks", {})
                        
    #                     if headers:
    #                         headers_md = "**Headers:**\n\n"
    #                         for header_key, header_value in headers.items():
    #                             headers_md += f"- **{header_key}:** {header_value}\n"
    #                         st.markdown(headers_md)
                        
    #                     if chunk_attributes:
    #                         chunk_page = chunk_attributes.get("page_idx", {})
    #                         st.markdown(f"**Page Index:** {chunk_page}")
                            
    #                     if sibling_chunks:
    #                         sibling_md = "**Siblings:**\n\n"
    #                         for sibling in sibling_chunks:
    #                             sibling_md += f"- {sibling}\n"
    #                         st.markdown(sibling_md)
                        
    #                     st.markdown("---")
    #             else:
    #                 st.warning("Mismatch in the lengths of top_references, source, and metadata.")
                    
    #     elif msg["role"] == "user":
    #         # Display user message
    #         st.markdown(
    #             f"""
    #             <div style='text-align: right; background-color: #D0F0FF; 
    #             padding: 8px; margin: 5px 0; border-radius: 5px;'>
    #                 <b>You:</b> {msg['content']}
    #             </div>
    #             """,
    #             unsafe_allow_html=True
    #         )
    
    # Display each message
    for idx, msg in enumerate(chat_history):
        if msg["role"] == "assistant":
            # Display assistant message
            st.markdown(
                f"""
                <div style='text-align: left; background-color: #F0F0F0; 
                padding: 8px; margin: 5px 0; border-radius: 5px; position: relative;'>
                    <b>Assistant:</b> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )
            # Add expander for JSON
            with st.expander("View Top Chunks", expanded=False):
                full_response = msg.get("full_response", {})
                
                # Extract required fields
                top_references = full_response.get("top_references", [])
                sources = full_response.get("source", [])
                metadata = full_response.get("metadata", [])
                
                # Check if all lists are of the same length
                if len(top_references) == len(sources) == len(metadata):
                    for chunk_num in range(min(5,len(top_references))):
                        st.markdown(f"#### Chunk {chunk_num+1}: \n\n{top_references[chunk_num]}")
                        chunk_page = metadata[chunk_num].get("chunk_attributes", {}).get("page_idx",{})
                        if chunk_page:
                            st.markdown(f"``` Source: {sources[chunk_num]} || Page: {chunk_page}```")
                        else:
                            st.markdown(f"``` Source: {sources[chunk_num]} ```")
                        headers = metadata[chunk_num].get("headers", {})
                        chunk_attributes = metadata[chunk_num].get("chunk_attributes", {})
                        if chunk_attributes:
                            sibling_chunks = metadata[chunk_num].get("sibling_chunks", {})
                            sibling_md = "\nSiblings: \n"
                            for sibling in sibling_chunks:
                                sibling_md+="- "+sibling+"\n"
                            st.markdown(f"```{sibling_md}```")
                        elif headers:
                            headers_md = "\nHeaders: \n"
                            for header_key, header_value in headers.items():
                                headers_md += f"{header_key}: {header_value};\n\n "
                            st.markdown(f"```{headers_md}```")
                        else:
                            # st.markdown("**Headers:** Not Available")
                            pass
                        st.markdown("___")
                else:
                    st.warning("Mismatch in the lengths of top_references, source, and metadata.")
                    
        elif msg["role"] == "user":
            # Display user message
            st.markdown(
                f"""
                <div style='text-align: right; background-color: #D0F0FF; 
                padding: 8px; margin: 5px 0; border-radius: 5px;'>
                    <b>You:</b> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )
    
    # Close container div
    st.markdown(f"</div>", unsafe_allow_html=True)

# -------------------------------------------------------
# 7) Function to update base_url
# -------------------------------------------------------
def update_base_url(new_url):
    if new_url:
        st.session_state["base_url"] = new_url
        st.success("API base URL updated successfully!")
    else:
        st.warning("Please enter a valid URL.")

# -------------------------------------------------------
# 8) Main Layout
# -------------------------------------------------------
st.title("Compare Chatbots Side by Side")

# -------------------------------------------------------
# 9) Input Section for API Base URL
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
# 10) User input for the question
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
        if user_question.strip() == "":
            st.warning("Please enter a question before asking the bot.")
        else:
            st.session_state['asked_any_bot'] = True
            
            # Append user message to chat history
            st.session_state["col1_chatHistory"].append({
                "role": "user",
                "content": user_question
            })
            
            payload1 = {
                "question": user_question,
                "index_name": "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8",
                "chat_history": st.session_state["col1_chatHistory"]
            }
            try:
                response1 = requests.post(url_nBot, json=payload1)
                response1.raise_for_status()  # Raise exception for HTTP errors
                response1_data = response1.json()
                # Assuming response1_data contains 'final_output' and 'chat_history'
                final_output1 = response1_data.get("final_output", "")
                updated_chat_history1 = response1_data.get("chat_history", [])
                
                # Append the assistant message with full_response
                st.session_state["col1_chatHistory"].append({
                    "role": "assistant",
                    "content": final_output1,
                    "full_response": response1_data  # Store the entire response as full_response
                })
            except Exception as e:
                # Log error message in the chat as "assistant"
                st.session_state["col1_chatHistory"].append({
                    "role": "assistant",
                    "content": f"Error calling Normal Bot: {e}",
                    "full_response": {}
                })

with col_button2:
    if st.button("Ask Normal Bot + Memory"):
        if user_question.strip() == "":
            st.warning("Please enter a question before asking the bot.")
        else:
            st.session_state['asked_any_bot'] = True
            
            # Append user message to chat history
            st.session_state["col2_chatHistory"].append({
                "role": "user",
                "content": user_question
            })
            
            payload2 = {
                "question": user_question,
                "index_name": "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8",
                "chat_history": st.session_state["col2_chatHistory"]
            }
            try:
                response2 = requests.post(url_nBotMemory, json=payload2)
                response2.raise_for_status()
                response2_data = response2.json()
                final_output2 = response2_data.get("final_output", "")
                updated_chat_history2 = response2_data.get("chat_history", [])
                
                st.session_state["col2_chatHistory"].append({
                    "role": "assistant",
                    "content": final_output2,
                    "full_response": response2_data
                })
            except Exception as e:
                st.session_state["col2_chatHistory"].append({
                    "role": "assistant",
                    "content": f"Error calling Normal Bot + Memory: {e}",
                    "full_response": {}
                })

with col_button3:
    if st.button("Ask Hybrid Bot"):
        if user_question.strip() == "":
            st.warning("Please enter a question before asking the bot.")
        else:
            st.session_state['asked_any_bot'] = True
            
            # Append user message to chat history
            st.session_state["col3_chatHistory"].append({
                "role": "user",
                "content": user_question
            })
            
            payload3 = {
                "question": user_question,
                "chat_history": st.session_state["col3_chatHistory"]
            }
            try:
                response3 = requests.post(url_hBot, json=payload3)
                response3.raise_for_status()
                response3_data = response3.json()
                final_output3 = response3_data.get("final_output", "")
                updated_chat_history3 = response3_data.get("chat_history", [])
                
                st.session_state["col3_chatHistory"].append({
                    "role": "assistant",
                    "content": final_output3,
                    "full_response": response3_data
                })
            except Exception as e:
                st.session_state["col3_chatHistory"].append({
                    "role": "assistant",
                    "content": f"Error calling Hybrid Bot: {e}",
                    "full_response": {}
                })

# -------------------------------------------------------
# 11) Display the chat histories in 3 columns with borders
# -------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line before chat sections

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Normal Bot")
    display_chat(st.session_state["col1_chatHistory"], container_id="chat-container-1")
    
    # Clear Chat Button for Normal Bot
    if st.button("Clear Chat", key="clear_col1"):
        st.session_state["col1_chatHistory"] = []
        st.success("Normal Bot chat has been cleared.")

with col2:
    st.subheader("Normal Bot + Memory")
    display_chat(st.session_state["col2_chatHistory"], container_id="chat-container-2")
    
    # Clear Chat Button for Normal Bot + Memory
    if st.button("Clear Chat", key="clear_col2"):
        st.session_state["col2_chatHistory"] = []
        st.success("Normal Bot + Memory chat has been cleared.")

with col3:
    st.subheader("Hybrid Bot")
    display_chat(st.session_state["col3_chatHistory"], container_id="chat-container-3")
    
    # Clear Chat Button for Hybrid Bot
    if st.button("Clear Chat", key="clear_col3"):
        st.session_state["col3_chatHistory"] = []
        st.success("Hybrid Bot chat has been cleared.")

# -----------------------------------------
# 12) Auto-scroll to page bottom if needed
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
