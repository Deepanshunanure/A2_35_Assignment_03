from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        if not name or not age:
            error = "Both name and age are required."
            return render_template('form.html', error=error)

        try:
            age = int(age)
        except ValueError:
            return render_template('form.html', error="Age must be a number.")

        return f"<h2>Hello, {name}! You are {age} years old.</h2><a href='/greet'>Back</a>"

    return render_template('form.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
