from flask import Flask, request, render_template, redirect, url_for
import json
from crawler import *

app = Flask(__name__, static_folder='./static')
w3s = W3S_Crawler()
topic = ''
STATE = ''

@app.route('/learn', methods=['GET', 'POST'])
def getLang():
    global STATE, topic, w3s
    if STATE == 0:
        if request.method == 'POST':
            keyword_l = request.form['keyword']
            k, lang = hcrawler.legalChoice(keyword_l)
            if lang == None:
                return render_template('index.html')
            else:
                w3s.direct(f'https://www.w3schools.com{lang}')
                topic=k.upper()
                STATE = 1
                return render_template('lang.html', topic=topic)
    else:
        STATE = 0
        w3s.getChoice(topic.lower())
        if request.method == 'POST':
            keyword_l = request.form['keyword'].lower()
            keyword_l = keyword_l.replace('cpp', 'c++').replace('javascript', 'js')
            subs, title = w3s.legalChoice(keyword_l)
            if len(subs) + len(title) == 0:
                return render_template('index.html')
            else:
                return render_template('results.html', subs=subs, titles=title, ls=len(subs), lt=len(title))
    return render_template('index.html')
    
@app.route('/')
def aboutMe():
    return render_template('home.html')

if __name__ == '__main__':
    STATE = 0
    hcrawler = Header_Crawler()
    hcrawler.direct('https://www.w3schools.com/')
    hcrawler.getHeader()
    app.run(debug=True)
