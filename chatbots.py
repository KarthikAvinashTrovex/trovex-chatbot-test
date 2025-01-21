# import streamlit as st
# import requests

# # -------------------------------------------------------
# # 1) Define the initial chat history (same for all 3 bots)
# # -------------------------------------------------------
# initial_chat_history = [
#     {
#         "role": "user",
#         "content": "what happens in the event of death during the policy term"
#     },
#     {
#         "role": "assistant",
#         "content": "In the event of death during the policy term, the following implications apply: \nDeath Benefit: The nominee will receive the Sum Assured on Death, provided all premiums are paid up to date.\nPolicy Termination: The policy will terminate immediately upon the death of the Life Assured.\nClaim Process: The nominee must submit the necessary documents for the claim process as per Bajaj Allianz guidelines.\nIf you need more details about a specific policy, please let me know!"
#     },
#     {
#         "role": "user",
#         "content": "is this for all plans?"
#     },
#     {
#         "role": "assistant",
#         "content": "The implications and procedures in the event of death during the policy term can vary across different Bajaj Allianz plans. Each plan has specific terms regarding death benefits, eligibility, and claim processes. It’s essential to review the details of the specific policy you are interested in for accurate information"
#     },
#     {
#         "role": "user",
#         "content": "Can you tell me more about the benefits of the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Sure! Bajaj Allianz Life Insurance policies typically offer various benefits, including:\n\n1. **Death Benefit**: Provides financial protection to the nominee in case of the policyholder's demise during the policy term.\n\n2. **Maturity Benefit**: If the policyholder survives the policy term, they receive a lump sum amount.\n\n3. **Tax Benefits**: Premiums paid may be eligible for tax deductions under Section 80C, and the maturity or death benefits may be tax-free under Section 10(10D).\n\n4. **Surrender Benefit**: If the policy is surrendered after a specific period, the policyholder may receive a surrender value.\n\n5. **Rider Options**: Additional coverage options like accidental death benefits or critical illness cover can be added.\n\nPlease let me know if you want specific details about a particular policy!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more details about the death benefit offered by the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Certainly! The death benefit offered by Bajaj Allianz Life Insurance policies generally includes:\n\n1. **Sum Assured on Death**: This is the guaranteed amount paid to the nominee in the event of the policyholder's death during the policy term.\n\n2. **Total Premiums Paid**: If the policyholder passes away before the maturity date, the nominee may receive the total premiums paid, depending on the policy conditions.\n\n3. **Additional Benefits**: Some plans may offer additional benefits, such as bonuses, which can enhance the death benefit amount.\n\n4. **Claim Process**: The nominee must provide necessary documents like the death certificate, policy document, and identity proof for the claim to be processed smoothly.\n\n5. **No Reduction in Benefit**: The death benefit remains unaffected by any withdrawals made during the policy term, ensuring financial security for the nominee.\n\nIf you would like details about a specific plan's death benefit, please share the plan name!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more information about the benefits and features of Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "Absolutely! Bajaj Allianz Life Insurance policies come with a range of benefits and features designed to provide comprehensive protection and savings. Here are some key benefits:\n\n1. **Flexible Premium Payment Options**: Choose from single, limited, or regular premium payment modes based on your financial convenience.\n\n2. **Variety of Plans**: Options include term plans, endowment plans, ULIPs, and more, catering to diverse financial goals.\n\n3. **Death Benefit**: A guaranteed sum assured is paid to the nominee in the event of the policyholder's demise during the policy term.\n\n4. **Maturity Benefit**: If the policyholder survives the term, they receive a lump sum amount, which can include bonuses depending on the plan.\n\n5. **Tax Benefits**: Premiums paid are eligible for tax deductions under Section 80C, and benefits received are generally tax-free under Section 10(10D).\n\n6. **Riders**: Additional coverage options like critical illness, accidental death, and disability riders can enhance financial protection.\n\n7. **Surrender Value**: Policies may accumulate a surrender value after a certain period, providing liquidity if needed.\n\n8. **Loyalty and Bonus**: Many policies offer loyalty additions or bonuses that enhance the policy's value over time.\n\nIf you'd like more information about a specific product or feature, feel free to ask!"
#     },
#     {
#         "role": "user",
#         "content": "For future wealth gain, what is the minimum premium required for Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "The minimum premium required for Bajaj Allianz Life Insurance policies varies based on the type of policy you choose. Generally, it can start from as low as ₹2,000 to ₹5,000 annually or more, depending on the specific plan and its features.\n\nTo get precise information, please specify the particular policy you are interested in, and I can provide you with the minimum premium details!"
#     }
# ]

# # -------------------------------------------------------
# # 2) Initialize Session State for each bot's chat history
# # -------------------------------------------------------
# if "col1_chatHistory" not in st.session_state:
#     st.session_state["col1_chatHistory"] = initial_chat_history.copy()

# if "col2_chatHistory" not in st.session_state:
#     st.session_state["col2_chatHistory"] = initial_chat_history.copy()

# if "col3_chatHistory" not in st.session_state:
#     st.session_state["col3_chatHistory"] = initial_chat_history.copy()

# # -------------------------------------------------------
# # 3) Helper function to display chat messages
# #    - Assistant messages on the LEFT
# #    - User messages on the RIGHT
# # -------------------------------------------------------
# def display_chat(chat_history):
#     """
#     Display the conversation with assistant on the left,
#     and user on the right using basic HTML alignment.
#     """
#     for msg in chat_history:
#         if msg["role"] == "assistant":
#             st.markdown(
#                 f"<div style='text-align: left; background-color: #F0F0F0; "
#                 f"padding: 8px; margin: 5px 30% 5px 0; border-radius: 5px;'>"
#                 f"<b>Assistant:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )
#         elif msg["role"] == "user":
#             st.markdown(
#                 f"<div style='text-align: right; background-color: #D0F0FF; "
#                 f"padding: 8px; margin: 5px 0 5px 30%; border-radius: 5px;'>"
#                 f"<b>You:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )

