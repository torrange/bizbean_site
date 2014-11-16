from flask import Flask, render_template, request
from requests import get
from json import loads

app = Flask(__name__)


#get rid of this soon
@app.route('/')
def main_page():
    return render_template('search.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == "POST":
        industry = request.form["industry"]
        city = request.form["city"]
        r = get("http://api.bizbean.co.uk/%s/%s" % (city, industry))
        content = loads(r.content)
        result_length = len(content)
        return render_template('business-list.html', city=city, industry=industry, result_length=result_length, content=content )





# @app.route('/')
# def main_page():
#     r = get("http://api.bizbean.co.uk/London/Accountants")
#     query_response = loads(r.content)
#     lead = dict(query_response[3])

#     return render_template('search.html', 
#         business_name=lead["BusinessName"], 
#         addr1=lead["Addr1"], 
#         addr2=lead["Addr2"],  
#         phone_number=lead["Phone"],
#         post_code=lead["PostCode"],
#         city=lead["City"],

#          )      #  county=lead["County"],



# "LogoUrl": "None", 

# "Industry": "Coach-and-Bus-Hir", 
# "BusinessName": "2 Way Travel",  
# "LatLon": [5.0, 1.0]
# }

# if __name__ == "__main__":
#     app.run(debug=True)