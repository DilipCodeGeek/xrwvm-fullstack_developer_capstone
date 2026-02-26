import requests

# =========================================================
# ✅ HARD CODED SERVICE URLS
# =========================================================

# Node backend (3030)
backend_url = "https://dilipnair85-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"

# Sentiment analyzer
sentiment_analyzer_url = "https://sentianalyzer.26u9rqmouxqe.us-south.codeengine.appdomain.cloud/"

# ---------------------------------------------------------
# GET REQUEST FUNCTION
# ---------------------------------------------------------

def get_request(endpoint, **kwargs):
    params = ""

    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + str(value) + "&"

    request_url = backend_url + endpoint

    if params:
        request_url += "?" + params

    print("GET from {}".format(request_url))

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("GET Network exception occurred:", e)
        return {}


# ---------------------------------------------------------
# SENTIMENT ANALYZER FUNCTION
# ---------------------------------------------------------

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text

    print("SENTIMENT from {}".format(request_url))

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Sentiment network exception:", e)
        return {"sentiment": "neutral"}


# ---------------------------------------------------------
# POST REVIEW FUNCTION (FIXED ENDPOINT)
# ---------------------------------------------------------

def post_review(data_dict):
    # ✅ Correct endpoint for IBM backend
    request_url = backend_url + "/insert_review"

    print("POST to {}".format(request_url))

    try:
        response = requests.post(request_url, json=data_dict)

        print("Backend status code:", response.status_code)
        print("Backend response text:", response.text)

        # Backend does not return JSON, so treat 200 as success
        if response.status_code == 200:
            return {"status": 200}

        return {"status": 500}

    except Exception as e:
        print("POST Network exception occurred:", e)
        return {"status": 500}