# # -------------------------------------------------------
# # Streamlit Layout
# # -------------------------------------------------------
# st.title("Compare 3 Chatbots Side by Side")

# # Single user input for the question
# user_question = st.text_input("Enter your question for all 3 chatbots:")

# # A button to send the question to all bots
# if st.button("Ask All Bots"):
#     # Endpoints
#     url_nBot = "http://127.0.0.1:8000/chatbotazure/normal-bot-response/"
#     url_nBotMemory = "http://127.0.0.1:8000/chatbotazure/normal-bot-response-with-memory/"
#     url_hBot = "http://127.0.0.1:8000/chatbotazure/hybrid-bot-response/"
    
#     # Index name (common for two of the bots as per your requirement)
#     index_name_for_bots = "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8"

#     # 1) Call normal-bot
#     payload1 = {
#         "question": user_question,
#         "index_name": index_name_for_bots,
#         "chat_history": st.session_state["col1_chatHistory"]
#     }
#     try:
#         response1 = requests.post(url_nBot, json=payload1)
#         response1_data = response1.json()
#         # Only capture final_output & chat_history
#         final_output1 = response1_data.get("final_output", "")
#         updated_chat_history1 = response1_data.get("chat_history", [])

#         # Update session_state with the new chat history
#         st.session_state["col1_chatHistory"] = updated_chat_history1
#     except Exception as e:
#         final_output1 = f"Error calling nBot: {e}"

#     # 2) Call normal-bot-with-memory
#     payload2 = {
#         "question": user_question,
#         "index_name": index_name_for_bots,
#         "chat_history": st.session_state["col2_chatHistory"]
#     }
#     try:
#         response2 = requests.post(url_nBotMemory, json=payload2)
#         response2_data = response2.json()
#         # Only capture final_output & chat_history
#         final_output2 = response2_data.get("final_output", "")
#         updated_chat_history2 = response2_data.get("chat_history", [])

#         # Update session_state with the new chat history
#         st.session_state["col2_chatHistory"] = updated_chat_history2
#     except Exception as e:
#         final_output2 = f"Error calling nBotWithMemory: {e}"

#     # 3) Call hybrid-bot
#     payload3 = {
#         "question": user_question,
#         "chat_history": st.session_state["col3_chatHistory"]
#     }
#     try:
#         response3 = requests.post(url_hBot, json=payload3)
#         response3_data = response3.json()
#         # Only capture final_output & chat_history
#         final_output3 = response3_data.get("final_output", "")
#         updated_chat_history3 = response3_data.get("chat_history", [])

#         # Update session_state with the new chat history
#         st.session_state["col3_chatHistory"] = updated_chat_history3
#     except Exception as e:
#         final_output3 = f"Error calling hBot: {e}"

#     # If you want to show the raw final_output from each bot after each query,
#     # you could uncomment the lines below or handle them otherwise:
#     #
#     # st.write("Normal Bot Answer:", final_output1)
#     # st.write("Memory Bot Answer:", final_output2)
#     # st.write("Hybrid Bot Answer:", final_output3)

# # -------------------------------------------------------
# # 4) Display the chat histories in 3 columns
# # -------------------------------------------------------
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.subheader("Normal Bot")
#     display_chat(st.session_state["col1_chatHistory"])

# with col2:
#     st.subheader("Normal Bot + Memory")
#     display_chat(st.session_state["col2_chatHistory"])

# with col3:
#     st.subheader("Hybrid Bot")
#     display_chat(st.session_state["col3_chatHistory"])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import streamlit as st
# import requests

# # Set the page to wide mode
# st.set_page_config(layout="wide")

