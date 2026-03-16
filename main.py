import streamlit as st
import dashscope
from dashscope import Generation

# API key
dashscope.api_key = st.secrets["DASHSCOPE_API_KEY"]

st.set_page_config(page_title="AI人生智囊团", page_icon="🧠")

st.title("🧠 AI人生智囊团")

st.write("输入你的人生问题，获得多位导师建议 + 人生决策报告")

st.divider()

# 用户输入
question = st.text_area("你的人生问题")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input("年龄")

with col2:
    job = st.text_input("职业")

with col3:
    money = st.text_input("存款")

st.divider()


def ask_qwen(prompt):

    response = Generation.call(
        model="qwen-plus",
        prompt=prompt
    )

    return response.output.text


# ===============================
# 生成导师建议
# ===============================

if st.button("获取导师建议"):

    if question == "":
        st.warning("请输入问题")

    else:

        with st.spinner("AI导师正在讨论..."):

            prompt = f"""
你是AI人生智囊团。

用户问题：
{question}

用户背景：
年龄：{age}
职业：{job}
存款：{money}

请模拟四个导师回答：

【职业导师】
分析职业发展并给出3条建议

【财务顾问】
分析财务状况并给出3条建议

【心理导师】
分析用户心理状态并给出建议

【创业顾问】
是否适合创业？给出方向

使用 Markdown 格式输出。
"""

            result = ask_qwen(prompt)

            st.markdown(result)

            st.session_state["question"] = question


# ===============================
# 生成人生决策报告
# ===============================

if st.button("生成完整人生决策报告"):

    if question == "":
        st.warning("请先输入问题")

    else:

        with st.spinner("AI正在生成决策报告..."):

            report_prompt = f"""
你是一位顶级人生规划顾问。

请为用户生成一份【人生决策报告】。

用户信息：

年龄：{age}
职业：{job}
存款：{money}

用户问题：
{question}

报告结构：

# 人生决策报告

## 一、问题本质分析
分析用户真正的问题

## 二、当前阶段判断
判断人生阶段

## 三、3种未来路径

### 路径1：稳健路线
优缺点

### 路径2：成长路线
优缺点

### 路径3：探索路线
优缺点

## 四、最推荐路线
给出理由

## 五、未来1年行动计划

### 第1阶段（1-3个月）
### 第2阶段（3-6个月）
### 第3阶段（6-12个月）

使用 Markdown 输出
"""

            report = ask_qwen(report_prompt)

            st.divider()

            st.subheader("📊 人生决策报告")

            st.markdown(report)