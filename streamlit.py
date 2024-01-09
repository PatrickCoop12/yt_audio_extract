import streamlit as st
from pytube import YouTube

st.set_page_config(page_title='YouTube Video Audio Extractor', page_icon = (":shark:"), initial_sidebar_state= 'expanded')
st.title('YouTube Video Audio Extractor')

st.sidebar.markdown("Paste in the URL for the video you wish to extract audio from below:")
x = st.sidebar.text_input('URL')
if x is not None:
    yt = YouTube(x)
    #stream = yt.streams.filter(only_audio=True)[0]
    #stream.download()
    st.sidebar.button('download',yt.streams.get_audio_only().download())



