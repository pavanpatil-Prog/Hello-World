from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info('Status request successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info('Metrics request successfull')
    return response

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    Message= "New Beginings , What..!!! Why..? and How? <br> Hi All, <br> its my last working day here, \
    <br> So I would like to take this opportunity to back in time and recall my story\
    <br> <li> By the time I finished gratuation it was too late to decide WHAT..? Next  \
    <br> <li>Just when I get answer of that, HR asked another Question  WHY..? this\
    <br> It took me 5 years to find the answer of that question\
    <br> <br>So I would like to thank The leader who introduced me in ZF to another the leader \
    <br> who gave me opportunity in ZF ITC to explore new world\
    <br>Most important learning in ZF for me is that I learned Not only to have an Opinion, but to belive it and wear it with confidance\
    <br> <li>Rest became easy beacuse all of you guys who helped me in my daily work when I was finding answers to different WHY..?\
    <br> <li>Thank you very much to all and All the very best for future\
    <br><br><br> <li>This exit is however special as my 8 years streak in Hyderabad is ending\
    <br> Gonna Miss Biryani and Trivikrams One liners a lot\
    <br> <br><br><br>Best Regards, <br>Pavan Patil"
    return Message

if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    
    app.run(host='0.0.0.0')
