from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from medicines.models import Medicine, Category
from medicineapi.serializers import MedicineSerializer
from django.contrib.auth.models import User


# Create your views here.

def getSuccessResponse(data, code, message):
    context = {
        'message': message,
        'status_code': code,
        'data': data,
        'error': [],
        'pagination': [],
        'files': []
    }
    return context


def getErrorResponse(data, code, message):
    context = {
        'message': message,
        'status_code': code,
        'data': data,
        'error': [],
        'pagination': [],
        'files': []
    }
    return context


class MedicineApiView(APIView):
    def get(self, request):
        data_list = Medicine.objects.all()
        serializer = MedicineSerializer(data_list, many=True)
        message = 'Medicine List'
        if not data_list:
            message = 'Not Found'
            data = {
                'message': 'No data Found'
            }
            return Response(getErrorResponse(message, 404, message), status=status.HTTP_NOT_FOUND)
        return Response(getSuccessResponse(serializer.data, 200, message), status=status.HTTP_200_OK)

    def post(self, request):
        user = User.objects.get(username='a')
        category = Category.objects.get(id=request.POST.get('category'))
        req_data = {
            "name": request.POST.get('name'),
            "description": request.POST.get('description'),
            "expiry_date": request.POST.get('expiry_date'),
            "mg": request.POST.get('mg'),
            "price": request.POST.get('price'),
            "quantity": request.POST.get('quantity'),
            "category": 1,
            "user": user,
        }
        serializer = MedicineSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            message = 'Added Successfully'
            return Response(getSuccessResponse(serializer.data, 201, message), status=status.HTTP_CREATED_201)
        else:
            message = 'something went wrong'
            return Response(getErrorResponse(serializer.data, 200, message), status=status.HTTP_200_OK)


class MedicineApiIdView(APIView):
    def get_medicine_object(self, id):
        try:
            data = Medicine.objects.get(id=id)
            return data
        except Medicine.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_medicine_object(id)

        if not instance:
            message = 'Not Found'
            return Response(getErrorResponse(message, 404, message), status=status.HTTP_404_NOT_FOUND)

        serializer = MedicineSerializer(instance)
        message = 'Medicine Detail'
        return Response(getErrorResponse(serializer.data, 200, message), status=status.HTTP_200_OK)

    def delete(self, request, id):
        instance = self.get_medicine_object(id)

        if not instance:
            message = 'Not Found'
            return Response(getErrorResponse(message, 404, message), status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        message = 'Medicine Deleted'
        return Response(getSuccessResponse(message, 200, message), status=status.HTTP_200_OK)
