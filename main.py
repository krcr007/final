from flask import Flask, render_template, request

app = Flask(__name__)

# Import your langchain_helper functions
from langchain_helper import get_qa_chain, create_vector_db

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_db', methods=['POST'])
def create_db():
    create_vector_db()
    return "Knowledgebase created successfully"

@app.route('/get_answer', methods=['POST'])
def get_answer():
    question = request.form.get('question')
    chain = get_qa_chain()
    response = chain(question)
    return response["result"]

if __name__ == '__main__':
    app.run(debug=True)
