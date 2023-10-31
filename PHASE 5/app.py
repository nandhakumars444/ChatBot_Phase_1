from flask import Flask, request, render_template
import csv

app = Flask(__name__)

# Load the CSV dataset into a dictionary
chatbot_dataset = {}
with open('chatbot.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        chatbot_dataset[row['Question']] = row['Response']

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = chatbot_dataset.get(user_input, "I'm not sure how to respond to that.")
    return response

if __name__ == '__main__':
    app.run(debug=True)
