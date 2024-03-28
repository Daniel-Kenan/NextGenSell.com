from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views import View

def home(request):
    return render(request,'home.html')

import qrcode
import os
def clientsignin(request):
    # Path to the existing QR code image
    existing_qr_path = "public/images/qrcode"
    
    # Check if the QR code image exists
    if os.path.exists(existing_qr_path):
        # If it exists, render the template with the existing QR code image path
        return render(request, 'sign-in/sign-in.html', {'qr_code_path': existing_qr_path})
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

        # Render the template with the QR code image path
        return render(request, 'sign-in/sign-in.html', {'qr_code_path': img_path})

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
