
from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    string_to_cut = request.json['string_to_cut']
    returned_string = string_conversion(string_to_cut)
    returned_json = {"return_string": returned_string}
    return json.dumps(returned_json)

def string_conversion(string_to_cut):
    new_string = ""
    counter = 0
    for char in string_to_cut:
        counter += 1
        if counter % 3 == 0:
            new_string += char
        else:
            pass
    return new_string


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
