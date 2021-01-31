from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def release_me(request):
    # return response with template and context 
    import subprocess
    if request.POST:
        subprocess.run(['/home/kirrton/keepit/release_me.sh'])
    return render(request, "release_me.html") 
    