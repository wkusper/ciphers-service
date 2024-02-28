from django.http import JsonResponse

# Create your views here.
def greetings(request):
    result ={"message" : "Welcome to the Ciphers API"}
    return JsonResponse(result)
