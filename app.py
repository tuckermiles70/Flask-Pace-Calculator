from flask import Flask, render_template, request
from form import ComputeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

def calculatePace():
    # pace is distance / time
    print('We\'re calculating pace')
    pass
def calculateDistance():
    # distance is time / pace
    print('We\'re calculating distance')
    pass
def calculateTime():
    # time = distance * pace
    print('We\'re calculating time')
    pass

# Base url
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ComputeForm()
    if form.is_submitted():
        result = request.form # import request

        if result['hours'] != '' and result['minutes'] != '' and result['seconds'] != '':
            givenTime = True
        else:
            givenTime = False


        if result['distance'] != '' and givenTime and result['pace'] == '':
            calculatePace()
        elif result['pace'] != '' and givenTime and result['distance'] == '':
            calculateDistance()
        elif result['distance'] != '' and result['pace'] != '' and not givenTime:
            calculateTime()
        else:
            # error and die
            # raise ValueError('2 Fields must be completed and 1 must be blank!')
            print('2 Fields must be completed and 1 must be blank!')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)