from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    input="AX에 대해서 설명해줘"
)

print(response.output_text)