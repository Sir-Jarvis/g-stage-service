from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.serializers import Serializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import json
import requests

# models classes
from gestion_stage.models import PostulatdeStage, EvaluationOrganisation_Dept, EvaluationOrganisation_par_Eleve, RapportdeStage, Evenement, ParticipantEvent, Reunion, ParticipantReunion

# Serializers classes
from gestion_stage.serializers import PostulatdeStageSerializer, EvaluationOrganisation_DeptSerializer, EvaluationOrganisation_par_EleveSerializer, RapportdeStageSerializer, EvenementSerializer, ParticipantEventSerializer, ReunionSerializer, ParticipantReunionSerializer

# Create your views here.


class PostulatAPIView(APIView):
    parser_classes = (MultiPartParser, )
    def post(self,request,*args, **kwargs):
        f_cv=request.FILES['cv']
        f_lm=request.FILES['lm']
        r_cv = requests.post('https://mon-api-docs.herokuapp.com/api/uploadfiles/', files={'file':f_cv})
        r_lm = requests.post('https://mon-api-docs.herokuapp.com/api/uploadfiles/', files={'file':f_lm})
        resp_cv = json.loads(r_cv.text)
        resp_lm = json.loads(r_lm.text)
        print(resp_cv)
        print(resp_lm)
        data = {
            'cv':resp_cv['url'],
            'lettre_motivation': resp_lm['url'],
            'type_stage': request.data['type_stage'],
            'duree_stage': request.data['duree_stage'],
            'eleve': request.data['eleve'],
            'organisation': request.data['organisation'],
        }

        serializer = PostulatdeStageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        urlsFile = serializer.save()
        return Response(PostulatdeStageSerializer(urlsFile).data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        posts = PostulatdeStage.objects.all()
        serializer = PostulatdeStageSerializer(posts,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RapportdeStageAPIView(APIView):
    parser_classes = (MultiPartParser, )
    def post(self,request,*args, **kwargs):
        f_rap_stage=request.FILES['file_rapport']
        r_rap_stage = requests.post('https://mon-api-docs.herokuapp.com/api/uploadfiles/', files={'file':f_rap_stage})
        resp_rap_stage = json.loads(r_rap_stage.text)
        print(resp_rap_stage)
        data = {
            'annee_scolaire': request.data['annee_scolaire'],
            'file_rapport':resp_rap_stage['url'],
            'nom_rapport': request.data['nom_rapport'],
            'maitre_stage': request.data['maitre_stage'],
            'organisation': request.data['organisation'],
            'eleve': request.data['eleve'],
        }

        serializer = RapportdeStageSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        urlsFile = serializer.save()
        return Response(RapportdeStageSerializer(urlsFile).data, status=status.HTTP_201_CREATED)


class RapportdeStageList(generics.ListCreateAPIView):
    queryset = RapportdeStage.objects.all()
    serializer_class = RapportdeStageSerializer
    name = 'rapports-stage-list'


class RapportdeStageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RapportdeStage.objects.all()
    serializer_class = RapportdeStageSerializer
    name = 'rapport-stage-detail'



class PostulatdeStageList(generics.ListCreateAPIView):
    queryset = PostulatdeStage.objects.all()
    serializer_class = PostulatdeStageSerializer
    name = 'postulats-stage-list'


class PostulatdeStageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostulatdeStage.objects.all()
    serializer_class = PostulatdeStageSerializer
    name = 'postulat-stage-detail'


class EvaluationOrganisation_DeptList(generics.ListCreateAPIView):
    queryset = EvaluationOrganisation_Dept.objects.all()
    serializer_class = EvaluationOrganisation_DeptSerializer
    name = 'evaluation-organisation-dept-list'


class EvaluationOrganisation_DeptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EvaluationOrganisation_Dept.objects.all()
    serializer_class = EvaluationOrganisation_DeptSerializer
    name = 'evaluation-organisation-dept-detail'


class EvaluationOrganisation_par_EleveList(generics.ListCreateAPIView):
    queryset = EvaluationOrganisation_par_Eleve.objects.all()
    serializer_class = EvaluationOrganisation_par_EleveSerializer
    name = 'evaluations-organisation-par-eleve-list'


class EvaluationOrganisation_par_EleveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EvaluationOrganisation_par_Eleve.objects.all()
    serializer_class = EvaluationOrganisation_par_EleveSerializer
    name = 'evaluation-organisation-par-eleve-detail'


class EvenementList(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    name = 'evenements-list'


class EvenementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    name = 'evenement-detail'


class ParticipantEventList(generics.ListCreateAPIView):
    queryset = ParticipantEvent.objects.all()
    serializer_class = ParticipantEventSerializer
    name = 'participants-event-list'


class ParticipantEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParticipantEvent.objects.all()
    serializer_class = ParticipantEventSerializer
    name = 'participant-event-detail'


class ReunionList(generics.ListCreateAPIView):
    queryset = Reunion.objects.all()
    serializer_class = ReunionSerializer
    name = 'reunion-list'


class ReunionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reunion.objects.all()
    serializer_class = ReunionSerializer
    name = 'reunion-detail'


class ParticipantReunionList(generics.ListCreateAPIView):
    queryset = ParticipantReunion.objects.all()
    serializer_class = ParticipantReunionSerializer
    name = 'reunions-list'


class ParticipantReunionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParticipantReunion.objects.all()
    serializer_class = ParticipantReunionSerializer
    name = 'reunion-detail'


class ApiRoot(generics.GenericAPIView):
    name='api-root'
    serializer_class  = ''
    def get(self, request, *args, **kwargs):
        return Response({
            'postulats-de-stage': reverse(PostulatdeStageList.name, request=request),
            'eval-organ-par-dept': reverse(EvaluationOrganisation_DeptList.name, request=request),
            'eval-organ-par-eleve': reverse(EvaluationOrganisation_par_EleveList.name, request=request),
            'rapports-de-stage': reverse(RapportdeStageList.name, request=request),
            'evenements': reverse(EvenementList.name, request=request),
            'participants-evenements': reverse(ParticipantEventList.name, request=request),
            'reunions': reverse(ReunionList.name, request=request),
            'participants-reunions': reverse(ParticipantReunionList.name, request=request)
        })

