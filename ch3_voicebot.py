# #4,5,6,7,8,9
# import streamlit as st
# import openai
# import os
# from datetime import datetime
# from audiorecorder import audiorecorder
# from gtts import gTTS
# import base64
# import pydub

# # FFmpeg 및 ffprobe의 경로를 설정합니다.
# pydub.AudioSegment.ffmpeg = "C:/Users/qkrdm/Downloads/ffmpeg-6.1.1-essentials_build/ffmpeg-6.1.1-essentials_build/bin/ffmpeg.exe"
# pydub.AudioSegment.ffprobe = "C:/Users/qkrdm/Downloads/ffmpeg-6.1.1-essentials_build/ffmpeg-6.1.1-essentials_build/bin/ffprobe.exe"

# def STT(audio, apikey):
#     filename='input.mp3'
#     audio.export(filename, format="mp3")
    
#     audio_file = open(filename,"rb")
#     client= openai.OpenAI(api_key=apikey)
#     response=client.audio.transcriptions.create(model="whisper-1",file=audio_file)
#     audio_file.close()
    
#     os.remove(filename)
#     return response.text

# def ask_gpt(prompt, model, apikey):
#     client = openai.OpenAI(api_key =apikey)
#     response=client.chat.completions.create(
#         model=model,
#         messages=prompt
#     )
#     gptResponse = response.choices[0].message.content
#     return gptResponse

# def TTS(response):
#     filename="output.mp3"
#     tts=gTTS(text=response,lang="ko")
#     tts.save(filename)
    
#     with open(filename,"rb")as f:
#         data = f.read()
#         b64=base64.b64encode(data).decode()
#         md = f"""

#             <audio autoplay="True">
#             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#             </audio>
        
#             """
#         st.markdown(md, unsafe_allow_html=True,)
#     os.remove(filename)
# def main():
    
#     st.set_page_config(
#         page_title="음성 비서 프로그램",
#         layout="wide"
#     )
    
#     if "chat" not in st.session_state:
#         st.session_state["chat"]=[]
        
#     if "OPENAI_API" not in st.session_state:
#         st.session_state["OPENAI_API"]=""
        
#     if "messages" not in st.session_state:
#         st.session_state["messages"]=[{"role":"system","content":"You are a thoughtful assistant. Respond to all input in 25words and answer in korea"}]
        
#     if "check_audio" not in st.session_state:
#         st.session_state["check_reset"]=False
        
#     st.header("음성 비서 프로그램")
    
#     st.markdown("---")
    
#     with st.expander("음성비서 프로그램에 관하여", expanded=True):
#         st.write(
#     """ 
#     - 음성비서 프로그램의 UI는 스트림릿을 화라용하여 만들었습니다.
#     - STT(Speech-To-Text)는 OpenAI의 Whisper AI를 활용하였습니다.
#     - 답변은 OpenAIdml GTP 모델을 활용하였습니다.
#     - TTS(Text-To-Speech)는 구글의 Google Translate TTS를 활용하였습니다.
#     """
#     )
        
#     st.markdown("")
    
    
    
    
#     with st.sidebar:
        
#         st.session_state["OPENAI_API"]=st.text_input(label="OPENAI API 키", placeholder="Enter your API key", value="",type="password")
        
#         st.markdown("---")
        
#         model = st.radio(label="GPT 모델", options=["gpt-4", "gpt-3.5-turbo"])
        
#         st.markdown("---")
        
#         if st.button(label="초기화"):
#             st.session_state["chat"]=[]
#             st.session_state["messages"]=[{"role":"system","content":"You are a thoughtful assistant. Respond to all input in 25 words and answer in korean"}]
#             st.session_state["check_reset"]=True

            
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("질문하기")
#         audio = audiorecorder("클릭하여 녹음하기","녹음 중...")
#         if (audio.duration_seconds >0) and (st.session_state["check_reset"]==False):
#             st.audio(audio.export().read())
#             question= STT(audio, st.session_state["OPENAI_API"])
            
#             now = datetime.now().strftime("%H:%M")
#             st.session_state["chat"]=st.session_state["chat"]+[{"user",now,question}]
#             st.session_state["messages"]=st.session_state["messages"]+[{"role":"user","content":question}]
        
#     with col2:
#         st.subheader("질문/답변")
#         if(audio.duration_seconds>0)and (st.session_state["check_reset"]==False):
#             response =ask_gpt(st.session_state["messages"], model, st.session_state["OPENAI_API"])
#             st.session_state["messages"]=st.session_state["messages"]+[{"role":"assistant","content":response}]
#             now= datetime.now().strftime("%H:%M")
#             st.session_state["chat"]=st.session_state["chat"]+[("bot", now,response)]
            
#             for sender, time, message in st.session_state["chat"]:
#                 if sender == "user":
#                     st.write(f'<div style="display:flex; align-items:center;"><div style="background-color: #007AFF; color:white; border-radius:12px; padding:8px 12px; margin-right:8px;">{message}</div><div style="font-size:0.8rem; color:gray;">{time}</div></div>', unsafe_allow_html=True)
#                     st.write("")
#                 else:
#                     st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
#                     st.write("")
#             TTS(response)
        
