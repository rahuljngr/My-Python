from flask import Flask, render_template

app = Flask(__name__, template_folder={/home/rahul/python3/home.html})

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def page():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug = True)

#go to browser and open 'localhost:5000'

