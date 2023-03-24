# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from ship_status.models import shipment as ship_obj

### This function is inserting the data into our table.
def ship_data_insert(fname, lname, email, mobile, address, product_id, quantity, payment_status, transaction_id, shipment_status):
	shipment_data = ship_obj(fname = fname,lname = lname, email = email, mobile = mobile, address = address, product_id = product_id, quantity = quantity,	payment_status = payment_status, transaction_id = transaction_id, shipment_status = shipment_status)
	shipment_data.save()
	return 1


### This function will get the data from front end.
@csrf_exempt
def shipment_reg_update(request):
	if request.method == 'POST':
		if 'application/json' in request.META['CONTENT_TYPE']:
			val1 = json.loads(request.body)
			### This is for reading the inputs from JSON.
			fname = val1.get("First Name")
			lname = val1.get("Last Name")
			email = val1.get("Email Id")
			mobile = val1.get("Mobile Number")
			address = val1.get("Address")
			product_id = val1.get("Product Id")
			quantity = val1.get("Quantity")
			payment_status = val1.get("Payment Status")
			transaction_id = val1.get("Transaction Id")
			shipment_status = "ready to dispatch"
	
			resp = {}
			### After all validation, it will call the data_insert function.
			respdata = ship_data_insert(fname, lname, email, mobile, address, product_id, quantity, payment_status, transaction_id, shipment_status)
			### If it returns value then will show success.
			if respdata:
				resp['status'] = 'Success'
				resp['status_code'] = '200'
				resp['message'] = 'Product is ready to dispatch.'
			### If it is not returning any value then will show failed.
			else:
				resp['status'] = 'Failed'
				resp['status_code'] = '400'
				resp['message'] = 'Failed to update shipment details.'

	return HttpResponse(json.dumps(resp), content_type = 'application/json')


### This function is used for finding the transaction.
def shipment_data(uname):
	data = ship_obj.objects.filter(email = uname)
	for val in data.values():
		return val

### This function is used for getting the shipment status
@csrf_exempt
def shipment_status(request):
	if request.method == 'POST':
		if 'application/json' in request.META['CONTENT_TYPE']:
			variable1 = json.loads(request.body)
			### This is for reading the inputs from JSON.
			uname = variable1.get("User Name")
			resp = {}
			### It will call the shipment_data function.
			respdata = shipment_data(uname)
			### If it returns value then will show success.
			if respdata:
				resp['status'] = 'Success'
				resp['status_code'] = '200'
				resp['message'] = respdata
			### If it is not returning any value then will show failed.
			else:
				resp['status'] = 'Failed'
				resp['status_code'] = '400'
				resp['message'] = 'User data is not available.'

	return HttpResponse(json.dumps(resp), content_type = 'application/json')