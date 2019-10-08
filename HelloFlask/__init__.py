
from flask import Flask, render_template, request, redirect, escape, session, copy_current_request_context
from .perform_bot import take_care_about_call


app = Flask(__name__, template_folder='templates')
app.secret_key = 'thisismysupperkey'

@app.route('/vk_bot', methods = ['POST'])
def perform():

    return take_care_about_call(request)
    # return 'bea2f6e3'

@app.route('/retro')
def retro():
    
    return render_template('retro.html')
    
@app.route('/send_schedule')
def send_schedule():
    
    


if __name__ == "__main__":

    app.run(debug = 1)