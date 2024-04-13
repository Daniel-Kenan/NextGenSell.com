from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate, login, get_user_model
import qrcode
import os
from django.contrib import messages
from django.urls import reverse
import json
from django.contrib.auth.models import User
from .payfast import PayfastPayment
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import smtplib
import ssl
from email.message import EmailMessage
import re

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        valid_email = re.match(email_pattern, email)
        user = None
        if valid_email and password:
            user = authenticate(request, username=email, password=password)  
        if user:
            login(request, user)
            return redirect(reverse('consultancy:cs_potential_clients'))
        else:
            try:
                # Attempt to get the user by email
                user = User.objects.get(email=email)
                messages.error(request, 'Incorrect password.')  # Add error message
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')  # Add error message
            
            return redirect('clientsignin')  
    return render(request,redirect(reverse('consultancy:cs_potential_clients')))

def home(request):
    return render(request,'home.html')

def clientsignin(request):
    error_message = None
    if 'error_message' in request.session:
        error_message = request.session.pop('error_message')  # Retrieve and remove error message from session
    
    # Retrieve error messages from the messages framework
    messages_data = messages.get_messages(request)
    error_messages = [message for message in messages_data if message.level == messages.ERROR]

    # Path to the existing QR code image
    existing_qr_path = "public/images/qrcode"
    
    # Check if the QR code image exists
    if os.path.exists(existing_qr_path):
        # If it exists, render the template with the existing QR code image path and error messages
        return render(request, 'sign-in/sign-in.html', {'qr_code_path': existing_qr_path, 'error_message': error_message, 'error_messages': error_messages})
    else:
        # If it doesn't exist, generate a new QR code (similar to previous example)
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # You can customize the data in the QR code as needed
        qr.add_data("Some data here")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image or convert it to bytes
        # In this example, I'm saving it temporarily
        img_path = "path_to_save_qr_code.png"
        img.save(img_path)

        # Render the template with the QR code image path and error messages
        return render(request, 'sign-in/sign-in.html', {'qr_code_path': img_path, 'error_message': error_message, 'error_messages': error_messages})

# @method_decorator(csrf_exempt, name='dispatch')
# class ValidateProductKeyView(View):
#     def post(self, request, key, device):
#         if key and device:
#             product_key = get_object_or_404(ProductKey, key=key, is_used=False)
#             product_key.is_used = True
#             product_key.device = device
#             product_key.date_used = datetime.now().date()
#             product_key.time_used = datetime.now().time()
#             product_key.save()

#             return JsonResponse({'status': 'success', 'message': 'Product key is valid.'})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Invalid request parameters.'})

# validate_product_key_view = api_view(['POST'])(permission_classes([AllowAny])(ValidateProductKeyView.as_view()))


data = {
    # Merchant details
    'merchant_id': settings.GATEWAY_CONFIG['merchant_id'],
    'merchant_key':settings.GATEWAY_CONFIG['merchant_key'],
    'return_url': settings.SITE+"payment-successful/",
    'cancel_url': settings.SITE+"payment-failed/",
    'notify_url': 'https://www.nextgensell.com/err',
    # Buyer details
    'name_first': 'First Name',
    'name_last': 'Last Name',
    'email_address': 'test@test.com',
    # Transaction details
    'm_payment_id': '1234', #Unique payment ID to pass through to notify_url
    'amount': "200",
    'item_name': 'Order#123'
}

payfast_payment = PayfastPayment(data,settings.GATEWAY_CONFIG['passphrase'],sandbox_mode=settings.GATEWAY_CONFIG['mode'])
html_form = payfast_payment.generate_html_form()
# print(html_form)

def testpage(request):
    return render(request, 'testpage.html',{'form':html_form})


def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_failure(request):
    return render(request, 'payments/payment_failure.html')


def payment_cancelled(request):
    return render(request, 'payments/payment_failure.html')



class ContactUsHandling(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact/contact.html')
    
    def post(self,request, *args, **kwargs):
       try: 
        tmp = request.POST
        print(tmp)
        # 'name': ['Daniel Kenan Slinda'], 'email': ['sdanielkenan@gmail.com'], 'subject': ['software'], 'message': ['GGG']
        msg = EmailMessage()
        msg['Subject'] = tmp['subject']
        msg['From'] = os.environ.get('BOT_EMAIL')
        msg['To'] = os.environ.get("BOT_MAILTO")
        msg.set_content("Email From: " + tmp["email"] + "\n\nMessage:\n" + tmp["message"])
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(msg['From'],os.environ.get('BOT_PASSWD'))
            smtp.sendmail(msg["From"],msg["To"],msg.as_string())
        return HttpResponse("The message has been dispatched. You can expect a response within the next one to two business days.")
       except Exception as e: 
           return HttpResponse(str(e.message))