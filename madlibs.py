from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game', methods=["POST"])
def show_game_form():
    decision = request.form.get("play")

    if decision == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")



@app.route('/madlib')
def show_mad_lib():
    chosen_person = request.args.get('person')
    chosen_color = request.args.get('color')
    chosen_noun = request.args.get('noun')
    chosen_adjective = request.args.get('adjective')
    chosen_verbs = request.args.getlist('verbs')
    story_list = ["madlib.html", "madlib1.html", "madlib2.html"]
    
    story_choice = choice(story_list)
    verb1_choice = choice(chosen_verbs)
    verb2_choice = choice(chosen_verbs)

    return render_template(story_choice, verb1=verb1_choice, verb2=verb2_choice, person=chosen_person, color=chosen_color, noun=chosen_noun, adjective=chosen_adjective)

    # story_choice = request.args.get("story")

    # if story_choice == "happy":
    #     return render_template('madlibhappy.html', person=chosen_person, color=chosen_color, noun=chosen_noun, adjective=chosen_adjective)
    #     # return render_template('madlib.html', person=chosen_person, color=chosen_color, noun=chosen_noun, adjective=chosen_adjective)
    # else:
    #     return render_template('madlibsad.html', person=chosen_person, color=chosen_color, noun=chosen_noun, adjective=chosen_adjective)     


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
