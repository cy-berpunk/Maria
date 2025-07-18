from flask import Flask, render_template
import random

app = Flask(__name__)

words = ["汝の敵を愛せよ",
         "富は天の国に積め",
         "貧しい者は幸いである",
         "義のために迫害された人々は幸いである",
         "主に感謝し、その名をほめたたえよ",
         "人を裁くな。裁かれないためである",
         "強く、雄々しくあれ",
         "自分を高くする者は低くされ、自分を低くする者は高くされるだろう",
         "もろもろの天は神の栄光をあらわし、大空はみ手のわざをしめす",
         "神は「光あれ」と言われた。すると光があった。",
         ]

@app.route('/')
def display_random_word():
    random_word = random.choice(words)
    return render_template('index.html', word=random_word)

@app.route('/')
def show_image():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)