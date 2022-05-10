from flask import Flask
from random import randint
app = Flask(__name__)

LOW_IMG = 'https://media.giphy.com/media/pNCpaSVwEAQMpkoR1f/giphy.gif'
HIGH_IMG = 'https://media.giphy.com/media/zwhSO2AFG1yI5DSmSu/giphy.gif'
CORRECT_IMG = 'https://media.giphy.com/media/hTOQHQ9lim011gF80j/giphy.gif'
START_IMG = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'

def style_decorator(function):
    def wrapper(**kwargs):
        text = function(**kwargs)       
        if function.__name__ == 'guess_number':      
            if 'low' in text:
                text_color = 'red'
                gif_link = LOW_IMG 
            elif 'high' in text:
                text_color = 'purple'
                gif_link = HIGH_IMG
            else:
                text_color = 'green'
                gif_link = CORRECT_IMG              
        else:
            text_color = 'black'
            gif_link = START_IMG
                           
        return f'<h1 style="color:{text_color}">{text}</h1><br><br><img src="{gif_link}">'         
    return wrapper
 
@app.route('/', endpoint='start_game')
@style_decorator
def start_game():
    return 'Guess a number between 0 and 9'
 
@app.route('/<int:n>', endpoint='guess_number')
@style_decorator
def guess_number(n): 
    if n < number:
        text = 'Too low, try again!'      
    elif n > number:
        text = 'Too high, try again!'
    else:
        text = 'You found me!'           
    return text       
  
number = randint(1,9)
print(number)
if __name__ == '__main__':
    app.run(debug=True) 