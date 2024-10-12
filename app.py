from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty list to store notes
notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('note')
        if title and content:
            # Append the new note as a dictionary to the notes list
            notes.append({'title': title, 'content': content})
            return redirect(url_for('home'))  # Redirect to the home route
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
