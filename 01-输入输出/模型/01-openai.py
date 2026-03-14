from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model='qwen3.5-plus',
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
)

response = llm.invoke("你是谁?")
print(response.content)

'''
你好呀！我是 **Qwen3.5**，阿里巴巴最新推出的通义千问大语言模型。我能够帮你回答问题、创作文字、编写代码、分析文档，甚至处理多语言任务和专业领域的复杂问题。比如：
- 📚 **超长上下文**：轻松处理数十万字的文档或长对话；
- 🌍 **多语言支持**：流畅使用全球 100+ 主流语言；
- 🧠 **深度推理**：擅长数学、逻辑、科学问题的拆解与解答；
- 💻 **代码全栈**：从生成到调试，支持多种编程语言；
- 🖼️ **视觉理解**：能分析图表、公式、科学图示等复杂内容。

有什么具体任务需要我协助吗？随时告诉我！ 😊
'''