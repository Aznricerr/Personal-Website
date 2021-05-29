from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    jobs = Job.objects
    #return render(request, 'jobs/detail.html',{'job':job_detail})
    if job_id == 1:
        return render(request, 'jobs/project1.html', {'job': job_detail})
    elif job_id == 2:
        return render(request, 'jobs/intel.html', {'job': job_detail})
    elif job_id == 3:
        return render(request, 'jobs/project2.html', {'job': job_detail})
    else:
        return render(request, 'jobs/home.html', {'jobs': jobs})


