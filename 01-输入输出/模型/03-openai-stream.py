import dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI(
    model='qwen3.5-plus',
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
)

for chunk in llm.stream("你是谁?"):
    print(chunk.content, end="")
