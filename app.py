from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
    <head>
        <title>Event Registration</title>
    </head>
    <body>
        <h1>Event Registration</h1>
        <form>
            <p><label>Name:</label><br><input type="text" required></p>
            <p><label>Email:</label><br><input type="email" required></p>
            <p><label>Department:</label><br><input type="text" required></p>
            <p><label>Father's Name:</label><br><input type="text" required></p>
            <p><label>Telephone:</label><br><input type="tel" required></p>
            <button type="submit">Register</button>
        </form>
    </body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

