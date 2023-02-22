import urllib.request, json

try:
    url = "https://failteireland.azure-api.net/opendata-api/v1/activities/csv"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
except Exception as e:
    print(e)