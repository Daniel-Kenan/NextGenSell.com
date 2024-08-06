from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json
import os
import datetime 
import time 
from django.shortcuts import render, redirect


# Path to the JSON file
DATA_FILE_PATH = 'office/data.json'

@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            data["last_updated"] = time.strftime("%D %H:%M")
            pretty_json = json.dumps(data, indent=4, sort_keys=True)
            # print(pretty_json)

            # Save data to JSON file
            with open(DATA_FILE_PATH, 'w') as file:
                file.write(pretty_json)

            return JsonResponse({'status': 'success'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    elif request.method == 'GET':
        try:
            if os.path.exists(DATA_FILE_PATH):
                with open(DATA_FILE_PATH, 'r') as file:
                    data = file.read()
                return JsonResponse({'status': 'success', 'data': json.loads(data)}, json_dumps_params={'indent': 4})
            else:
                return JsonResponse({'status': 'error', 'message': 'No data found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def office_dashboard(request):
    return render(request, 'officedashboard.html')


def chatbot(request):
    return render(request, 'plugins/chatbot.html')

def calculator(request):
    return render(request, 'plugins/calculator.html')


def advanced_reports(request):
    return render(request, 'advancedreports.html')


def retrieve_products(request):
    return render(request, 'tables.html')