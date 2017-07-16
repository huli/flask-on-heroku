import os
import json
import IP2Location

from flask import *
from json import load
from urllib.request import urlopen


app = Flask(__name__)

@app.route('/')
@app.route('/<nameparameter>')
def sayHello(nameparameter=None):
    return render_template('index.html', name=nameparameter)


@app.route('/details')
def details():
    results = {}

    address = load(urlopen('http://httpbin.org/ip'))['origin']
    
    try:
        address = IPAddress(address)
    except Exception as e:
        results['error'] = e.message
        return Response(json.dumps(results), mimetype='application/json')

    address_details = location.get_all(address)
    results['ipAddress'] = address
    results['countryCode'] = address_details.country_short
    results['countryName'] = address_details.country_long
    results['cityName'] = address_details.city
    results['regionName'] = address_details.region

    return Response(json.dumps(results), mimetype='application/json')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
