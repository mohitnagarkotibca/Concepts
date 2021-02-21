from flask import Flask,render_template

app= Flask(__name__)
post1=[
    {1'name':'Mohit',
     'roll_number':'18mca8012'
    }
]
@app.route('/')
def home():
    return render_template('home.html',posts=post1)
app.run()
