from http.client import responses

import openai
from openai import OpenAI, base_url
from pyexpat.errors import messages

from config import AI_TOKEN

client = OpenAI(api_key='sk-c2a507fa650a4127b06bab29291eb90e', base_url='https://api.deepseek.com')

response = client.chat.completions.create(
    model='deepseek-chat',
    messages=[
        {'role': 'system', 'content': 'you are a helpful assistant'},
        {'role': 'user', 'content': 'hello'}
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=True)

print(response.choices[0].message.content)