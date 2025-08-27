import streamlit as st
from assistant.chat_engine import ask_chatgpt
from assistant.pdf_reader import extract_text_from_pdf
from assistant.excel_search import load_excel_data, search_product_with_ai
import os

# Cấu hình trang
st.set_page_config(page_title="NEM Assistant", layout="wide")
st.title("🤖 NEM Assistant – Trợ lý AI nội bộ cho Công ty Nội Thất NEM")

# ----- PHẦN 1: Đọc PDF + hỏi AI -----
st.markdown("## 📘 Hỏi AI từ tài liệu PDF")

uploaded_file = st.file_uploader("📎 Tải lên file PDF", type="pdf")

if uploaded_file:
    os.makedirs("data/uploads", exist_ok=True)
    file_path = os.path.join("data/uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf(file_path)
    st.success("✅ Đã xử lý nội dung từ file PDF")

    user_question = st.text_input("💬 Đặt câu hỏi về nội dung file PDF:")

    if user_question:
        response = ask_chatgpt(user_question, text)
        st.markdown("### 🧠 Trả lời từ AI:")
        st.write(response)

# ----- PHẦN 2: Tìm sản phẩm từ Excel -----
st.markdown("---")
st.markdown("## 🛍️ Tìm kiếm sản phẩm nội thất từ mô tả")

excel_file = st.file_uploader("📂 Tải lên file Excel sản phẩm", type=["xlsx", "xls"])

if excel_file:
    os.makedirs("data", exist_ok=True)
    excel_path = os.path.join("data", excel_file.name)
    with open(excel_path, "wb") as f:
        f.write(excel_file.read())

    df = load_excel_data(excel_path)
    st.success("✅ Đã đọc dữ liệu sản phẩm")

    product_query = st.text_input("💬 Nhập yêu cầu/mô tả sản phẩm bạn muốn tìm:")

    if product_query:
        result = search_product_with_ai(df, product_query)
        st.markdown("### 🔎 Kết quả gợi ý từ AI:")
        st.write(result)
