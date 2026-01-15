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


"""
sudo apt update
sudo apt install docker-compose
sudo systemctl start docker
docker-compose up -d --build
docker ps
curl http://localhost:5007
docker-compose logs -f
docker exec -it flask-app bash
ls , pip list , exit
"""


