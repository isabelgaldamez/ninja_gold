from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret key'
@app.route('/')
def home():
    # check if the key exists in session dictionary 
    # if the key does not exists, then initialize to 0
    # information does not get carried into a GET request
    # therefore we use the session to see what values the client has
    if not 'points' in session:
        session['points'] = 0
        session['activity'] = ''
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
    
    if 'farm_opt' in request.form:
        rand_points = random.randint(10, 20)
        session['points'] = session['points'] +  rand_points
        session['activity'] += f'<p>Earned {rand_points} golds from the farm!</p>'
    elif 'cave_opt' in request.form:
        rand_points = random.randint(5, 10)
        session['points'] = session['points'] + rand_points
        session['activity'] += f'<p>Earned {rand_points} golds from the cave!</p>'
    elif 'house_opt' in request.form:
        rand_points = random.randint(2, 5)
        session['points'] = session['points']+rand_points
        session['activity'] += f'<p>Earned {rand_points} golds from the house!</p>'
    else:
        rand_points = random.randint(0, 50)
        earn_money = bool(random.getrandbits(1)) #creates randomly a True or False value
        if earn_money:
            session['points'] += rand_points 
            session['activity'] += f'<p>Earned {rand_points} golds from the casino!</p>'
        else:
            session['points'] -= rand_points
            session['activity'] += f'<p>Entered a casino and lost {rand_points} golds!!!!</p>'

    # information stored in the request form cannot be carried into the ('/') when redirect
    # root is GET not 
    return redirect('/')
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug = True)