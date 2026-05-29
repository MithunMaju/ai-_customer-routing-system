from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomerRequest
from .serializers import CustomerRequestSerializer
from classification.tasks import classify_request

class CustomerRequestListCreateView(generics.ListCreateAPIView):
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        request = serializer.save()
        classify_request.delay(request.id)

class CustomerRequestDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializer
    permission_classes = [IsAuthenticated]
