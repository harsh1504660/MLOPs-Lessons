import streamlit as st

st.title("streamlit demo")

st.header("this is the header")
st.subheader("this is the sub header")

st.text("this is text")

st.success("success")
st.warning('warning')
st.info('info')
st.error('error')

if st.checkbox("select or unselect"):
    st.text("user hs select")
else :
    st.text("user dosnet selected")

state = st.radio("what is the fav colour" , ("red","greenn","blue"))

occupation = st.selectbox("what you do?",['user','dont know','your father '])

st.button("exampe button")

st.sidebar.header("heading of sidebar")
st.sidebar.text("textss")
