from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk import pos_tag

app = Flask(__name__)


def is_ai_generated(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    noun_count = sum(1 for word, tag in tagged if tag.startswith('NN'))
    word_count = len(tokens)

    if word_count == 0:
        return "No text entered"

    if noun_count / word_count > 0.3:
        return "Possibly AI-Generated"
    else:
        return "Likely Human-Written"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        user_text = request.form['text']
        result = is_ai_generated(user_text)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