# if __name__=="__main__":
#     main()


#팀플 코드

#apikey = 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
import streamlit as st
from audiorecorder import audiorecorder
import openai
import os
from datetime import datetime

def STT(audio, apikey):
    filename = "input.mp3"
    audio.export(filename, format="mp3")
    
    audio_file = open(filename, "rb")
    client=openai.OpenAI(api_key = apikey)
    response = client.audio.transcriptions.create(model="whisper-1", file = audio_file)
    audio_file.close()
    os.remove(filename)
    return response.text

def ask_gpt(prompt, model, apikey):
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model=model,
        messages=prompt)
    gptResponse = response.choices[0].message.content
    return gptResponse

def main():

    st.set_page_config(
        page_title="당신의 열받는 대화 친구",
        layout="wide")
    
    if "chat" not in st.session_state:
        st.session_state["chat"] = []
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role":"system", "content":"You are Nilanilla Vanillaria II of the Kingdom of Vanilla, an Orthodox descendant of the Kingdom of Vanilla. You speak in a fantasy historical drama style, and you must speak in Korean."}]
    if "check_audio" not in st.session_state:
        st.session_state["check_reset"] = False
    
    st.title("✨ 닐라닐라 바닐라리아 2세 ✨")

    st.markdown("---")

    with st.expander("자기소개", expanded=True):
        st.write(
        """

        짐은 바닐라 왕국의 닐라닐라 바닐라리아 2세, 바닐라 왕국의 정통 후손으로서, 
        모두에게 나의 존재와 함께하는 기쁨을 전하고자 하는 바램이 있다.
        함께 이 땅을 빛나게 만들어 나가자, 당신과 나, 우리 모두의 힘을 모아!

        > - 202004052 박은빈, 202204252 이성민
        """
        )

        st.markdown("")

    with st.sidebar:
        st.session_state["OPENAI_API"] = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key", value="", type="password")

        st.markdown("---")

        model = st.selectbox(label='GPT모델', options=['gpt-3.5-turbo', 'gpt-4'])

        if st.button(label="초기화"):
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role":"system", "content":"You are Nilanilla Vanillaria II of the Kingdom of Vanilla, an Orthodox descendant of the Kingdom of Vanilla. You speak in a fantasy historical drama style, and you must speak in Korean."}]
            st.session_state["check_reset"] = True

        st.markdown("---")
        color_var = st.color_picker("대화 창의 색상을 선택해보세요", "#ffd700")
        
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("음성으로 질문하기")
        audio = audiorecorder("음성 질문", "녹음 중•••")
        if (audio.duration_seconds > 0) and (not st.session_state["check_reset"]):
            st.audio(audio.export().read())
            question = STT(audio, st.session_state["OPENAI_API"])
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] = st.session_state["chat"] + [("user", now, question)]
            st.session_state["messages"] = st.session_state["messages"] + [{"role": "user", "content": question}]
        
        st.subheader("텍스트로 질문하기")
        user_input = st.text_input(label="닐라닐라 바닐라리아 2세에게 질문하기", placeholder="텍스트로 질문 ", value="", key="user_input")
        tB=st.button("텍스트 질문")
        if tB:
            if user_input and (not st.session_state["check_reset"]):
                now = datetime.now().strftime("%H:%M")
                st.session_state["chat"] = st.session_state["chat"] + [("user", now, user_input)]
                st.session_state["messages"] = st.session_state["messages"] + [{"role": "user", "content": user_input}]

    with col2:
        st.subheader("질문/답변")
        response = None
        if (audio.duration_seconds > 0) and (not st.session_state["check_reset"]):
            response = ask_gpt(st.session_state["messages"], model, st.session_state["OPENAI_API"])
        elif user_input and (not st.session_state["check_reset"]):
            response = ask_gpt(st.session_state["messages"], model, st.session_state["OPENAI_API"])
            
        if response:
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] = st.session_state["chat"] + [("bot", now, response)]
            st.session_state["messages"] = st.session_state["messages"] + [{"role": "system", "content": response}]
            
            for sender, time, message in st.session_state["chat"]:
                if sender == "user":
                    color_var = color_var
                    st.write(f"""<div style="display:flex;align-items:center;justify-content:flex-end;">
                            <div style="background-color:{color_var};border-radius:12px;padding:8px 12px;margin-left:8px;">
                            {message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>""", unsafe_allow_html=True)                    
                    st.write("")
                else:
                    st.write(f"""<div style="display:flex;align-items:center;justify-content:flex-end;">
                            <div style="background-color:;border-radius:12px;padding:8px 12px;margin-left:8px;">
                            {message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>""", unsafe_allow_html=True)
                    st.write("")
            tB = False
if __name__=="__main__":
    main()