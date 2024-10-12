from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if query:
        return f'You searched for: {query}'
    else:
        return 'Please enter a search term.'

if __name__ == '__main__':
    app.run(debug=True)
