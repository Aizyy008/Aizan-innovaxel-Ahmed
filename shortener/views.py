# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import URL
# from django.shortcuts import redirect, render
# from .serializers import URLSerializer, URLStatsSerializer



# def home(request):
#     return render(request, 'index.html')


# @api_view(['POST'])
# def create_short_url(request):
#     serializer = URLSerializer(data=request.data)
    
#     if serializer.is_valid():
#         short_code = URL.generate_short_code()
        
#         url_obj = URL.objects.create(
#             url=serializer.validated_data['url'],
#             short_code=short_code
#         )
        
#         response_serializer = URLSerializer(url_obj)
#         return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_original_url(request, short_code):
#     try:
#         url_obj = URL.objects.get(short_code=short_code)
#         url_obj.access_count += 1
#         url_obj.save(update_fields=['access_count'])
        
#         serializer = URLSerializer(url_obj)
#         return Response(serializer.data)
#     except URL.DoesNotExist:
#         return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['PUT'])
# def update_url(request, short_code):
#     try:
#         url_obj = URL.objects.get(short_code=short_code)
#     except URL.DoesNotExist:
#         return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer = URLSerializer(url_obj, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_url(request, short_code):
#     try:
#         url_obj = URL.objects.get(short_code=short_code)
#         url_obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except URL.DoesNotExist:
#         return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def get_url_stats(request, short_code):
#     try:
#         url_obj = URL.objects.get(short_code=short_code)
#         serializer = URLStatsSerializer(url_obj)
#         return Response(serializer.data)
#     except URL.DoesNotExist:
#         return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def redirect_to_original(request, short_code):
#     try:
#         url_obj = URL.objects.get(short_code=short_code)
#         url_obj.access_count += 1
#         url_obj.save(update_fields=['access_count'])
#         return redirect(url_obj.url)
#     except URL.DoesNotExist:
#         return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)