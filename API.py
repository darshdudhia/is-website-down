from flask import *
import json
import requests

app = Flask(__name__)

def Site_Check(url):
    try:
        request_response = requests.get("http://" + url, timeout=5)
        status_code = request_response.status_code
        if status_code == 200:
            return "UP"
        if status_code == 404:
            return "PAGE NOT FOUND"

    except requests.RequestException:
        return "BAD URL"

    except requests.ConnectionError:
        return "CONNECTION ERROR"


    except requests.HTTPError:
       return "HTTP ERROR"


    except requests.URLRequired:
        return "INVALID URL"

    except requests.TooManyRedirects:
        return "TOO MANY REDIRECTS"


    except requests.ConnectTimeout:
        return """TIMED OUT WHILE
                TRYING TO CONNECT TO THE REMOTE SERVER."""


    except requests.ReadTimeout:
        return "THE SERVER DID NOT SEND ANY DATA IN THE ALLOTTED AMOUNT OF TIME."

    except requests.Timeout:
        return "THE REQUEST TIMED OUT."


@app.route('/request/', methods=['GET'])
def req():
    url = str(request.args.get('site_name'))
    # /request/?site_name=www.google.com
    Status = Site_Check(url)
    data_set = {'Url:': url, 'Status': Status}
    json_dump = json.dumps(data_set)
    return json_dump


app.run()
