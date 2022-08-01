from json import loads
from pytest import mark
from requests import request

headers = "code, expected_branch"

data = [("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
    ("SBIN0040014", "BASAVANAGUDI"),
    ("ICIC0000002", "BANGALORE - M G ROAD")]

@mark.parametrize(headers, data)
def test_bank(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    print(url)

    response = request("GET", url)
    reponse_test = response.text
    print(reponse_test)

    d = loads(reponse_test)
    actual_branch = d["BRANCH"]
    assert actual_branch == expected_branch