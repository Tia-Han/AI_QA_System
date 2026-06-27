"""
AI问答系统主应用

使用Streamlit构建用户界面，
提供问题输入、答案查询和历史记录查看功能。
"""

import streamlit as st
from matcher import match_question
from history import add_history, get_history, clear_history, get_history_count


# 页面配置
st.set_page_config(
    page_title="AI问答系统",
    page_icon="🤖",
    layout="centered"
)

# 标题
st.title("🤖 AI基础问答系统")
st.markdown("---")

# 输入区域
st.subheader("📝 提问区域")
user_question = st.text_input(
    "请输入您的问题:",
    placeholder="例如: 什么是人工智能？"
)

# 查询按钮
query_button = st.button("🔍 查询", type="primary")

# 回答区域
st.markdown("---")
st.subheader("💬 回答区域")

# 处理查询
if query_button and user_question:
    # 调用matcher获取答案
    answer = match_question(user_question)

    # 保存历史记录
    add_history(user_question, answer)

    # 显示回答
    st.success("✅ 查询成功!")
    st.write(f"**问题:** {user_question}")
    st.write(f"**答案:** {answer}")

# 历史记录区域
st.markdown("---")
st.subheader("📚 历史记录")

# 显示历史记录数量
history_count = get_history_count()
st.write(f"**历史记录总数:** {history_count}")

# 清空历史按钮
if st.button("🗑️ 清空历史记录"):
    clear_history()
    st.success("✅ 历史记录已清空!")
    st.rerun()

# 显示历史记录列表
history = get_history()
if history:
    for i, item in enumerate(history, 1):
        with st.expander(f"记录 #{i} - {item['timestamp']}"):
            st.write(f"**问题:** {item['question']}")
            st.write(f"**答案:** {item['answer']}")
else:
    st.info("暂无历史记录")

# 底部说明
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        AI问答系统 | 基于20条人工智能基础知识
    </div>
    """,
    unsafe_allow_html=True
)