# # -------------------------------------------------------
# # 1) Define the initial chat history (same for all 3 bots)
# # -------------------------------------------------------
# initial_chat_history = [
#     {
#         "role": "user",
#         "content": "what happens in the event of death during the policy term"
#     },
#     {
#         "role": "assistant",
#         "content": "In the event of death during the policy term, the following implications apply: \nDeath Benefit: The nominee will receive the Sum Assured on Death, provided all premiums are paid up to date.\nPolicy Termination: The policy will terminate immediately upon the death of the Life Assured.\nClaim Process: The nominee must submit the necessary documents for the claim process as per Bajaj Allianz guidelines.\nIf you need more details about a specific policy, please let me know!"
#     },
#     {
#         "role": "user",
#         "content": "is this for all plans?"
#     },
#     {
#         "role": "assistant",
#         "content": "The implications and procedures in the event of death during the policy term can vary across different Bajaj Allianz plans. Each plan has specific terms regarding death benefits, eligibility, and claim processes. It’s essential to review the details of the specific policy you are interested in for accurate information"
#     },
#     {
#         "role": "user",
#         "content": "Can you tell me more about the benefits of the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Sure! Bajaj Allianz Life Insurance policies typically offer various benefits, including:\n\n1. **Death Benefit**: Provides financial protection to the nominee in case of the policyholder's demise during the policy term.\n\n2. **Maturity Benefit**: If the policyholder survives the policy term, they receive a lump sum amount.\n\n3. **Tax Benefits**: Premiums paid may be eligible for tax deductions under Section 80C, and the maturity or death benefits may be tax-free under Section 10(10D).\n\n4. **Surrender Benefit**: If the policy is surrendered after a specific period, the policyholder may receive a surrender value.\n\n5. **Rider Options**: Additional coverage options like accidental death benefits or critical illness cover can be added.\n\nPlease let me know if you want specific details about a particular policy!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more details about the death benefit offered by the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Certainly! The death benefit offered by Bajaj Allianz Life Insurance policies generally includes:\n\n1. **Sum Assured on Death**: This is the guaranteed amount paid to the nominee in the event of the policyholder's death during the policy term.\n\n2. **Total Premiums Paid**: If the policyholder passes away before the maturity date, the nominee may receive the total premiums paid, depending on the policy conditions.\n\n3. **Additional Benefits**: Some plans may offer additional benefits, such as bonuses, which can enhance the death benefit amount.\n\n4. **Claim Process**: The nominee must provide necessary documents like the death certificate, policy document, and identity proof for the claim to be processed smoothly.\n\n5. **No Reduction in Benefit**: The death benefit remains unaffected by any withdrawals made during the policy term, ensuring financial security for the nominee.\n\nIf you would like details about a specific plan's death benefit, please share the plan name!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more information about the benefits and features of Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "Absolutely! Bajaj Allianz Life Insurance policies come with a range of benefits and features designed to provide comprehensive protection and savings. Here are some key benefits:\n\n1. **Flexible Premium Payment Options**: Choose from single, limited, or regular premium payment modes based on your financial convenience.\n\n2. **Variety of Plans**: Options include term plans, endowment plans, ULIPs, and more, catering to diverse financial goals.\n\n3. **Death Benefit**: A guaranteed sum assured is paid to the nominee in the event of the policyholder's demise during the policy term.\n\n4. **Maturity Benefit**: If the policyholder survives the term, they receive a lump sum amount, which can include bonuses depending on the plan.\n\n5. **Tax Benefits**: Premiums paid are eligible for tax deductions under Section 80C, and benefits received are generally tax-free under Section 10(10D).\n\n6. **Riders**: Additional coverage options like critical illness, accidental death, and disability riders can enhance financial protection.\n\n7. **Surrender Value**: Policies may accumulate a surrender value after a certain period, providing liquidity if needed.\n\n8. **Loyalty and Bonus**: Many policies offer loyalty additions or bonuses that enhance the policy's value over time.\n\nIf you'd like more information about a specific product or feature, feel free to ask!"
#     },
#     {
#         "role": "user",
#         "content": "For future wealth gain, what is the minimum premium required for Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "The minimum premium required for Bajaj Allianz Life Insurance policies varies based on the type of policy you choose. Generally, it can start from as low as ₹2,000 to ₹5,000 annually or more, depending on the specific plan and its features.\n\nTo get precise information, please specify the particular policy you are interested in, and I can provide you with the minimum premium details!"
#     }
# ]

# # -------------------------------------------------------
# # 2) Initialize Session State for each bot's chat history
# # -------------------------------------------------------
# if "col1_chatHistory" not in st.session_state:
#     st.session_state["col1_chatHistory"] = initial_chat_history.copy()
# if "col2_chatHistory" not in st.session_state:
#     st.session_state["col2_chatHistory"] = initial_chat_history.copy()
# if "col3_chatHistory" not in st.session_state:
#     st.session_state["col3_chatHistory"] = initial_chat_history.copy()

# # -------------------------------------------------------
# # 3) Helper function to display chat messages
# #    with optional auto-scrolling
# # -------------------------------------------------------
# def display_chat(chat_history, container_id, scroll=False):
#     """
#     Display the conversation with assistant on the left,
#     and user on the right using basic HTML alignment.
#     Automatically scroll to the bottom if scroll=True.
#     """
#     # Add CSS for container
#     container_style = f"""
#     <style>
#     #{container_id} {{
#         max-height: 400px; /* Adjust as needed */
#         overflow-y: auto;
#         background-color: #FFFFFF;
#         padding: 5px;
#         border: 1px solid #ccc;
#     }}
#     </style>
#     """
#     st.markdown(container_style, unsafe_allow_html=True)

#     # Open container div
#     st.markdown(f"<div id='{container_id}'>", unsafe_allow_html=True)

#     # Display each message
#     for msg in chat_history:
#         if msg["role"] == "assistant":
#             st.markdown(
#                 f"<div style='text-align: left; background-color: #F0F0F0; "
#                 f"padding: 8px; margin: 5px 30% 5px 0; border-radius: 5px;'>"
#                 f"<b>Assistant:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )
#         elif msg["role"] == "user":
#             st.markdown(
#                 f"<div style='text-align: right; background-color: #D0F0FF; "
#                 f"padding: 8px; margin: 5px 0 5px 30%; border-radius: 5px;'>"
#                 f"<b>You:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )

#     # Close container div
#     st.markdown(f"</div>", unsafe_allow_html=True)

#     # Auto-scroll to the bottom
#     if scroll:
#         scroll_script = f"""
#         <script>
#         var container = document.getElementById('{container_id}');
#         container.scrollTop = container.scrollHeight;
#         </script>
#         """
#         st.markdown(scroll_script, unsafe_allow_html=True)


# # -------------------------------------------------------
# # Streamlit Layout - Single Input, 3 Buttons
# # -------------------------------------------------------
# st.title("Compare Chatbots Side by Side")

# # Optional check for auto-scrolling
# scroll_enabled = st.checkbox("Enable auto scrolling in each column", value=False)

# user_question = st.text_input("Enter your question:")
# st.write("Click one of the buttons below to ask a single bot at a time.")

# # Endpoints
# url_nBot = "http://127.0.0.1:8000/chatbotazure/normal-bot-response/"
# url_nBotMemory = "http://127.0.0.1:8000/chatbotazure/normal-bot-response-with-memory/"
# url_hBot = "http://127.0.0.1:8000/chatbotazure/hybrid-bot-response/"

# # Common index (as required)
# index_name_for_bots = "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8"

# # -------------------------------------------------------
# # 4) Three separate buttons to query each bot independently
# # -------------------------------------------------------
# col_button1, col_button2, col_button3 = st.columns(3)

