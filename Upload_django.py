@csrf_exempt
def upload(request):
    file_path = "/opt/upload"
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    if request.method == 'POST':
        try:
            file_obj = request.FILES.get('file')
            file_name = os.path.join(file_path, file_obj.name)
            print(file_name)
            if os.path.exists(file_name):
                return HttpResponse('file already exist')
            else:
                file = open(file_name, 'wb')
                file.close()
            with open(file_name, 'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')
    else:
        try:
            file_lists = os.listdir(file_path)
            return HttpResponse(json.dumps(file_lists), content_type="application/json")
        except:
            return HttpResponse('404')

