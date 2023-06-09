from flask import Flask, render_template, request, redirect, session # added request and redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return render_template("index.html")

@app.route('/add_two')
def addTwo():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return redirect('/')

@app.route('/random_number', methods=['post'])
def random_number():
    session['counter'] += int(request.form['counter']) - 1
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()		# clears all key
    return redirect('/')	 

if __name__ == "__main__":
    app.run(debug=True)


# Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly