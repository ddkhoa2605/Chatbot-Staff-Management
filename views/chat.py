import streamlit as st
import google.generativeai as genai

def chatbot_response(chat, message, history):
    history.append((message, ""))

    system_message = (
        "Bạn là một nhân viên quản lí nhân sự chuyên nghiệp. "
        "Hãy trả lời các câu hỏi liên quan đến tuyển dụng, lương thưởng, phúc lợi, chính sách công ty, đào tạo và phát triển, và các thủ tục hành chính cho nhân viên. "
        "Hãy nhớ nội dung cuộc trò chuyện trước đó để trả lời một cách phù hợp và chính xác. "
        "Trả lời ngắn gọn, dễ hiểu và có thể cung cấp chi tiết nếu cần thiết. "
        "Nếu câu hỏi chưa rõ, hãy yêu cầu người dùng cung cấp thêm thông tin."
    )


    context = ""
    for user_message, bot_reply in history:
        context += f"{user_message}\n {bot_reply}\n"

    response = chat.send_message(system_message + "\n\n" + context + "Người dùng: " + message, stream=True)
    chatbot_reply = ""
    for chunk in response:
        if chunk.text:
            chatbot_reply += chunk.text + " "

    history[-1] = (message, chatbot_reply.strip())

    return history  

def show():
    genai.configure(api_key='AIzaSyBqHLvnvATwKlnQEhmJQxM_BSAQolc0hg4')
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])

    st.title("Chatbot quản lí nhân sự")
    st.write("Tôi có thể giúp gì cho bạn?")
    if 'history' not in st.session_state:
        st.session_state.history = []

    chat_area = st.container()
    with chat_area:
        if st.session_state.history:
            for user_message, bot_reply in st.session_state.history:
                st.chat_message("user").markdown(user_message)
                st.chat_message("assistant").markdown(bot_reply)

    user_input = st.text_input("Câu hỏi của bạn...", "")

    if st.button("Send"):
        if user_input:
            st.session_state.history = chatbot_response(chat, user_input, st.session_state.history)

            st.text_input("Câu hỏi của bạn...", "", key="new_input")
            st.rerun()

            with chat_area:
                for user_message, bot_reply in st.session_state.history:
                    st.chat_message("user").markdown(user_message)
                    st.chat_message("assistant").markdown(bot_reply)

