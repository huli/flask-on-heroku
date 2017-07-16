import os
import json
import IP2Location


from werkzeug import *
from flask import *
from json import load
from urllib.request import urlopen


app = Flask(__name__)

@app.route('/')
@app.route('/<nameparameter>')
def sayHello(nameparameter=None):
    return render_template('index.html', name=nameparameter)

@app.route('/test')
def test_ip():
      provided_ips = request.headers.getlist("X-Forwarded-For")
      return Response(json.dumps(provided_ips), mimetype='application/json')

@app.route('/details')
def details():
    results = {}

    address = request.headers.getlist("X-Forwarded-For")[0]
    
    try:
        IP2LocObj = IP2Location.IP2Location()
        IP2LocObj.open("data/IP2LOCATION-LITE-DB1.BIN")
        address_details = IP2LocObj.get_all(address)
    except Exception as e:
        results['error'] = str(e)
        return Response(json.dumps(results), mimetype='application/json')

    results['ipAddress'] = address_details.ip
    results['countryCode'] = address_details.country_short.decode()
    results['countryName'] = address_details.country_long.decode()

    return Response(json.dumps(results), mimetype='application/json')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
