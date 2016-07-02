from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/var/www/cgi-bin/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
