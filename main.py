import streamlit as st
import dashscope
from dashscope import Generation

# 设置你的API Key
dashscope.api_key = "sk-a6d3dd278db24255a26b915418265dd6"

st.title("AI人生智囊团")

st.write("输入你的人生问题，让AI智囊团给你建议")

question = st.text_area("请输入问题")


def ask_qwen(prompt):

    response = Generation.call(
        model="qwen-plus",
        prompt=prompt
    )

    return response.output.text
   
def summarize_advice(question, career, finance, psychology, startup):

    summary_prompt = f"""
你是一名人生决策顾问。

用户的问题：
{question}

以下是四位专家的建议：

职业导师：
{career}

财务顾问：
{finance}

心理导师：
{psychology}

创业顾问：
{startup}

请综合他们的观点：

1 给出一个清晰的人生建议
2 指出最重要的行动
3 控制在200字以内
"""

    response = Generation.call(
        model="qwen-plus",
        prompt=summary_prompt
    )

    return response.output.text

if st.button("获取建议"):

    if question:

        with st.spinner("AI智囊团正在思考..."):

            career_prompt = f"""
你是一名经验丰富的职业导师。

用户问题：
{question}

请从职业发展角度给出建议。
"""

            finance_prompt = f"""
你是一名理性的财务顾问。

用户问题：
{question}

请从财务风险和收入角度给出建议。
"""

            psychology_prompt = f"""
你是一名心理导师。

用户问题：
{question}

请从心理和情绪角度给出建议。
"""

            startup_prompt = f"""
你是一名创业顾问。

用户问题：
{question}

请从创业机会与风险角度给出建议。
"""

            career = ask_qwen(career_prompt)
            finance = ask_qwen(finance_prompt)
            psychology = ask_qwen(psychology_prompt)
            startup = ask_qwen(startup_prompt)

            st.subheader("职业导师")
            st.write(career)

            st.subheader("财务顾问")
            st.write(finance)

            st.subheader("心理导师")
            st.write(psychology)

            st.subheader("创业顾问")
            st.write(startup)
            
            summary = summarize_advice(
                question,
                career,
                finance,
                psychology,
                startup
            )
            st.subheader("最终建议")
            st.write(summary)

    else:
        st.warning("请先输入问题")