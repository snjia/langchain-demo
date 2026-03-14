from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model='qwen3.5-plus',
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
)

for chunk in llm.stream("你是谁?"):
    print(chunk.content, end="")
