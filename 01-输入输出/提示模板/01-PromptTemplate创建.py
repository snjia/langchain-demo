from langchain_core.prompts import PromptTemplate

'''
prompt = PromptTemplate.from_template("用{topic}写一首五言绝句")
print(type(prompt), prompt)
# <class 'langchain_core.prompts.prompt.PromptTemplate'>
# input_variables=['topic'] input_types={} partial_variables={} template='用{topic}写一首五言绝句'
'''


prompt = PromptTemplate(
    input_variables=['topic'],
    template="用{topic}写一首五言绝句"
)
formatted_prompt = prompt.format(topic="春天")
print(type(formatted_prompt), formatted_prompt)
# <class 'str'>
# 用春天写一首五言绝句