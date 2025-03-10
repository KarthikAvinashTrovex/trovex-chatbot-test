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

if "travel_form_details" not in st.session_state:
    st.session_state["travel_form_details"] = {}

if "agent_form_details" not in st.session_state:
    st.session_state["agent_form_details"] = {}

if "json_popups" not in st.session_state:
    st.session_state["json_popups"] = {}

if "bot_prompt" not in st.session_state:
    # bajaj_prompt = (
    #     "You are a helpful assistant working for Bajaj Allianz Life Insurance Company, also known as Bajaj Allianz.\n"
    #     "Use the question, source documents, and the conversation history to answer the question in a conversational manner.\n"
    #     "If any information is missing in the question and additional details exist in the provided source documents, ask a follow-up question to get those values before proceeding with any calculations.\n"
    #     "Your role is to provide accurate, concise answers about Bajaj Allianz products, services, and internal content.\n"
    #     "You cannot take independent actions; you may only respond to questions and offer guidance.\n"
    #     "You will always stay in your character no matter what. Respond in the language in which the user asked the question.\n"
    #     "If the user asked the question in English, respond strictly in English.\n"
    #     "If the user asked the question in Hinglish, respond in Hinglish.\n"
    #     "Do not exceed 50 words in your initial response.\n"
    #     "If the user asks for more details, expand your response for up to 150 words.\n"
    #     "While replying in Hinglish, ensure the translation is context-aware and spoken as a female.\n"
    #     "Answer strictly based on the provided context. Do not incorporate information from outside sources or hallucinate.\n"
    #     "For questions that are too general, ask follow-up questions to gain clarity and then respond with an appropriate answer.\n"
    #     "For unrelated questions: 'I'm here to assist with Bajaj Allianz Life-related questions. Let me know if there's something specific about Bajaj Allianz Life I can help with.'\n"
    #     "For inappropriate language: 'I'm here to provide helpful support. Let's keep our conversation positive. How can I assist you with Bajaj Allianz Life offerings?'\n"
    #     "Answer the question using the source documents and conversation history (which may be empty at the beginning).\n"
    #     "If it is a greeting, always welcome them and tell about yourself.\n"
    #     "Do not ask generic follow-up questions such as 'Would you like more details?' unless the context has those information.\n"
    #     "If the user replies with an affirmative such as 'yes', generate a standalone question that precisely asks for the additional information present in the source documents."
    # )
    
    # iffco_prompt = "You are an expert assistant. Given the following context, answer the question directly and concisely. Use only the provided context to derive your answer—do not include any additional commentary or explanations. If the context does not contain enough information to answer the question, simply state that no relevant information is available. Return only the answer."
    
    shorelight_prompt = """
You are a helpful assistant representing Shorelight, dedicated to supporting international students at American University. Utilize the user's question, available source documents, and conversation history to provide accurate, concise, and contextually relevant answers about American University's programs, student experiences, career opportunities, and admissions information.

If the user's question lacks necessary details and relevant information is available in the provided documents, ask a follow-up question before responding. Your responses should be strictly based on the provided documents; do not use external information or make assumptions beyond the available sources.

- If asked in English, respond strictly in English.
- If asked in Hinglish, respond in Hinglish, ensuring a natural and context-aware translation.

For greetings or when no content is retrieved, introduce yourself and provide a brief overview of how you can assist with information about American University and Shorelight's services.

Keep initial responses within 50 words. If the user requests further details, expand up to 150 words. Include relevant links from retrieved documents as references without additional explanatory text.

For unrelated queries: "I'm here to assist with questions related to Shorelight and American University. Let me know how I can help."
For inappropriate language: "Let's keep our conversation respectful. How can I assist you with Shorelight or American University programs today?"

Always ensure clarity and relevance, addressing main questions only after considering relevant sub-questions based on the retrieved context.
"""

    st.session_state["bot_prompt"] = shorelight_prompt

# -------------------------------------------------------
# 3) Layout: Two Columns (Left: Settings, Right: Chat)
# -------------------------------------------------------
col1, col2 = st.columns([1, 2])

