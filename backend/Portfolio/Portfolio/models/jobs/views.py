from rest_framework import generics
from .jobs import Job
from .serializers import JobSerializer # Assicurati che l'import sia corretto

#utilizzo di generics per la creazione delle api
class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer