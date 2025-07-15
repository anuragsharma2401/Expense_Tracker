from tracker.models import RequestLogs

class RequestLogging():
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_info = request
        RequestLogs.objects.create(
            request_info = vars(request_info),
            request_path = request_info.path,
            request_method = request_info.method,
        )
        return self.get_response(request)    