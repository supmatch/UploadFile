import requests

def upload_file(file_name):
    url = upload_url
    files = {'file':open(file_name, 'rb')}
    req = requests.post(url,files=files)
    data = req.text
    return data

if __name__ == '__main__':
    filename = filename
    data = upload_file(filename)
    print(data)
