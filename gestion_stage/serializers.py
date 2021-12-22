from django.db.models import fields
from rest_framework import serializers
from gestion_stage.models import PostulatdeStage, EvaluationOrganisation_Dept, EvaluationOrganisation_par_Eleve, RapportdeStage, Evenement, ParticipantEvent, Reunion, ParticipantReunion
import requests


class PostulatdeStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostulatdeStage
        fields = '__all__'


class EvaluationOrganisation_DeptSerializer(serializers.HyperlinkedModelSerializer):
    avis_eleves = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avis-eleves-detail')
    class Meta:
        model = EvaluationOrganisation_Dept
        fields = (
            'pk',
            'url',
            'contenu_evaluation',
            'note',
            'organisation',
            'membre_dept',
            'date_creation',
            'avis_eleves',
        )


class EvaluationOrganisation_par_EleveSerializer(serializers.HyperlinkedModelSerializer):
    related_dept_evaluation = serializers.SlugRelatedField(queryset=EvaluationOrganisation_Dept.objects.all(), slug_field='name')
    class Meta:
        model = EvaluationOrganisation_par_Eleve
        fields = (
            'pk',
            'url',
            'avis',
            'eleve',
            'organisation',
            'related_dept_evaluation',
            'date_creation',
        )


class RapportdeStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapportdeStage
        fields = '__all__'


class EvenementSerializer(serializers.HyperlinkedModelSerializer):
    guests = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='guests-detail')
    class Meta:
        model = Evenement
        fields = (
            'pk',
            'url',
            'libelle_event',
            'date_event',
            'lieu_evenement',
            'theme_event',
            'user',
            'organisation',
            'commentaire',
            'date_creation_event',
            'guests',
        )


class ParticipantEventSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.SlugRelatedField(queryset=Evenement.objects.all(), slug_field='name')
    class Meta:
        model = ParticipantEvent
        fields = (
            'pk',
            'url',
            'participant',
            'event'
        )



class ReunionSerializer(serializers.HyperlinkedModelSerializer):
    guests = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='guests-detail')
    class Meta:
        model = Reunion
        fields = (
            'pk',
            'url',
            'libelle_reunion',
            'date_reunion',
            'lieu_reunion',
            'ordre_du_jour_reunion',
            'user',
            'organisation',
            'commentaire',
            'date_creation_reunion',
            'guests',
        )


class ParticipantReunionSerializer(serializers.HyperlinkedModelSerializer):
    reunion = serializers.SlugRelatedField(queryset=Evenement.objects.all(), slug_field='name')
    class Meta:
        model = ParticipantReunion
        fields = (
            'pk',
            'url',
            'participant',
            'reunion'
        )