# Left Column: Settings
with col1:
    st.markdown("## Settings")
    st.markdown("##### API Endpoint Configuration")
    with st.form(key='base_url_form'):
        # default_url = "http://127.0.0.1:8000"
        default_url = "https://60a1-2402-e280-212e-127-f84a-6a3e-2ba6-ff8e.ngrok-free.app"
        base_url_input = st.text_input(
            "Enter API base URL (e.g., http://127.0.0.1:8000 or https://<ngrok_link>):",
            value=st.session_state.get("base_url", default_url)
        )
        submit_button = st.form_submit_button(label='Save')
        if submit_button:
            def update_base_url(new_url):
                if new_url:
                    clean_url = new_url.strip().rstrip("/")
                    st.session_state["base_url"] = clean_url
                    st.success(f"API base URL updated successfully to: {clean_url}")
                else:
                    st.warning("Please enter a valid URL.")
            update_base_url(base_url_input)
    st.markdown("---")
    st.write(f"**Current API Base URL:** {st.session_state.get('base_url', 'Not Set')}")
    
    st.markdown("##### Advanced Parameters")
    with st.form(key='advanced_params'):
        index_name_input = st.text_input(
            "Index Name",
            value=st.session_state.get("index_name", "7adf2fcf-5b92-4fae-8be0-b39fdd4380d1")
        )
        plain_input = st.selectbox(
            "Plain Retrieval - 1; Hierarchical Retrieval- 0;",
            options=[0, 1],
            index=0 if st.session_state.get("plain", 0) == 0 else 1
        )
        top_m_input = st.number_input(
            "Top M",
            min_value=1,
            step=1,
            value=st.session_state.get("top_m", 5)
        )
        top_n_input = st.number_input(
            "Top N",
            min_value=1,
            step=1,
            value=st.session_state.get("top_n", 3)
        )
        advanced_submit = st.form_submit_button(label="Save Advanced Params")
        if advanced_submit:
            st.session_state["index_name"] = index_name_input
            st.session_state["plain"] = int(plain_input)
            st.session_state["top_m"] = int(top_m_input)
            st.session_state["top_n"] = int(top_n_input)
            st.success("Advanced parameters saved.")
            
    st.markdown("##### Bot Prompt Configuration")
    with st.form(key='bot_prompt_form'):
        bot_prompt = st.text_area(
            "Enter the prompt to be sent in the payload:",
            value=st.session_state.get("bot_prompt", ""),
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
    st.markdown(f"<div class='preformatted'>{st.session_state.get('bot_prompt', 'Not Set')}</div>", unsafe_allow_html=True)


# Right Column: Chat Interface
with col2:
    st.header("Chat")
    
    # Define the callback that is triggered when Enter is pressed in the text input.
    def ask_bot():
        user_question = st.session_state.get("user_question", "")
        if user_question.strip() == "":
            st.warning("Please enter a question before asking the bot.")
        else:
            st.session_state["hybrid_chatHistory"].append({
                "role": "user",
                "content": user_question
            })
            base_url = st.session_state.get("base_url", "http://127.0.0.1:8000").rstrip('/')
            # Update the URL as needed.
            url_hBot = f"{base_url}/chatbotazure/retrieve-response-genbot/"
            # Use advanced parameters stored in session state
            index_name = st.session_state.get("index_name", "7adf2fcf-5b92-4fae-8be0-b39fdd4380d1")
            payload = {
                "question": user_question,
                "prompt": st.session_state.get("bot_prompt", ""),
                "chat_history": st.session_state["hybrid_chatHistory"],
                "index_name": index_name,
                "plain": st.session_state.get("plain", 0),
                "top_m": st.session_state.get("top_m", 5),
                "top_n": st.session_state.get("top_n", 3),
                "travel_form_details": st.session_state["travel_form_details"],
                "agent_form_details": st.session_state["agent_form_details"]
            }
            print("payload: ", json.dumps(payload, indent=3))
            print('-'*30)
            with st.spinner("Waiting for the Agentic Hybrid Bot to respond..."):
                try:
                    response = requests.post(url_hBot, json=payload)
                    response.raise_for_status()
                    response_data = response.json()
                    final_output = response_data.get("final_output", "")
                    # Update persistent form details
                    st.session_state["travel_form_details"] = response_data.get("travel_form_details", {})
                    st.session_state["agent_form_details"] = response_data.get("agent_form_details", {})
                    st.session_state["hybrid_chatHistory"].append({
                        "role": "assistant",
                        "content": final_output,
                        "full_response": response_data
                    })
                except Exception as e:
                    st.session_state["hybrid_chatHistory"].append({
                        "role": "assistant",
                        "content": "❌ Error: Unable to reach the Agentic Hybrid Bot. Please try again later.",
                        "full_response": {}
                    })
                    st.error(f"An error occurred: {e}")
            # Optionally clear the input after sending
            # st.session_state["user_question"] = ""
    
    # Create a text input that triggers the ask_bot callback when Enter is pressed.
    # st.text_input("Enter your question:", key="user_question", on_change=ask_bot)
    
    # Create a text input for the question
    st.text_input("Enter your question:", key="user_question")
    # Place the send button below the text input
    if st.button("Send 📨", key="send_button"):
        ask_bot()
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Conversation with Agentic Hybrid Bot")
    
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
        # st.markdown(container_style, unsafe_allow_html=True)
        # st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
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
                full_response = msg.get("full_response", {})
                with st.expander("🔍 Top References"):
                    # st.markdown(f"Pipeline: **{full_response['pipeline']}**")
                    # st.markdown(f"Standalone: **{full_response['standAloneQuestion']}**")
                    # st.markdown(f"Usage:")
                    # st.json(full_response['usage'])
                    # st.markdown(f"Time:")
                    # st.json(full_response['time'])
                    # if full_response.get("pageNumFilter"):
                    #     st.markdown(f"pageNumFilters:")
                    #     st.json(full_response['pageNumFilter'])
                    # st.markdown(f"travel_form_details: ")
                    # st.json(full_response["travel_form_details"])
                    # st.markdown(f"agent_form_details: ")
                    # st.json(full_response["agent_form_details"])
                    # st.markdown("Top References: ")
                    # st.json(full_response["top_references"])
                    # st.write("**Pipeline**:", full_response.get("pipeline", "N/A"))
                    # usage = full_response.get("usage", {})
                    # if usage:
                    #     st.write("**Usage**:")
                    #     st.json(usage)
                    # detailed_usage = full_response.get("detailed_usage", {})
                    # if detailed_usage:
                    #     st.write("**Detailed Usage**:")
                    #     st.json(detailed_usage)
                    # st.write("**Agent Form Details**:")
                    # st.json(full_response.get("agent_form_details", {}))
                    # st.write("**Travel Form Details**:")
                    # st.json(full_response.get("travel_form_details", {}))
                    # top_refs = full_response.get("top_references", [])
                    # sources = full_response.get("source", [])
                    # page_nos = full_response.get("pageNos", [])
                    # if top_refs and sources and page_nos and (len(top_refs) == len(sources) == len(page_nos)):
                    #     for i in range(len(top_refs)):
                    #         st.markdown(
                    #             f"**Reference {i+1}:** {top_refs[i]}<br>"
                    #             f"*Source:* `{sources[i]}` | *Page:* {page_nos[i]}",
                    #             unsafe_allow_html=True
                    #         )
                    # else:
                    #     st.info("No additional references available.")
                    # st.markdown(f"Standalone Question: {full_response['standaloneQuestion']}")
                    # st.markdown(f"Pipeline: {full_response['pipeline']}")
                    # st.markdown(f"PageNumFilters: {full_response['pageNumFilter']}")
                    # st.markdown("Usage: ")
                    # st.json(full_response["usage"])
                    # total_t = 0
                    # for time in full_response["time_taken"]:
                    #     total_t+=time["time"]
                    # st.markdown(f"Time Consumption: {total_t}")
                    # st.json(full_response["time_taken"])
                    # st.markdown("Detailed Usage: ")
                    st.json(full_response)
                    
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
        st.session_state["travel_form_details"] = {}
        st.session_state["agent_form_details"] = {}
        st.success("Hybrid Bot chat and form details have been cleared.")
    
    if 'asked_any_bot' not in st.session_state:
        st.session_state['asked_any_bot'] = False
    if st.session_state.get('asked_any_bot', False):
        st.markdown("""<script>window.scrollTo(0, document.body.scrollHeight);</script>""", unsafe_allow_html=True)
        st.session_state['asked_any_bot'] = False

