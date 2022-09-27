from django.shortcuts import render
from introduce.models import AccessLog
# Create your views here.
def index(request):
    # case 1
    '''
    # access_log = AccessLog()
    # access_log.location = "introduce"
    # access_log.save()
    '''
    AccessLog.objects.create(location='introduce')
    return render(request, 'index.html')