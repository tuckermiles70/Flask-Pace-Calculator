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

    return render_template('index.html', pace='100')

# https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
# using this instead of the jinja forms stuff
@app.route('/handle_data', methods=['POST'])
def handle_data():
    # print("here")
    result = request.form

    if result['hours'] == '' and result['minutes'] == '' and result['seconds'] == '':
        # error
        pass
    
    if result['distance'] == '':
        # error
        pass

    totalseconds = 0
    
    if result['hours'] != '':
        totalseconds += int(result['hours']) * 3600
    if result['minutes'] != '':
        totalseconds += int(result['minutes']) * 60
    if result['seconds'] != '':
        totalseconds += int(result['seconds'])

    distance = float(result['distance'])

    print('Distance: {}\nTime: {}\n'.format(distance, totalseconds))
    print('Pace is {} seconds per mile'.format(totalseconds / distance))

    pace_in_seconds = totalseconds / distance

    pace_in_minutes = pace_in_seconds / 60

    return render_template('index.html', pace = pace_in_minutes)

# Base url
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)