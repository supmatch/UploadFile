import requests

def upload_file(file_name):
    url = upload_url
    files = {'file':open(file_name, 'rb')}
    req = requests.post(url,files=files)
    result = req.text
    return result
