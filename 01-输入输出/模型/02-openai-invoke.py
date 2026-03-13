import dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI(
    model='qwen3.5-plus',
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
)

# 字符串
'''
response = llm.invoke("你是谁?")
print(response.content)
'''

# 消息列表
'''
messages = [
    SystemMessage(content="你是一名程序员。"),
    HumanMessage(content="你是谁?")
]
res = llm.invoke(messages)
print(res.content)

你好！我是一名程序员。👨‍💻
我的日常就是写代码、调试 Bug、设计架构，偶尔也跟产品经理“友好交流”一下需求。
无论是前端、后端、数据库还是算法问题，都可以跟我聊聊。有什么技术难题需要帮忙解决吗？
'''

# PromptValue对象
prompt = ChatPromptTemplate.from_template("讲一个关于{topic}的笑话")
prompt_value = prompt.invoke({"topic": "程序员"})
res = llm.invoke(prompt_value)
print(res.content)
