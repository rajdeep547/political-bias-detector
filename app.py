
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re

# --- Load Model ---
model_path = "./trilabel_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# --- Define Prediction Function ---
def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s.,!?\'"-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_bias(text):
    if not text or len(text.strip()) < 10:
        return "Please enter a longer article (minimum 10 characters)"
    
    text = clean_text(text)
    inputs = tokenizer(text, padding=True, truncation=True, max_length=128, return_tensors='pt')
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        pred = torch.argmax(outputs.logits, dim=1)
    
    label_map = {0: 'Left', 1: 'Neutral', 2: 'Right'}
    label = label_map[pred.item()]
    confidence = probs[0][pred.item()].item()
    probs = probs.cpu().numpy()
    
    # Create formatted output
    result = f"**Prediction: {label}**\n\n"
    result += f"**Confidence:** {confidence:.2%}\n\n"
    result += f"**Left:** {probs[0][0]:.2%}\n"
    result += f"**Neutral:** {probs[0][1]:.2%}\n"
    result += f"**Right:** {probs[0][2]:.2%}"
    
    return result

# --- Create and Launch Gradio Interface ---
interface = gr.Interface(
    fn=predict_bias,
    inputs=gr.Textbox(
        label="📝 Enter News Article",
        lines=6,
        placeholder="Paste your news article here..."
    ),
    outputs=gr.Markdown(label="📊 Results"),
    title="📰 Political Bias Detector",
    description="Enter a news article to detect its political bias (Left, Neutral, or Right).",
    examples=[
        ["The new healthcare reform will provide coverage to all Americans regardless of income. This progressive policy aims to reduce costs and improve access."],
        ["Tax cuts will stimulate the economy and benefit small businesses. We need to reduce government spending and regulation."],
        ["The bipartisan committee reached an agreement on the infrastructure bill with both parties making concessions."]
    ],
    theme="default"
)

# Launch the app
interface.launch()
