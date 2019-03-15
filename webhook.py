import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("request",req)
    print(json.dumps(req, indent=4))
    
    res = processrequest(req)
    
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processrequest(req):
    result = req.get("queryResult")
    print("result", result)
    address_context = result.get("outputContexts")
    print("address_context",address_context)
    parameters = address_context.get("parameters")
    print("parameters", parameters)
    location_original = parameters.get("location.original")
    print("location_original", location_original)
    address_line2_original = parameters.get("address_line2.original")
    print("address_line2_original", address_line2_original)
   # postal_code = parameters.get("'postal_code'")




    return {
    "fulfillmentText": "Great Your special will be delivered to" +location_original + address_line2_original + "in 40 minutes",
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        "Great Your special will be delivered to" +location_original + address_line2_original + "in 40 minutes"
                    ]
                }
            }
        ]
    }


    # result = req.get("queryResult")
    # print("result",result)
    # parameters = result.get("parameters")
    # city = parameters.get("geo-city")
    # date = parameters.get("date")
    # if city is None:
    #     return None
    # r=requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=06f070197b1f60e55231f8c46658d077')
    # json_object = r.json()
    # weather=json_object['list']
    # for i in range(0,30):
    #     if date in weather[i]['dt_txt']:
    #         condition= weather[i]['weather'][0]['description']
    #         break
    # speech = "The forecast for"+city+ "for "+date+" is "+"cloudy skies"
    # return {
    # "fulfillmentText": speech,
    #     "fulfillmentMessages": [
    #         {
    #             "text": {
    #                 "text": [
    #                     speech
    #                 ]
    #             }
    #         }
    #     ]
    # }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')

















