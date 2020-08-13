from flask import Flask, render_template, request
from form import ComputeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

def calculatePace(result):
    # pace is distance / time
    print('We\'re calculating pace')

    totalseconds = 0
    totalseconds += int(result['hours']) * 3600
    totalseconds += int(result['minutes']) * 60
    totalseconds += int(result['seconds'])

    distance = float(result['distance'])

    print('Distance: {}\nTime: {}\n'.format(distance, totalseconds))
    print('Pace is {} seconds per mile'.format(totalseconds / distance))
    
def calculateDistance(result):
    # distance is time / pace
    print('We\'re calculating distance')
    
    totalseconds = 0
    totalseconds += int(result['hours']) * 3600
    totalseconds += int(result['minutes']) * 60
    totalseconds += int(result['seconds'])

    pace = float(result['pace'])

    print('Time: {}\nPace: {}\n'.format(totalseconds, pace))
    print('Distance is {} miles'.format(totalseconds / pace))

def calculateTime(result):
    # time = distance * pace
    print('We\'re calculating time')

    distance = float(result['distance'])

    pace = float(result['pace'])

    print('Distance: {}\nPace: {}\n'.format(distance, pace))
    print('Time is {} seconds'.format(distance * pace))


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
            calculatePace(result)
        elif result['pace'] != '' and givenTime and result['distance'] == '':
            calculateDistance(result)
        elif result['distance'] != '' and result['pace'] != '' and not givenTime:
            calculateTime(result)
        else:
            # error and die
            # raise ValueError('2 Fields must be completed and 1 must be blank!')
            print('2 Fields must be completed and 1 must be blank!')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)