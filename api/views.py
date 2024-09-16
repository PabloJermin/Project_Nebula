from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudSerializers, DbSerializer
from .models import Students
from django.db import connections
from django.db.models import Q
from django.db.utils import OperationalError



# Getting all the students
@api_view(['GET'])
def all_students(request):
    users= Students.objects.all()
    serialize = StudSerializers(users, many=True)
    return Response(serialize.data)


# creating a user
@api_view(["POST"])
def create_student(request):
    searialize = StudSerializers(data=request.data)
    if searialize.is_valid():
        searialize.save()
        return Response(searialize.data, status=status.HTTP_201_CREATED)
    return Response(searialize.errors, status=status.HTTP_400_BAD_REQUEST)


# querry a student
@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, pk):
    
    # if student doesn't exist in DB
    try:
        user = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # getting an existing student
    if request.method == "GET":
        serialize = StudSerializers(user)
        return Response(serialize.data)
    
    # creating a new student in DB
    elif request.method == "PUT":
        serializer = StudSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # deleting a item in db
    elif request.method == "DELETE":
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    

# searching a particular student
@api_view(["GET"])
def search(request):
    s_query = request.GET.get('q', '').strip()
    c_query = request.GET.get('q', '').strip()
    all_query = Students.objects.all()
    
    
    try:
# querrying with both cohort and name
        # if s_query and c_query:
        #     stud_q = all_query.filter(Q(name__icontains=s_query) & Q(cohort__icontains=c_query))
        # elif s_query:
        #     stud_q = all_query.filter(Q(name__icontains=s_query))
        # elif c_query:
        #     stud_q = all_query.filter(Q(cohort__icontains=c_query))
        # stud = StudSerializers(stud_q, many=True).data
        # print(stud_q)
        
        
# query student details by name or cohort only
        if s_query:
            stud_query = all_query.filter(
                Q(name__icontains=s_query) |
                Q(email__icontains=s_query)
                )
        # elif c_query:
        #     cohort_query = Students.objects.filter(
        #                 Q(cohort__icontains=c_query)
        #                 )
            
        # selected_stud = stud_query
            # selected_cohort = cohort_query
            selected_stud = stud_query
            
        # serializing the selected student deatails
            serial_stud = StudSerializers(selected_stud, many=True).data
            # serial_coh = StudSerializers(selected_cohort, many=True).data

        # throw an error for empty query
            if len(serial_stud) == 0:
                return Response({"error": "No student found"}, status=status.HTTP_404_NOT_FOUND)
            
            else:
                ser_stud=(serial_stud[0])
                # ser_coh=(serial_coh[0])
                
                # print(ser_stud["email"])
                # print(ser_coh)
                print(ser_stud)
                    
        # returning details to api
                stud_detail = {
                            "details" : ser_stud,
                            # "cohort": stud_cohort
                        }
                return Response(stud_detail, status=status.HTTP_200_OK)
        
            
    except Students.DoesNotExist:
            error = {"error":"No student found" }
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        
    


# testing connection to db
@api_view(["GET"])
def health(request):
    db_connect = connections['default']
    try:
        # tries the connection
        db_connect.cursor()
        data =  {
            "message" : "Connection is successful"
        }
        return Response(data, status=status.HTTP_302_FOUND)
 
    except OperationalError:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    
# testing the health or connection of another database
# @api_view(["POST", "OPTIONS"])
# def db_connections(request):
#     if request.method == "OPTIONS":
#         return Response({"status":"Okay"}, status=status.HTTP_200_OK)
    
#     if request.method == "POST":
#         serializer = DbSerializer(data=request.data)
#         if serializer.is_valid():
#             engine = serializer.validated_data['engine']
#             name = serializer.validated_data['name']
#             user = serializer.validated_data['user']
#             password = serializer.validated_data['password']
#             host = serializer.validated_data['host']
#             port = serializer.validated_data['port']
            
#         # add temporary connection to django db
#             temp_db = {
#                 'ENGINE' : f'django.db.backends.{engine}', 
#                 'NAME' : name,
#                 'USER' : user,
#                 'PASSWORD' : password,
#                 'HOST' : host,
#                 'PORT' : port,
#                 'OPTIONS' : {
#                 }
#                 }
#             # if not settings.USE_TZ:
#             #     temp_db['TIME_ZONE'] = settings.TIME_ZONE
            
#             connections.databases['temp_db'] = temp_db
#         # trying the users database
#             try:
#                 db_connect = connections['temp_db']
#                 db_connect.cursor()
#                 return Response({"message": "connection was successfull"}, status=status.HTTP_200_OK)
#             except OperationalError as e:
#                 return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
#         # remove the user's database
#             finally:
#                 connections.databases.pop('temp_db', None)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
        
#Testing the health of a database dynamically inputed by a user 
@api_view(["POST"])
def db_connections(request, *args, **kwargs):
    serializer = DbSerializer(data=request.data)
    if serializer.is_valid():
        dbase = serializer.validated_data
        try:
            connection = connections['default']
            connection.settings_dict.update({
                'NAME': dbase['name'],
                'USER': dbase['user'],
                'PASSWORD': dbase['password'],
                'ENGINE': dbase['engine'],
                'HOST': dbase['host'],
            })
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1;')
            return Response({"status": "Success"}, status=status.HTTP_200_OK)
        except OperationalError:
            return Response({"status":"No connection"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)