# with col_button1:
#     if st.button("Ask Normal Bot"):
#         payload1 = {
#             "question": user_question,
#             "index_name": index_name_for_bots,
#             "chat_history": st.session_state["col1_chatHistory"]
#         }
#         try:
#             response1 = requests.post(url_nBot, json=payload1)
#             response1_data = response1.json()
#             updated_chat_history1 = response1_data.get("chat_history", [])
#             st.session_state["col1_chatHistory"] = updated_chat_history1
#         except Exception as e:
#             # Log error message in the chat as "assistant"
#             st.session_state["col1_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Normal Bot: {e}"
#             })

# with col_button2:
#     if st.button("Ask Normal Bot+Memory"):
#         payload2 = {
#             "question": user_question,
#             "index_name": index_name_for_bots,
#             "chat_history": st.session_state["col2_chatHistory"]
#         }
#         try:
#             response2 = requests.post(url_nBotMemory, json=payload2)
#             response2_data = response2.json()
#             updated_chat_history2 = response2_data.get("chat_history", [])
#             st.session_state["col2_chatHistory"] = updated_chat_history2
#         except Exception as e:
#             st.session_state["col2_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Normal Bot+Memory: {e}"
#             })

# with col_button3:
#     if st.button("Ask Hybrid Bot"):
#         payload3 = {
#             "question": user_question,
#             "chat_history": st.session_state["col3_chatHistory"]
#         }
#         try:
#             response3 = requests.post(url_hBot, json=payload3)
#             response3_data = response3.json()
#             updated_chat_history3 = response3_data.get("chat_history", [])
#             st.session_state["col3_chatHistory"] = updated_chat_history3
#         except Exception as e:
#             st.session_state["col3_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Hybrid Bot: {e}"
#             })

# # -------------------------------------------------------
# # 5) Display the chat histories in 3 wider columns
# # -------------------------------------------------------
# col1, col2, col3 = st.columns([1,1,1])  # 3 equal wide columns

# with col1:
#     st.subheader("Normal Bot")
#     display_chat(st.session_state["col1_chatHistory"], container_id="chat-container-1", scroll=scroll_enabled)

# with col2:
#     st.subheader("Normal Bot + Memory")
#     display_chat(st.session_state["col2_chatHistory"], container_id="chat-container-2", scroll=scroll_enabled)

# with col3:
#     st.subheader("Hybrid Bot")
#     display_chat(st.session_state["col3_chatHistory"], container_id="chat-container-3", scroll=scroll_enabled)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# import streamlit as st
# import requests

# # -----------------------------
# # 1) Page Config & Custom CSS
# # -----------------------------
# st.set_page_config(layout="wide")

# # Custom CSS for vertical dividers between columns, button styling, etc.
# custom_css = """
# <style>
# /* Vertical divider for columns */
# .column-wrapper {
#     border-right: 1px solid #ccc;
#     padding-right: 10px; /* space between content and divider */
# }
# .column-wrapper:last-child {
#     border-right: none;  /* remove right border on last column */
# }

# /* Style the "Ask" buttons slightly */
# div.stButton > button {
#     background-color: #007acc;
#     color: white;
#     border-radius: 6px;
#     border: 1px solid #005f99;
#     padding: 0.5em 1em;
#     cursor: pointer;
# }
# div.stButton > button:hover {
#     background-color: #0061a8;
# }

# /* Slight improvement for text_input to stand out */
# .css-16huue1.e1fqkh3o2 {
#     border: 1px solid #ccc;
# }

# /* Hide default horizontal lines that appear above columns (for a cleaner layout) */
# hr {
#     display: none !important;
# }
# </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

