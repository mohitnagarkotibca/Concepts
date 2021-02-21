from flask import render_template,Flask
app= Flask(__name__)
something= ['alpha','bravo','charlie','delta']
@app.route('/')
def Home():
    return render_template('home.html',posts=something)
app.run()