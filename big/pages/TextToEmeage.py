'''
文生图大模型
'''

import streamlit as st
from zhipuai import ZhipuAI

st.title("菜就多看小程序🙌🙌🙌")

# 先构建智谱AI的大模型
model = ZhipuAI(api_key="dc463694d74db10ee0e816ff7f4a3e46.cbFX7aGzmbqR0mbI")

# 构建一个缓存，用来保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    # 需要从缓存中获取对话信息在界面上渲染 缓存两块内容 角色 角色的消息
    for message in st.session_state.cache:
        if message['role'] == "user":
            st.write(message["content"])
        else:
            with st.chat_message(message['role']):
                st.image(message["content"],width=200)

# 创建输入框
desc = st.chat_input("请输入图片的描述")
if desc:
    # 将用户输入的内容以角色输出到界面
    with st.chat_message("user"):
        st.write(desc)
    st.session_state.cache.append({"role": "user", "content": desc})
    # 调用智谱AI的文生图大模型生成图片
    response = model.images.generations(
        model="cogview-3-plus",  # 填写需要调用的模型编码
        prompt=desc,
    )
    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=200)
    st.session_state.cache.append({"role": "assistant", "content": response.data[0].url})