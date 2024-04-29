from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_request.html', {'form': form})

def track_requests(request):
    requests = ServiceRequest.objects.all().order_by('-request_date') #Order requests by date 
    return render(request, 'customer/track_requests.html', {'requests': requests})

return render(request, 'customer/submit_request.html') #returning request
