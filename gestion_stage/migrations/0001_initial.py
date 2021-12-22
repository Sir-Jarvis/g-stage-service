# Generated by Django 4.0 on 2021-12-22 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationOrganisation_Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu_evaluation', models.TextField(max_length=300)),
                ('note', models.FloatField(default=None, max_length=4)),
                ('organisation', models.IntegerField()),
                ('membre_dept', models.IntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_event', models.CharField(max_length=100)),
                ('date_event', models.DateTimeField()),
                ('lieu_evenement', models.CharField(max_length=100)),
                ('theme_event', models.CharField(max_length=150)),
                ('user', models.IntegerField()),
                ('organisation', models.IntegerField()),
                ('commentaire', models.TextField(max_length=300)),
                ('date_creation_event', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostulatdeStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.URLField()),
                ('lettre_motivation', models.URLField(blank=True)),
                ('type_stage', models.CharField(choices=[('Ouvrier', 'Ouvrier'), ('Maitrise', 'Maîtrise'), ('PFE', 'PFE')], max_length=30)),
                ('duree_stage', models.CharField(max_length=30)),
                ('eleve', models.IntegerField()),
                ('organisation', models.IntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RapportdeStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_scolaire', models.IntegerField()),
                ('file_rapport', models.URLField(blank=True)),
                ('nom_rapport', models.CharField(max_length=200)),
                ('maitre_stage', models.IntegerField()),
                ('organisation', models.IntegerField()),
                ('eleve', models.IntegerField()),
                ('date_creation_rapport', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_reunion', models.CharField(max_length=100)),
                ('date_reunion', models.DateTimeField()),
                ('lieu_reunion', models.CharField(max_length=100)),
                ('ordre_du_jour_reunion', models.CharField(max_length=150)),
                ('user', models.IntegerField()),
                ('organisation', models.IntegerField()),
                ('commentaire', models.TextField(max_length=300)),
                ('date_creation_reunion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantReunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.IntegerField()),
                ('reunion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='gestion_stage.reunion')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='gestion_stage.evenement')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationOrganisation_par_Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avis', models.TextField(max_length=300)),
                ('eleve', models.IntegerField()),
                ('organisation', models.IntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('related_dept_evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avis_eleves', to='gestion_stage.evaluationorganisation_dept')),
            ],
        ),
    ]
