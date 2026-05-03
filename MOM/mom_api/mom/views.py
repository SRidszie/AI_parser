from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import *
from rest_framework import status
from django.http.response import JsonResponse






class gtts(APIView):
    # permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)

    def post(self, request):
        # if "file_content" and "file_extension" not in request.data:
        if "audio_path" not in request.data:
            response = JsonResponse(
                {
                    "status": "failure",
                    "status-code": status.HTTP_400_BAD_REQUEST,
                    "message": "Request to add required parameters",
                }
            )
            return response

        audio_path = request.data["audio_path"]
        # file_extension = request.POST.get("file_extension")
        # file_extension = request.POST["file_extension"]

        # file_extension = request.data["file_extension"]
        # print("Sandeep")
        # print(file_extension)
        # file_extension = request.POST.get("file_extension")

        # text = extract(file_content, file_extension)
        text = extract(audio_path)
        return Response(text)


def valid_audio_extensions_api(request):
    data = {
        "valid_extensions": ".mp3,.wav",
        "message": "Valid audio extensions are: .mp3,.wav",
    }
  
    return JsonResponse(data)



