from flask import Flask, render_template
import random

app = Flask(__name__)

words = ["汝の敵を愛せよ",
         "富は天の国に積め",
         "貧しい者は幸いである",
         "強く、雄々しくあれ",
         "自分を高くする者は低くされ、自分を低くする者は高くされるだろう",
         "もろもろの天は神の栄光をあらわし、大空はみ手のわざをしめす",
         "御名があがめられますように",
         "主の旗にむかって手を上げる、主は世々アマレクと戦われる",
         ]

@app.route('/')
def display_random_word():
    random_word = random.choice(words)
    return render_template('index.html', word=random_word)

if __name__ == '__main__':
    app.run(debug=True)