from flask import Flask, render_template, request
from form import ComputeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

# Base url
@app.route('/', methods=['GET', 'POST'])
def index():
    # return render_template('index.html')
    form = ComputeForm()
    if form.is_submitted():
        result = request.form # import request


        # Check which one of the three boxes is blank.
        # Then error check to ensure other two boxes have values
        # if result['distance'] == '':
        #     print('We\'re calculating distance')
        #     if result['time'] != '' and result['pace'] != '':
        #         # then we're good so continue
        #         print('ready to compute')
        #     else:
        #         print('2 fields must be filled in!')


        # elif result['time'] == '':
        #     print('We\'re calculating time')
        #     if result['distance'] != '' and result['pace'] != '':
        #         # then we're good so continue
        #         print('ready to compute')
        #     else:
        #         print('2 fields must be filled in!')

        # elif result['pace'] == '':
        #     print('We\'re calculating pace')
        #     if result['distance'] != '' and result['time'] != '':
        #         # then we're good so continue
        #         print('ready to compute')
        #     else:
        #         print('2 fields must be filled in!')

        # else:
        #     print('One field must be left blank!')
        
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)