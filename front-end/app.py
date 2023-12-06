from flask import Flask, jsonify, request
import summarization_model as sm

app = Flask(__name__)

model = None
tokenizer = None

def load_model():
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )

    name = "Undi95/Mistral-11B-OmniMix9"
    model = AutoModelForCausalLM.from_pretrained(name, quantization_config = quantization_config)
    tokenizer = AutoTokenizer.from_pretrained(name)

if model is None or tokenizer is None:
    load_model()

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello from Flask API!')

@app.route('/api/create-summary', methods=['POST'])
def create_summary():
    try:
        data = request.json
        input_text = data['input_text']

        summary = sm.model_inference(input_text)

        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
