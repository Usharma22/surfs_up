#part1
from flask import Flask
app = Flask(__name__)



#  part 2
@app.route('/')
def home():
    print("hey I'm in here")
    return"hey i'm in web page"
#
# 
# 
# hello_world():
#return 'Hello world'

#set 
#FLASK_APP = app.py
#flask run

# part 3

if __name__ == "__main__":
    app.run(debug=True)