# # -------------------------------------------------------
# # 2) Define the initial chat history (same for all 3 bots)
# # -------------------------------------------------------
# initial_chat_history = [
#     {
#         "role": "user",
#         "content": "what happens in the event of death during the policy term"
#     },
#     {
#         "role": "assistant",
#         "content": "In the event of death during the policy term, the following implications apply: \nDeath Benefit: The nominee will receive the Sum Assured on Death, provided all premiums are paid up to date.\nPolicy Termination: The policy will terminate immediately upon the death of the Life Assured.\nClaim Process: The nominee must submit the necessary documents for the claim process as per Bajaj Allianz guidelines.\nIf you need more details about a specific policy, please let me know!"
#     },
#     {
#         "role": "user",
#         "content": "is this for all plans?"
#     },
#     {
#         "role": "assistant",
#         "content": "The implications and procedures in the event of death during the policy term can vary across different Bajaj Allianz plans. Each plan has specific terms regarding death benefits, eligibility, and claim processes. It’s essential to review the details of the specific policy you are interested in for accurate information"
#     },
#     {
#         "role": "user",
#         "content": "Can you tell me more about the benefits of the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Sure! Bajaj Allianz Life Insurance policies typically offer various benefits, including:\n\n1. **Death Benefit**: Provides financial protection to the nominee in case of the policyholder's demise during the policy term.\n\n2. **Maturity Benefit**: If the policyholder survives the policy term, they receive a lump sum amount.\n\n3. **Tax Benefits**: Premiums paid may be eligible for tax deductions under Section 80C, and the maturity or death benefits may be tax-free under Section 10(10D).\n\n4. **Surrender Benefit**: If the policy is surrendered after a specific period, the policyholder may receive a surrender value.\n\n5. **Rider Options**: Additional coverage options like accidental death benefits or critical illness cover can be added.\n\nPlease let me know if you want specific details about a particular policy!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more details about the death benefit offered by the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Certainly! The death benefit offered by Bajaj Allianz Life Insurance policies generally includes:\n\n1. **Sum Assured on Death**: This is the guaranteed amount paid to the nominee in the event of the policyholder's death during the policy term.\n\n2. **Total Premiums Paid**: If the policyholder passes away before the maturity date, the nominee may receive the total premiums paid, depending on the policy conditions.\n\n3. **Additional Benefits**: Some plans may offer additional benefits, such as bonuses, which can enhance the death benefit amount.\n\n4. **Claim Process**: The nominee must provide necessary documents like the death certificate, policy document, and identity proof for the claim to be processed smoothly.\n\n5. **No Reduction in Benefit**: The death benefit remains unaffected by any withdrawals made during the policy term, ensuring financial security for the nominee.\n\nIf you would like details about a specific plan's death benefit, please share the plan name!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more information about the benefits and features of Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "Absolutely! Bajaj Allianz Life Insurance policies come with a range of benefits and features designed to provide comprehensive protection and savings. Here are some key benefits:\n\n1. **Flexible Premium Payment Options**: Choose from single, limited, or regular premium payment modes based on your financial convenience.\n\n2. **Variety of Plans**: Options include term plans, endowment plans, ULIPs, and more, catering to diverse financial goals.\n\n3. **Death Benefit**: A guaranteed sum assured is paid to the nominee in the event of the policyholder's demise during the policy term.\n\n4. **Maturity Benefit**: If the policyholder survives the term, they receive a lump sum amount, which can include bonuses depending on the plan.\n\n5. **Tax Benefits**: Premiums paid are eligible for tax deductions under Section 80C, and benefits received are generally tax-free under Section 10(10D).\n\n6. **Riders**: Additional coverage options like critical illness, accidental death, and disability riders can enhance financial protection.\n\n7. **Surrender Value**: Policies may accumulate a surrender value after a certain period, providing liquidity if needed.\n\n8. **Loyalty and Bonus**: Many policies offer loyalty additions or bonuses that enhance the policy's value over time.\n\nIf you'd like more information about a specific product or feature, feel free to ask!"
#     },
#     {
#         "role": "user",
#         "content": "For future wealth gain, what is the minimum premium required for Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "The minimum premium required for Bajaj Allianz Life Insurance policies varies based on the type of policy you choose. Generally, it can start from as low as ₹2,000 to ₹5,000 annually or more, depending on the specific plan and its features.\n\nTo get precise information, please specify the particular policy you are interested in, and I can provide you with the minimum premium details!"
#     }
# ]

# # -----------------------------------
# # 3) Session State for Chat Histories
# # -----------------------------------
# if "col1_chatHistory" not in st.session_state:
#     st.session_state["col1_chatHistory"] = initial_chat_history.copy()
# if "col2_chatHistory" not in st.session_state:
#     st.session_state["col2_chatHistory"] = initial_chat_history.copy()
# if "col3_chatHistory" not in st.session_state:
#     st.session_state["col3_chatHistory"] = initial_chat_history.copy()

# # -------------------------------------------------------
# # 4) Helper function to display chat messages
# # -------------------------------------------------------
# def display_chat(chat_history, container_id, scroll=False):
#     """
#     Display the conversation with assistant on the left,
#     and user on the right. If scroll=True, we set up a 
#     container with overflow-y: auto so user can scroll.
#     """
#     # Container style to hold messages
#     container_style = f"""
#     <style>
#     #{container_id} {{
#         max-height: 450px; /* Adjust as needed */
#         overflow-y: auto;
#         background-color: #FFFFFF;
#         padding: 5px;
#         border: 1px solid #ccc;
#         margin: 0.5rem 0;
#     }}
#     </style>
#     """
#     st.markdown(container_style, unsafe_allow_html=True)

#     # Open container div
#     st.markdown(f"<div id='{container_id}'>", unsafe_allow_html=True)

#     # Display each message
#     for msg in chat_history:
#         if msg["role"] == "assistant":
#             st.markdown(
#                 f"<div style='text-align: left; background-color: #F0F0F0; "
#                 f"padding: 8px; margin: 5px 30% 5px 0; border-radius: 5px;'>"
#                 f"<b>Assistant:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )
#         elif msg["role"] == "user":
#             st.markdown(
#                 f"<div style='text-align: right; background-color: #D0F0FF; "
#                 f"padding: 8px; margin: 5px 0 5px 30%; border-radius: 5px;'>"
#                 f"<b>You:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )

#     # Close container div
#     st.markdown(f"</div>", unsafe_allow_html=True)

#     # If scroll is enabled, automatically scroll container
#     if scroll:
#         scroll_script = f"""
#         <script>
#         var container = window.parent.document.getElementById('{container_id}');
#         if (container) {{
#             container.scrollTop = container.scrollHeight;
#         }}
#         </script>
#         """
#         st.markdown(scroll_script, unsafe_allow_html=True)

# # -------------------------------------------------------
# # 5) Main Layout
# # -------------------------------------------------------
# st.title("Compare Chatbots Side by Side")

# # Checkbox to toggle auto scroll in each column
# scroll_enabled = st.checkbox("Enable auto scrolling in each column", value=False)

# user_question = st.text_input("Enter your question:", "")

# st.write("**Click one of the buttons below** to ask a single bot at a time.")

# # Endpoints
# url_nBot = "http://127.0.0.1:8000/chatbotazure/normal-bot-response/"
# url_nBotMemory = "http://127.0.0.1:8000/chatbotazure/normal-bot-response-with-memory/"
# url_hBot = "http://127.0.0.1:8000/chatbotazure/hybrid-bot-response/"

# # Common index (as required)
# index_name_for_bots = "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8"

# # ------------------------------
# # Buttons to query each endpoint
# # ------------------------------
# col_button1, col_button2, col_button3 = st.columns(3)

# asked_any_bot = False  # A flag to check if any button was pressed

