from flask import Flask

app = Flask(__name__) # equivalent to main

@app.route('/') # www.appsite.com/api/

def hello_method():
    return "Hello from Flask"

if __name__ == '__main__':
    app.run()



