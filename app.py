from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', 
                         current_time=datetime.now().strftime('%H:%M:%S'),
                         current_date=datetime.now().strftime('%d %B %Y'))

if __name__ == '__main__':
    # host='0.0.0.0' çok önemli, yoksa Docker dışından siteye giremezsin.
    app.run(host='0.0.0.0', port=5000, debug=True)