# with col_button1:
#     if st.button("Ask Normal Bot"):
#         asked_any_bot = True
#         payload1 = {
#             "question": user_question,
#             "index_name": index_name_for_bots,
#             "chat_history": st.session_state["col1_chatHistory"]
#         }
#         try:
#             response1 = requests.post(url_nBot, json=payload1)
#             response1_data = response1.json()
#             updated_chat_history1 = response1_data.get("chat_history", [])
#             st.session_state["col1_chatHistory"] = updated_chat_history1
#         except Exception as e:
#             st.session_state["col1_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Normal Bot: {e}"
#             })

# with col_button2:
#     if st.button("Ask Normal Bot + Memory"):
#         asked_any_bot = True
#         payload2 = {
#             "question": user_question,
#             "index_name": index_name_for_bots,
#             "chat_history": st.session_state["col2_chatHistory"]
#         }
#         try:
#             response2 = requests.post(url_nBotMemory, json=payload2)
#             response2_data = response2.json()
#             updated_chat_history2 = response2_data.get("chat_history", [])
#             st.session_state["col2_chatHistory"] = updated_chat_history2
#         except Exception as e:
#             st.session_state["col2_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Normal Bot+Memory: {e}"
#             })

# with col_button3:
#     if st.button("Ask Hybrid Bot"):
#         asked_any_bot = True
#         payload3 = {
#             "question": user_question,
#             "chat_history": st.session_state["col3_chatHistory"]
#         }
#         try:
#             response3 = requests.post(url_hBot, json=payload3)
#             response3_data = response3.json()
#             updated_chat_history3 = response3_data.get("chat_history", [])
#             st.session_state["col3_chatHistory"] = updated_chat_history3
#         except Exception as e:
#             st.session_state["col3_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Hybrid Bot: {e}"
#             })

# # -------------------------------------------------------
# # 6) Display the chat histories in 3 columns with borders
# # -------------------------------------------------------
# columns = st.columns(3)
# column_titles = ["Normal Bot", "Normal Bot + Memory", "Hybrid Bot"]
# chat_ids = ["chat-container-1", "chat-container-2", "chat-container-3"]
# session_keys = ["col1_chatHistory", "col2_chatHistory", "col3_chatHistory"]

# for i, col in enumerate(columns):
#     with col:
#         st.markdown(
#             f"<div class='column-wrapper'>"
#             f"<h3 style='margin-top:0;'>{column_titles[i]}</h3>",
#             unsafe_allow_html=True
#         )
#         # Display chat in a container with ID
#         display_chat(
#             st.session_state[session_keys[i]],
#             container_id=chat_ids[i],
#             scroll=scroll_enabled
#         )
#         st.markdown("</div>", unsafe_allow_html=True)

# # -----------------------------------------
# # 7) Auto-scroll to page bottom if needed
# # -----------------------------------------
# # If any button was pressed, scroll to bottom of page.
# if asked_any_bot:
#     st.markdown(
#         """
#         <script>
#         window.scrollTo(0, document.body.scrollHeight);
#         </script>
#         """,
#         unsafe_allow_html=True
#     )




# import streamlit as st
# import requests

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
# }
# </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

# # -------------------------------------------------------
# # 2) Define the initial chat history (same for all 3 bots)
# # -------------------------------------------------------
# initial_chat_history = [
#     {
#         "role": "user",
#         "content": "what happens in the event of death during the policy term"
#     },
#     {
#         "role": "assistant",
#         "content": "In the event of death during the policy term, the following implications apply: \nDeath Benefit: The nominee will receive the Sum Assured on Death, provided all premiums are paid up to date.\nPolicy Termination: The policy will terminate immediately upon the death of the Life Assured.\nClaim Process: The nominee must submit the necessary documents for the claim process as per Bajaj Allianz guidelines.\nIf you need more details about a specific policy, please let me know!"
#     },
#     {
#         "role": "user",
#         "content": "is this for all plans?"
#     },
#     {
#         "role": "assistant",
#         "content": "The implications and procedures in the event of death during the policy term can vary across different Bajaj Allianz plans. Each plan has specific terms regarding death benefits, eligibility, and claim processes. It’s essential to review the details of the specific policy you are interested in for accurate information"
#     },
#     {
#         "role": "user",
#         "content": "Can you tell me more about the benefits of the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Sure! Bajaj Allianz Life Insurance policies typically offer various benefits, including:\n\n1. **Death Benefit**: Provides financial protection to the nominee in case of the policyholder's demise during the policy term.\n\n2. **Maturity Benefit**: If the policyholder survives the policy term, they receive a lump sum amount.\n\n3. **Tax Benefits**: Premiums paid may be eligible for tax deductions under Section 80C, and the maturity or death benefits may be tax-free under Section 10(10D).\n\n4. **Surrender Benefit**: If the policy is surrendered after a specific period, the policyholder may receive a surrender value.\n\n5. **Rider Options**: Additional coverage options like accidental death benefits or critical illness cover can be added.\n\nPlease let me know if you want specific details about a particular policy!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more details about the death benefit offered by the policy?"
#     },
#     {
#         "role": "assistant",
#         "content": "Certainly! The death benefit offered by Bajaj Allianz Life Insurance policies generally includes:\n\n1. **Sum Assured on Death**: This is the guaranteed amount paid to the nominee in the event of the policyholder's death during the policy term.\n\n2. **Total Premiums Paid**: If the policyholder passes away before the maturity date, the nominee may receive the total premiums paid, depending on the policy conditions.\n\n3. **Additional Benefits**: Some plans may offer additional benefits, such as bonuses, which can enhance the death benefit amount.\n\n4. **Claim Process**: The nominee must provide necessary documents like the death certificate, policy document, and identity proof for the claim to be processed smoothly.\n\n5. **No Reduction in Benefit**: The death benefit remains unaffected by any withdrawals made during the policy term, ensuring financial security for the nominee.\n\nIf you would like details about a specific plan's death benefit, please share the plan name!"
#     },
#     {
#         "role": "user",
#         "content": "Can you provide more information about the benefits and features of Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "Absolutely! Bajaj Allianz Life Insurance policies come with a range of benefits and features designed to provide comprehensive protection and savings. Here are some key benefits:\n\n1. **Flexible Premium Payment Options**: Choose from single, limited, or regular premium payment modes based on your financial convenience.\n\n2. **Variety of Plans**: Options include term plans, endowment plans, ULIPs, and more, catering to diverse financial goals.\n\n3. **Death Benefit**: A guaranteed sum assured is paid to the nominee in the event of the policyholder's demise during the policy term.\n\n4. **Maturity Benefit**: If the policyholder survives the term, they receive a lump sum amount, which can include bonuses depending on the plan.\n\n5. **Tax Benefits**: Premiums paid are eligible for tax deductions under Section 80C, and benefits received are generally tax-free under Section 10(10D).\n\n6. **Riders**: Additional coverage options like critical illness, accidental death, and disability riders can enhance financial protection.\n\n7. **Surrender Value**: Policies may accumulate a surrender value after a certain period, providing liquidity if needed.\n\n8. **Loyalty and Bonus**: Many policies offer loyalty additions or bonuses that enhance the policy's value over time.\n\nIf you'd like more information about a specific product or feature, feel free to ask!"
#     },
#     {
#         "role": "user",
#         "content": "For future wealth gain, what is the minimum premium required for Bajaj Allianz Life Insurance policies?"
#     },
#     {
#         "role": "assistant",
#         "content": "The minimum premium required for Bajaj Allianz Life Insurance policies varies based on the type of policy you choose. Generally, it can start from as low as ₹2,000 to ₹5,000 annually or more, depending on the specific plan and its features.\n\nTo get precise information, please specify the particular policy you are interested in, and I can provide you with the minimum premium details!"
#     }
# ]

