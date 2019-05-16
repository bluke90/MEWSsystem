from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/record", methods=['GET', 'POST'])
def record():
    # Start our TwiML response
    response = VoiceResponse()
    # Use <Say> to give the caller some instructions
    response.say('Thanks you for calling the Mississippi Early Warning Sytem. Thank you for any intel provided.')
    # Use <Record> to record the caller's message
    response.record()
    # End the call with <Hangup>
    response.hangup()
    return str(response)

if __name__ == "__main__":
    app.run()