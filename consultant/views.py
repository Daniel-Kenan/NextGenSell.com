from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from website.models import BusinessInfo
from django.http import JsonResponse
import json

# BusinessInfo  it is more of a lead and we register this lead

@login_required
@staff_member_required
def dashboard(req):
    return redirect(reverse("consultancy:cs_potential_clients"))
    return render(req, 'Dashboard.html', {'active_view': 'dashboard'})

@login_required
@staff_member_required
def potential_clients(req):
    clients = BusinessInfo.objects.all()
    return render(req, 'PotentialClients.html', {'active_view': 'potential-clients', 'clients': clients})

@login_required
@staff_member_required
def existing_clients(req):
    return render(req, 'ExistingClients.html', {'active_view': 'existing-clients'})

@login_required
@staff_member_required
def productkeys(req):
    return render(req, 'ProductKeys.html', {'active_view': 'product-keys'})

@login_required
@staff_member_required
def notifications(req):
    return render(req, 'Notifications.html', {'active_view': 'notifications'})

@login_required
@staff_member_required
def profile(req):
    return render(req, 'Profile.html', {'active_view': 'profile'})

@login_required
@staff_member_required
def bussiness_form(req):
    return render(req, 'BussinessForm/BussinessForm.html')

@login_required
@staff_member_required
def add_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Assuming 'data' contains the necessary form fields
        # Create a new Client object and save it to the database
        new_client = BusinessInfo.objects.create(
            name=data['enterprise'],
            contact_name=data['contactPerson'],
            position=data['position'],
            phone=data['phone'],
            email=data['email'],
            website=data['website']
            # Add other fields as needed
        )
        print(data)
        return JsonResponse({'success': True})  # Send a JSON response indicating success
    else:
        return JsonResponse({'success': False}) 