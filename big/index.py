''''
streamlit多页面程序入口文件
'''

import streamlit as st
st.title("请选择你的英雄")

col, col1 = st.columns(2)

# 语言大模型应用程序入口
with col:
    st.image("http://gips1.baidu.com/it/u=1658389554,617110073&fm=3028&app=3028&f=JPEG&fmt=auto?w=1280&h=960", use_column_width=True)
    flag = st.button("晋中一言",use_container_width=True)
    if flag:
        st.switch_page("pages/damn02.py")
# 文生图大模型应用程序入口
with col1:
    st.image("http://gips3.baidu.com/it/u=3557221034,1819987898&fm=3028&app=3028&f=JPEG&fmt=auto?w=1280&h=960", use_column_width=True)
    flag = st.button("晋中一图",use_container_width=True)
    if flag:
        st.switch_page("pages/TextToEmeage.py")

# c1, c2, c3, c4= st.columns(4)
#
# with c1:
#     flag1 = st.button("基础版")
#     if flag1:
#         st.switch_page("pages/damn.py")
# with c2:
#     flag2 = st.button("进阶版")
#     if flag2:
#         st.switch_page("pages/damn01.py")
# with c3:
#     flag3 = st.button("最终版")
#     if flag3:
#         st.switch_page("pages/damn02.py")
# with c4:
#     flag4 = st.button("文生图")
#     if flag4:
#         st.switch_page("pages/TextToEmeage.py")
