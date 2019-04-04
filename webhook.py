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
    context_name= address_context[0].get("name")
    print("context_name", context_name)

    parameters = address_context[0].get("parameters")
    print("parameters", parameters)
    last_name = parameters.get("last-name")
    print("last_name", last_name)
    last_name = parameters.get("last-name")
    print("last_name", last_name)
    given_name = parameters.get("given-name")
    print("given_name", given_name)
    email = parameters.get("email")
    print("last_name", email)

    return {
        "fulfillmentText": "As per our records "+given_name+", your order is left at the front desk "
                                                            "signed by Daniel at 7:40 pm",
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        "As per our records "+given_name+", your order is left at the front desk "
                                                            "signed by Daniel at 7:40 pm"
                    ]
                }
            }
        ],
        "outputContexts": [
            {
                "name": context_name,
                "lifespanCount": 0,
                "parameters": {
                    "given_name": given_name
                }
            }
        ]
    }


   #  pizza_base = parameters.get("pizza_base")
   #  print("pizza_base", pizza_base)
   #
   #  pizza_toppings = parameters.get("pizza_toppings")
   #  print("pizza_toppings", pizza_toppings)
   #
   #  pizza_size = parameters.get("pizza_size")
   #  print("pizza_size", pizza_size)
   #
   #  address_line2 = parameters.get("address_line2.original")
   #  print("address_line2", address_line2)
   #
   #  drink = parameters.get("drink")
   #  print("drink", drink)
   #
   #  if drink is None and drink.len>0:
   #      drink=drink
   #  else:
   #      drink= "no drink"
   #
   #
   #
   #  location_line1 = parameters.get("location_line1")
   #  print("location_line1", location_line1)
   #  street_address = location_line1.get("street-address")
   #  print("street_address", street_address)
   # # postal_code = parameters.get("'postal_code'")
   #
   #  if pizza_toppings is None and pizza_toppings.len>0:
   #      pizza_toppings=pizza_toppings
   #  else:
   #      pizza_toppings= "no"





    # return {
    # "fulfillmentText": "Great Your order of a "+ pizza_size +" size pizza with "+pizza_base+ " base "  + " and " + pizza_toppings +" toppings"+
    #                     " with an order of "+drink+
    #                    "will be delivered to" +street_address + "in 40 minutes",
    #     "fulfillmentMessages": [
    #         {
    #             "text": {
    #                 "text": [
    #                     "Great Your order of a "+ pizza_size +" size pizza with "+pizza_base+ " base "  + " and " + pizza_toppings +" toppings"+
    #                     " with an order of "+drink+
    #                    "will be delivered to" +street_address + "in 40 minutes"
    #                 ]
    #             }
    #         }
    #     ]
    # }


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

