# # -----------------------------------
# # 3) Session State for Chat Histories
# # -----------------------------------
# if "col1_chatHistory" not in st.session_state:
#     st.session_state["col1_chatHistory"] = initial_chat_history.copy()
# if "col2_chatHistory" not in st.session_state:
#     st.session_state["col2_chatHistory"] = initial_chat_history.copy()
# if "col3_chatHistory" not in st.session_state:
#     st.session_state["col3_chatHistory"] = initial_chat_history.copy()

# # -------------------------------------------------------
# # 4) Helper function to display chat messages
# # -------------------------------------------------------
# def display_chat(chat_history, container_id):
#     """
#     Display the conversation with assistant on the left,
#     and user on the right using basic HTML alignment.
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
#     for msg in chat_history:
#         if msg["role"] == "assistant":
#             st.markdown(
#                 f"<div style='text-align: left; background-color: #F0F0F0; "
#                 f"padding: 8px; margin: 5px 0; border-radius: 5px;'>"
#                 f"<b>Assistant:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )
#         elif msg["role"] == "user":
#             st.markdown(
#                 f"<div style='text-align: right; background-color: #D0F0FF; "
#                 f"padding: 8px; margin: 5px 0; border-radius: 5px;'>"
#                 f"<b>You:</b> {msg['content']}</div>",
#                 unsafe_allow_html=True
#             )
    
#     # Close container div
#     st.markdown(f"</div>", unsafe_allow_html=True)

# # -------------------------------------------------------
# # 5) Main Layout
# # -------------------------------------------------------
# st.title("Compare Chatbots Side by Side")

# # User input for the question
# user_question = st.text_input("Enter your question:", "")

# st.write("**Click one of the buttons below** to ask a single bot at a time.")

# # Endpoints
# url_nBot = "http://127.0.0.1:8000/chatbotazure/normal-bot-response/"
# url_nBotMemory = "http://127.0.0.1:8000/chatbotazure/normal-bot-response-with-memory/"
# url_hBot = "http://127.0.0.1:8000/chatbotazure/hybrid-bot-response/"

# # Common index (as required)
# index_name_for_bots = "b7cb8fce-97cb-44bb-b022-ddd0a2ee4ea8"

# # ------------------------------
# # Buttons to query each endpoint
# # ------------------------------
# col_button1, col_button2, col_button3 = st.columns(3)

# # Flag to determine if any bot was asked
# asked_any_bot = False

# with col_button1:
#     if st.button("Ask Normal Bot"):
#         asked_any_bot = True
#         payload1 = {
#             "question": user_question,
#             "index_name": index_name_for_bots,
#             "chat_history": st.session_state["col1_chatHistory"]
#         }
#         try:
#             response1 = requests.post(url_nBot, json=payload1)
#             response1_data = response1.json()
#             updated_chat_history1 = response1_data.get("chat_history", [])
#             st.session_state["col1_chatHistory"] = updated_chat_history1
#         except Exception as e:
#             # Log error message in the chat as "assistant"
#             st.session_state["col1_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Normal Bot: {e}"
#             })

# with col_button2:
#     if st.button("Ask Normal Bot + Memory"):
#         asked_any_bot = True
#         payload2 = {
#             "question": user_question,
#             "index_name": index_name_for_bots,
#             "chat_history": st.session_state["col2_chatHistory"]
#         }
#         try:
#             response2 = requests.post(url_nBotMemory, json=payload2)
#             response2_data = response2.json()
#             updated_chat_history2 = response2_data.get("chat_history", [])
#             st.session_state["col2_chatHistory"] = updated_chat_history2
#         except Exception as e:
#             st.session_state["col2_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Normal Bot + Memory: {e}"
#             })

