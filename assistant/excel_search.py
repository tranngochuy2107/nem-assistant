import pandas as pd
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_excel_data(file_path):
    df = pd.read_excel(file_path)
    return df

def search_product_with_ai(df, query):
    product_text = df.to_string(index=False)

    prompt = f"""
    Dưới đây là danh sách các sản phẩm nội thất của công ty:

    {product_text}

    Yêu cầu của khách hàng: "{query}"

    Hãy chọn ra sản phẩm phù hợp nhất, và trả lời theo mẫu sau:

    - Mã sản phẩm:
    - Tên sản phẩm:
    - Giá bán:
    - Mô tả sản phẩm (ngắn gọn):
    - Vì sao sản phẩm này phù hợp?
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",  # hoặc gpt-3.5-turbo nếu bạn dùng bản free
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
