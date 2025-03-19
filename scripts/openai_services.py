import openai
import os
from dotenv import load_dotenv
from constants import validations

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

mensagem = "Henrique"
regras = validations.QUESTAO_1

prompt = f"""
{regras}

Nome informado: '{mensagem}'

Apenas responda `TRUE` ou `FALSE` sem explicações.
"""

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "Você é um validador de nomes. Responda apenas `TRUE` ou `FALSE`, sem explicações."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150,
    temperature=0.8
)

print(response.choices[0].message.content)
