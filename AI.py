from http.client import responses

import openai
from openai import OpenAI, base_url
from config import AI_TOKEN

client = OpenAI(api_key=AI_TOKEN, base_url='https://api.deepseek.com')

def chat_with_bot(prompt):
    try:
        response = openai.Completion.creat(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return print(f'Произошла ошибка {e}')

print('Боте  начало')
while True:
    user_input = input('ты : ')
    if user_input.lower() in ['стоп', 'пока', 'выход']:
        print('Бот пока! я ушел')
        break
    response = chat_with_bot(user_input)
    print(f'Бот:', {response})