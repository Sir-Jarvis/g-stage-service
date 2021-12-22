from django.urls import path
from gestion_stage import views

urlpatterns = [
    # Postulats de stage
    path('postulats/', views.PostulatAPIView.as_view()),
    path('postulats-de-stage/', views.PostulatdeStageList.as_view(), name=views.PostulatdeStageList.name),
    path('postulats-de-stage/<int:pk>/', views.PostulatdeStageDetail.as_view(), name=views.PostulatdeStageDetail.name),

    # Evaluations des organisations par les départements
    path('eval-organ-par-dept/', views.EvaluationOrganisation_DeptList.as_view(), name=views.EvaluationOrganisation_DeptList.name),
    path('eval-organ-par-dept/<int:pk>/', views.EvaluationOrganisation_DeptDetail.as_view(), name=views.EvaluationOrganisation_DeptDetail.name),

    # Evaluations des organisations par les élèves
    path('avis-eleves/', views.EvaluationOrganisation_par_EleveList.as_view(), name=views.EvaluationOrganisation_par_EleveList.name),
    path('avis-eleves/<int:pk>/', views.EvaluationOrganisation_par_EleveDetail.as_view(), name=views.EvaluationOrganisation_par_EleveDetail.name),

    # les rapports de stages
    path('rapports-stage/', views.RapportdeStageAPIView.as_view()),
    path('rapports-de-stage/', views.RapportdeStageList.as_view(), name=views.RapportdeStageList.name),
    path('rapports-de-stage/<int:pk>/', views.RapportdeStageDetail.as_view(), name=views.RapportdeStageDetail.name),

    # Les évènements
    path('evenements/', views.EvenementList.as_view(), name=views.EvenementList.name),
    path('evenements/<int:pk>/', views.EvenementDetail.as_view(), name=views.EvenementDetail.name),

    # Les participants des évènements
    path('participants-evenements/', views.ParticipantEventList.as_view(), name=views.ParticipantEventList.name),
    path('participants-evenements/<int:pk>/', views.ParticipantEventDetail.as_view(), name=views.ParticipantEventDetail.name),

    # Les réunions
    path('reunions/', views.ReunionList.as_view(), name=views.ReunionList.name),
    path('reunions/<int:pk>/', views.ReunionDetail.as_view(), name=views.ReunionDetail.name),

    # Les participants des réunions
    path('participants-renions/', views.ParticipantReunionList.as_view(), name=views.ParticipantReunionList.name),
    path('participants-reunions/<int:pk>/', views.ParticipantReunionDetail.as_view(), name=views.ParticipantReunionDetail.name),
    # root endpoint for the web service
    path ('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]