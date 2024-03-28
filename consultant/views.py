from django.shortcuts import render

def dashboard(req):
    return render(req, 'Dashboard.html', {'active_view': 'dashboard'})

def potential_clients(req):
    return render(req, 'PotentialClients.html', {'active_view': 'potential-clients'})

def existing_clients(req):
    return render(req, 'ExistingClients.html', {'active_view': 'existing-clients'})

def productkeys(req):
    return render(req, 'ProductKeys.html', {'active_view': 'product-keys'})

def notifications(req):
    return render(req, 'Notifications.html', {'active_view': 'notifications'})

def profile(req):
    return render(req, 'Profile.html', {'active_view': 'profile'})

def bussiness_form(req):
    return render(req, 'BussinessForm/BussinessForm.html')