# with col_button3:
#     if st.button("Ask Hybrid Bot"):
#         asked_any_bot = True
#         payload3 = {
#             "question": user_question,
#             "chat_history": st.session_state["col3_chatHistory"]
#         }
#         try:
#             response3 = requests.post(url_hBot, json=payload3)
#             response3_data = response3.json()
#             updated_chat_history3 = response3_data.get("chat_history", [])
#             st.session_state["col3_chatHistory"] = updated_chat_history3
#         except Exception as e:
#             st.session_state["col3_chatHistory"].append({
#                 "role": "assistant",
#                 "content": f"Error calling Hybrid Bot: {e}"
#             })

# # -------------------------------------------------------
# # 6) Display the chat histories in 3 columns with borders
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
# # 7) Auto-scroll to page bottom if needed
# # -----------------------------------------
# if asked_any_bot:
#     # Use a script to scroll to the bottom of the page
#     scroll_script = """
#     <script>
#     window.scrollTo(0, document.body.scrollHeight);
#     </script>
#     """
#     st.markdown(scroll_script, unsafe_allow_html=True)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


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
    {
        "role": "user",
        "content": "what happens in the event of death during the policy term"
    },
    {
        "role": "assistant",
        "content": "In the event of death during the policy term, the following implications apply: \nDeath Benefit: The nominee will receive the Sum Assured on Death, provided all premiums are paid up to date.\nPolicy Termination: The policy will terminate immediately upon the death of the Life Assured.\nClaim Process: The nominee must submit the necessary documents for the claim process as per Bajaj Allianz guidelines.\nIf you need more details about a specific policy, please let me know!"
    },
    {
        "role": "user",
        "content": "is this for all plans?"
    },
    {
        "role": "assistant",
        "content": "The implications and procedures in the event of death during the policy term can vary across different Bajaj Allianz plans. Each plan has specific terms regarding death benefits, eligibility, and claim processes. It’s essential to review the details of the specific policy you are interested in for accurate information"
    },
    {
        "role": "user",
        "content": "Can you tell me more about the benefits of the policy?"
    },
    {
        "role": "assistant",
        "content": "Sure! Bajaj Allianz Life Insurance policies typically offer various benefits, including:\n\n1. **Death Benefit**: Provides financial protection to the nominee in case of the policyholder's demise during the policy term.\n\n2. **Maturity Benefit**: If the policyholder survives the policy term, they receive a lump sum amount.\n\n3. **Tax Benefits**: Premiums paid may be eligible for tax deductions under Section 80C, and the maturity or death benefits may be tax-free under Section 10(10D).\n\n4. **Surrender Benefit**: If the policy is surrendered after a specific period, the policyholder may receive a surrender value.\n\n5. **Rider Options**: Additional coverage options like accidental death benefits or critical illness cover can be added.\n\nPlease let me know if you want specific details about a particular policy!"
    },
    {
        "role": "user",
        "content": "Can you provide more details about the death benefit offered by the policy?"
    },
    {
        "role": "assistant",
        "content": "Certainly! The death benefit offered by Bajaj Allianz Life Insurance policies generally includes:\n\n1. **Sum Assured on Death**: This is the guaranteed amount paid to the nominee in the event of the policyholder's death during the policy term.\n\n2. **Total Premiums Paid**: If the policyholder passes away before the maturity date, the nominee may receive the total premiums paid, depending on the policy conditions.\n\n3. **Additional Benefits**: Some plans may offer additional benefits, such as bonuses, which can enhance the death benefit amount.\n\n4. **Claim Process**: The nominee must provide necessary documents like the death certificate, policy document, and identity proof for the claim to be processed smoothly.\n\n5. **No Reduction in Benefit**: The death benefit remains unaffected by any withdrawals made during the policy term, ensuring financial security for the nominee.\n\nIf you would like details about a specific plan's death benefit, please share the plan name!"
    },
    {
        "role": "user",
        "content": "Can you provide more information about the benefits and features of Bajaj Allianz Life Insurance policies?"
    },
    {
        "role": "assistant",
        "content": "Absolutely! Bajaj Allianz Life Insurance policies come with a range of benefits and features designed to provide comprehensive protection and savings. Here are some key benefits:\n\n1. **Flexible Premium Payment Options**: Choose from single, limited, or regular premium payment modes based on your financial convenience.\n\n2. **Variety of Plans**: Options include term plans, endowment plans, ULIPs, and more, catering to diverse financial goals.\n\n3. **Death Benefit**: A guaranteed sum assured is paid to the nominee in the event of the policyholder's demise during the policy term.\n\n4. **Maturity Benefit**: If the policyholder survives the term, they receive a lump sum amount, which can include bonuses depending on the plan.\n\n5. **Tax Benefits**: Premiums paid are eligible for tax deductions under Section 80C, and benefits received are generally tax-free under Section 10(10D).\n\n6. **Riders**: Additional coverage options like critical illness, accidental death, and disability riders can enhance financial protection.\n\n7. **Surrender Value**: Policies may accumulate a surrender value after a certain period, providing liquidity if needed.\n\n8. **Loyalty and Bonus**: Many policies offer loyalty additions or bonuses that enhance the policy's value over time.\n\nIf you'd like more information about a specific product or feature, feel free to ask!"
    },
    {
        "role": "user",
        "content": "For future wealth gain, what is the minimum premium required for Bajaj Allianz Life Insurance policies?"
    },
    {
        "role": "assistant",
        "content": "The minimum premium required for Bajaj Allianz Life Insurance policies varies based on the type of policy you choose. Generally, it can start from as low as ₹2,000 to ₹5,000 annually or more, depending on the specific plan and its features.\n\nTo get precise information, please specify the particular policy you are interested in, and I can provide you with the minimum premium details!"
    }
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
