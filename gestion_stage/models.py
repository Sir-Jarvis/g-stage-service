from django.db import models


# Type de stage
OUVRIER = 'Ouvrier'
MAITRISE = 'Maitrise'
PFE = 'PFE'

TYPE_STAGE = [
    (OUVRIER, 'Ouvrier'),
    (MAITRISE, 'Maîtrise'),
    (PFE, 'PFE')
]


class PostulatdeStage(models.Model):
    cv = models.URLField(max_length=200)
    lettre_motivation = models.URLField(max_length=200, blank=True)
    type_stage = models.CharField(max_length=30, choices=TYPE_STAGE)
    duree_stage = models.CharField(max_length=30)
    eleve = models.IntegerField() # From user service
    organisation = models.IntegerField() # From organisation service
    date_creation = models.DateTimeField(auto_now_add=True)



class EvaluationOrganisation_Dept(models.Model):
    contenu_evaluation = models.TextField(max_length=300)
    note = models.FloatField(max_length=4, default=None)
    organisation = models.IntegerField() # From organisation service
    membre_dept = models.IntegerField() # From user service
    date_creation = models.DateTimeField(auto_now_add=True)



class EvaluationOrganisation_par_Eleve(models.Model):
    avis = models.TextField(max_length=300)
    eleve = models.IntegerField() # From user service
    organisation = models.IntegerField() # From organisation service
    related_dept_evaluation = models.ForeignKey(EvaluationOrganisation_Dept, related_name='avis_eleves', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)



class RapportdeStage(models.Model):
    annee_scolaire = models.IntegerField() # From user service
    file_rapport = models.URLField(max_length=200, blank=True)
    nom_rapport = models.CharField(max_length=200)
    maitre_stage = models.IntegerField() # From user service
    organisation = models.IntegerField() # From organisation service
    eleve = models.IntegerField() # From user service
    date_creation_rapport = models.DateTimeField(auto_now_add=True)
 


class Evenement(models.Model):
    libelle_event = models.CharField(max_length=100)
    date_event = models.DateTimeField()
    lieu_evenement = models.CharField(max_length=100)
    theme_event = models.CharField(max_length=150)
    user = models.IntegerField()
    organisation =models.IntegerField()
    commentaire = models.TextField(max_length=300)
    date_creation_event = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.libelle_event


class ParticipantEvent(models.Model):
    participant = models.IntegerField()
    event = models.ForeignKey(Evenement, related_name='guests', on_delete=models.CASCADE)

    def __str__(self):
        return self.participant


class Reunion(models.Model):
    libelle_reunion = models.CharField(max_length=100)
    date_reunion = models.DateTimeField()
    lieu_reunion = models.CharField(max_length=100)
    ordre_du_jour_reunion = models.CharField(max_length=150)
    user = models.IntegerField()
    organisation =models.IntegerField()
    commentaire = models.TextField(max_length=300)
    date_creation_reunion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.libelle_reunion


class ParticipantReunion(models.Model):
    participant = models.IntegerField()
    reunion = models.ForeignKey(Reunion, related_name='guests', on_delete=models.CASCADE)

    def __str__(self):
        return self.participant
