# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 11:45
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=64)),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CashLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DBVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.IntegerField()),
                ('minor', models.IntegerField()),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[(b'NEW', b'New'), (b'FOL', b'Followup'), (b'NOT', b'Not Addressed'), (b'RES', b'Resolved')], default=b'FOL', max_length=3)),
                ('notes', models.TextField(default=b'')),
                ('diagnosedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('chronic', models.BooleanField(default=False)),
                ('icpc2Code', models.CharField(default=b'', max_length=5)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('note', models.TextField(default=b'')),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExamNoteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ImmunizationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[(b'ORD', b'Ordered'), (b'PEN', b'Pending'), (b'CAN', b'Canceled'), (b'COM', b'Complete'), (b'FAI', b'Failed')], max_length=3)),
                ('result', models.CharField(default=b'', max_length=32)),
                ('orderedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LabNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('note', models.TextField(default=b'')),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='LabType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('cost', models.FloatField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('dosage', models.CharField(max_length=64)),
                ('dispenseAmount', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[(b'ORD', b'Ordered'), (b'DIS', b'Dispensed'), (b'SUB', b'Substituted'), (b'CAN', b'Canceled')], max_length=3)),
                ('dispensedDateTime', models.DateTimeField(blank=True, null=True)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Diagnosis')),
                ('dispensedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dispensedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('note', models.TextField(default=b'')),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('med', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Med')),
            ],
        ),
        migrations.CreateModel(
            name='MedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('cost', models.FloatField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familyName', models.CharField(max_length=128, verbose_name=b'Last Name')),
                ('givenName', models.CharField(max_length=128, verbose_name=b'First Name')),
                ('middleName', models.CharField(blank=True, max_length=128, verbose_name=b'Middle Name')),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1)),
                ('birthYear', models.IntegerField(help_text=b'Year of Birth or Age', verbose_name=b'Year of Birth')),
                ('birthDate', models.DateField(blank=True, help_text=b'If Available, Not Required', null=True)),
                ('createdDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('scratchNote', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('altContactName', models.CharField(blank=True, max_length=32)),
                ('altContactPhone', models.CharField(blank=True, max_length=32)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(help_text=b'Doctor/Hospital/Specialist', max_length=64)),
                ('reason', models.TextField(blank=True)),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='SymptomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Vac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedDate', models.DateField()),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vac_added_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='VacNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('note', models.TextField(default=b'')),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='VacType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('quick', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduledDate', models.DateField(verbose_name=b'Date scheduled')),
                ('status', models.CharField(choices=[(b'SCHE', b'Scheduled'), (b'WAIT', b'Waiting'), (b'INPR', b'In Progress'), (b'CHOT', b'Checking Out'), (b'RESO', b'Resolved'), (b'MISS', b'Missed')], default=b'SCHE', max_length=4)),
                ('reason', models.CharField(choices=[(b'NEW', b'New'), (b'FOL', b'Followup')], default=b'NEW', max_length=3)),
                ('reasonDetail', models.TextField(default=b'', verbose_name=b'Reason for Visit')),
                ('seenDateTime', models.DateTimeField(blank=True, null=True, verbose_name=b'Seen')),
                ('claimedDateTime', models.DateTimeField(blank=True, null=True, verbose_name=b'Claimed')),
                ('finishedDateTime', models.DateTimeField(blank=True, null=True, verbose_name=b'Finished')),
                ('resolvedDateTime', models.DateTimeField(blank=True, null=True, verbose_name=b'Resolved')),
                ('cost', models.FloatField(default=0)),
                ('claimedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visit_claimed_by', to=settings.AUTH_USER_MODEL)),
                ('finishedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visit_finished_by', to=settings.AUTH_USER_MODEL)),
                ('followupTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient')),
                ('resolvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visit_resolved_by', to=settings.AUTH_USER_MODEL)),
                ('scheduledBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_scheduled_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VisitSymptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(default=b'')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.SymptomType')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit')),
            ],
        ),
        migrations.CreateModel(
            name='Vital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observedDateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('data', models.FloatField()),
                ('observedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='VitalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('unit', models.CharField(default=b'', max_length=32)),
                ('minValue', models.FloatField(default=-1024)),
                ('maxValue', models.FloatField(default=1024)),
            ],
        ),
        migrations.AddField(
            model_name='vital',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.VitalType'),
        ),
        migrations.AddField(
            model_name='vital',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit'),
        ),
        migrations.AddField(
            model_name='vacnote',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.VacType'),
        ),
        migrations.AddField(
            model_name='vac',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.VacType'),
        ),
        migrations.AddField(
            model_name='referral',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit'),
        ),
        migrations.AddField(
            model_name='patient',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Village'),
        ),
        migrations.AddField(
            model_name='med',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient'),
        ),
        migrations.AddField(
            model_name='med',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.MedType'),
        ),
        migrations.AddField(
            model_name='med',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit'),
        ),
        migrations.AddField(
            model_name='lab',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient'),
        ),
        migrations.AddField(
            model_name='lab',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.LabType'),
        ),
        migrations.AddField(
            model_name='lab',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit'),
        ),
        migrations.AddField(
            model_name='immunizationlog',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient'),
        ),
        migrations.AddField(
            model_name='examnote',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.ExamNoteType'),
        ),
        migrations.AddField(
            model_name='examnote',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.DiagnosisType'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit'),
        ),
        migrations.AddField(
            model_name='cashlog',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient'),
        ),
        migrations.AddField(
            model_name='cashlog',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Visit'),
        ),
        migrations.AddField(
            model_name='allergy',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocemr.Patient'),
        ),
    ]