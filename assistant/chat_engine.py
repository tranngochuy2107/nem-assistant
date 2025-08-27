import openai
import os
from dotenv import load_dotenv

load_dotenv()  # ← Dòng này bắt buộc phải có
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatgpt(question, context=""):
    prompt = f"""
    Bạn là trợ lý AI của công ty nội thất NEM. Dưới đây là nội dung tài liệu khách hàng cung cấp:

    {context}

    Câu hỏi: {question}

    Trả lời bằng tiếng Việt, rõ ràng, dễ hiểu.
    """

    response = client.chat.completions.create(
        model="gpt-4",  # hoặc gpt-3.5-turbo
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content