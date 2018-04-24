from flask import Flask, render_template
app = Flask(__name__)

@app.route('/users/')
def users():
    names = ['ingyin','thant','gyingyinn','enu','batch1']
    return render_template('list.html', names=names)

if __name__ == "__main__" :
    app.run(host='0.0.0.0', debug=True)
