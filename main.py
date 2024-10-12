from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

@app.route('/contents')
def contents():
    return render_template('contents.html')

@app.route('/featured_content')
def featured_content():
    return render_template('featured_content.html')

@app.route('/current_events')
def current_events():
    return render_template('current_events.html')

@app.route('/random_article')
def random_article():
    return render_template('random_article.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if query:
        return f'You searched for: {query}'
    else:
        return 'Please enter a search term.'

if __name__ == '__main__':
    app.run(debug=True)
