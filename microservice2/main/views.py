from django.http import HttpResponse


def get_message(request):
    if request.method == 'GET':
        return HttpResponse('Привет! Это ВТОРОЙ микросервис!')
