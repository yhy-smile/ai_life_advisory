import requests
import streamlit as st
# 设置Ollama的本地API地址
API_URL = "http://localhost:11434/api/generate"

# 设置Ollama模型名称（例如你下载的模型名）
MODEL_NAME = "huihui_ai/deepseek-r1-abliterated:8b"

st.title("AI人生智囊团")

st.write("输入你的人生问题，让AI智囊团给你建议")

question = st.text_area("请输入问题")

def ask_local_model(model_name, prompt):
    """向本地Ollama模型发送请求并返回响应"""
    response = requests.post(
        API_URL,
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        }
    )

    # 打印返回的JSON数据，确认结构
    print("Response JSON:", response.json())

    # 检查返回的JSON是否包含正确的字段
    try:
        return response.json()["response"]
    except KeyError:
        # 如果没有 "response" 字段，可以返回原始数据
        return f"Error: {response.json()}"

if st.button("获取建议"):
    if question:
        with st.spinner("AI智囊团正在思考..."):

            # 准备角色的Prompt
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

            # 使用本地模型获取每个角色的建议
            career = ask_local_model(MODEL_NAME, career_prompt)
            finance = ask_local_model(MODEL_NAME, finance_prompt)
            psychology = ask_local_model(MODEL_NAME, psychology_prompt)
            startup = ask_local_model(MODEL_NAME, startup_prompt)

            # 显示每个角色的建议
            st.subheader("职业导师")
            st.write(career)

            st.subheader("财务顾问")
            st.write(finance)

            st.subheader("心理导师")
            st.write(psychology)

            st.subheader("创业顾问")
            st.write(startup)
    else:
        st.warning("请先输入问题")