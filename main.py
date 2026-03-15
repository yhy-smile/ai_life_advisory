import streamlit as st
import dashscope
from dashscope import Generation

# 设置你的API Key
dashscope.api_key = "sk-a6d3dd278db24255a26b915418265dd6"

st.set_page_config(page_title="AI人生智囊团", page_icon="🧠")

st.title("🧠 AI人生智囊团")

st.write("输入你的人生问题，让AI智囊团给你建议")

st.divider()

# 用户背景输入
question = st.text_area("你的人生问题")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input("年龄")

with col2:
    job = st.text_input("职业")

with col3:
    money = st.text_input("存款")

st.divider()


prompt = f"""
你是一个AI人生智囊团。

用户的问题：
{question}

用户背景：
年龄：{age}
职业：{job}
存款：{money}

请模拟四个导师，每个导师必须用以下结构回答：

【职业导师】

核心判断：
一句话判断用户当前阶段

行业趋势：
- 要点1
- 要点2
- 要点3

建议方向：
- 建议1
- 建议2
- 建议3

【财务顾问】

风险评估：
一句话说明风险

财务建议：
- 建议1
- 建议2
- 建议3


【心理导师】

心理状态分析：
一句话分析

建议：
- 建议1
- 建议2
- 建议3


【创业顾问】

创业可能性：
一句话判断

可尝试方向：
- 方向1
- 方向2
- 方向3


【最终建议】

总结用户最适合的方向。


【30天行动计划】

第1周：
第2周：
第3周：
第4周：

必须使用 Markdown 格式输出。
"""

def ask_qwen(prompt):

    response = Generation.call(
        model="qwen-plus",
        prompt=prompt
    )

    return response.output.text

if st.button("获取建议"):

    if question == "":
        st.warning("请输入问题")

    else:
        with st.spinner("AI智囊团正在思考..."):

            result = ask_qwen(prompt)

            st.divider()

            # 自动拆分AI输出
            sections = result.split("【")
            for section in sections:
                if section.strip() == "":
                    continue

                try:
                    title, content = section.split("】", 1)

                    st.subheader(title)

                    st.markdown(content.strip())

                    st.divider()

                except:
                    st.markdown(section)
