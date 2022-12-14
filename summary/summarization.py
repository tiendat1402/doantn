from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch
import streamlit as st
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

@st.cache(allow_output_mutation=True)
def load_token():
    tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\Admin\Downloads\datn\datn\summary\model")
    return tokenizer
def load_my_model():
    model = T5ForConditionalGeneration.from_pretrained(r"C:\Users\Admin\Downloads\datn\datn\summary\model")
    model = model.to(device)
    return model

model = load_my_model()
tokenizer = load_token()


def summarization(text):
    preprocess_text = text.strip().replace("\n", "")
    tokenized_text = tokenizer.encode(preprocess_text, return_tensors="pt").to(device)
    summary_ids = model.generate(
        tokenized_text,
        max_length=1024,
        num_beams=4,
        repetition_penalty=2.5,
        length_penalty=1.0,
        early_stopping=True
    )
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output
summarization(text="2022 - 2023 là năm đầu tiên chương trình giáo dục phổ thông mới áp dụng với lớp 10. Cùng với Âm nhạc, Mỹ thuật lần đầu tiên được đưa vào giảng dạy, với mục tiêu giúp học sinh nâng cao khả năng lựa chọn nghề nghiệp phù hợp với năng lực và sở thích. Môn học này còn gây chú ý khi có nhiều sách giáo khoa nhất với 11 cuốn trong bộ sách Kết nối tri thức với cuộc sống. Đây là điều chưa từng có tiền lệ với tất cả các khối lớp đã triển khai chương trình mới")