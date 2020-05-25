from flask import Flask

app = Flask(__name__) # equivalent to main

@app.route('/') # www.appsite.com/api/

def message_method():
    message = "Let's get Flask working"
    return message

if __name__ == '__main__':
    app.run()



