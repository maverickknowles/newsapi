from flask import Flask, request, render_template
import requests

app = Flask(__name__)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
api_key = "553ad8b749104d99b6aa7de7a2928614"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    url = f"https://newsapi.org/v2/everything?q={search_term}&pageSize=10&sortBy=relevancy&apiKey={api_key}"

    response = requests.get(url)
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(host='http://ec2-3-210-186-25.compute-1.amazonaws.com/', port=80)