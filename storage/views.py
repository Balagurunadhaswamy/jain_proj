from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import File
# Create your views here.
from accounts.models import NewUser

@api_view(['POST'])
def store_file(request):

    if request.user.is_authenticated == True:

        data = request.data
        sender = request.user
        reciever = NewUser.objects.get(id=data['reciever'])
        file = data['encrypted_file']
        try:
            File.objects.create(sent_by=sender, recieved_by=reciever, encrypted_file=file)
            return Response({"success":"Data stored successfully"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"failure": "Data storage failure"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"failure": "You are unauthorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED )
    
@api_view(['GET'])
def get_files(request):
    import pdb; pdb.set_trace()

    if request.user.is_authenticated == True:
        try:
            notified_res = list(File.objects.filter(recieved_by=request.user.id).exclude(notified=False).values())
            unnotified_res = list(File.objects.filter(recieved_by=request.user.id).exclude(notified=True).values())

            change_obj_status = File.objects.filter(recieved_by=request.user.id).exclude(notified=True).update(notified=True)

            response_obj = {'notified':notified_res, 'un_notified':unnotified_res}
            return Response(response_obj, status=status.HTTP_200_OK)
        except:
            return Response({"failure": "Data storage failure"}, status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response({"failure": "You are unauthorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED )