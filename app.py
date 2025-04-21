# app.py

from flask import Flask, request, jsonify
from flask import render_template
from chatbot import get_response
from ocr_utils import extract_text_from_image
from summary import generate_order_summary

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = get_response(user_message)
    return jsonify({"reply": reply})

@app.route("/upload", methods=["POST"])
def upload_image():
    image_file = request.files['image']
    image_path = f"temp_image.jpg"
    image_file.save(image_path)

    # Extract text from image
    extracted_text = extract_text_from_image(image_path)
    items = extracted_text.split('\n')
    items = [item for item in items if item.strip() != ""]

    summary = generate_order_summary(items)
    return jsonify({
        "extracted_items": items,
        "summary": summary
    })

if __name__ == "__main__":
    app.run(debug=True)
