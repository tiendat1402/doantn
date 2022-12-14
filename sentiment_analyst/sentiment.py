import torch
from transformers import AutoTokenizer
#from vncorenlp import VnCoreNLP
import os
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\Admin\Downloads\datn\datn\sentiment_analyst\tokenizer")
def model_fn(model_dir, model_name="model.pt"):
    print("model_fn_sentiment")
    return torch.jit.load(os.path.join(model_dir, model_name), map_location=device)
model_dir = r"C:\Users\Admin\Downloads\datn\datn\sentiment_analyst\model"
model = model_fn(model_dir)
def sentiment_analyzer(input_text):
    max_sequence_length = 256
    input_dict = tokenizer.encode_plus(
        input_text,
        max_length=max_sequence_length,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )
    inputs = {
        "input_ids": torch.tensor(input_dict["input_ids"]).to(device),
        "attention_mask": torch.tensor(input_dict["attention_mask"]).to(device),
    }
    model.to(device)
    model.eval()
    with torch.no_grad():
        predictions, *_ = model(**inputs)
        predictions = torch.argmax(predictions, dim=1).flatten()
        predictions = predictions.detach().cpu().numpy()

    label_map = ["Negative", "Neutral", "Positive"]
    const = label_map[predictions[0]]
    return const
