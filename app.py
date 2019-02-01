from flask import Flask,render_template,request

app = Flask(__name__)

########## view funtion() ############

# This's sign_up page
@app.route('/')
def index():
    return render_template('sign_up.html')

# This page after form
@app.route('/report')
def report():
    lower_letter= False
    upper_letter= False
    num_end= False

    username= request.args.get('username')

    lower_letter= any(c.islower() for c in username)
    upper_letter= any(c.isupper() for c in username)
    num_end= username[-1].isdigit()

    report= lower_letter and upper_letter and num_end

    return render_template('report.html', report= report, lower_letter= lower_letter, upper_letter= upper_letter, num_end= num_end)
if __name__ == '__main__':
    app.run(debug=True)



