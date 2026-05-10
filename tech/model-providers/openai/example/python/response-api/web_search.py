from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    tools=[{"type": "web_search"}],
    input="AX 기술 관련 최신 트랜드를 분석해줘"
)

print(response.output_text)