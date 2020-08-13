from flask import Flask, render_template
from form import ComputeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

# Base url
@app.route('/')
def index():
    # return render_template('index.html')
    form = ComputeForm()
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)