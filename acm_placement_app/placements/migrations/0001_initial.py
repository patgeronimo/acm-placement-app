# Generated by Django 2.1.8 on 2019-05-29 07:08

import acm_placement_app.placements.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('started', models.DateTimeField(blank=True, editable=False, null=True)),
                ('school_data_file', models.FileField(upload_to=acm_placement_app.placements.models.input_upload_path)),
                ('acm_survey_data_file', models.FileField(upload_to=acm_placement_app.placements.models.input_upload_path, verbose_name='ACM survey data file')),
                ('num_iterations', models.IntegerField(default=10000, help_text='The number of team placements that will be attempted. 10,000 or more is recommended.', verbose_name='Number of iterations')),
                ('prevent_roommates', models.BooleanField(default=True, verbose_name='Prevent roommates from serving on the same team?')),
                ('consider_HS_elig', models.BooleanField(default=True, help_text='ACMs are eligible to serve in High School if they are 21+ years old (or have college experience) and are confident tutoring at least algebra-level math.', verbose_name='Apply High School eligibility rule?')),
                ('calc_commutes', models.BooleanField(default=True, help_text='Commute calculations cost HQ a small amount and take time to complete. For 100 ACMs and 10 schools, the cost is $5 and takes about 10 minutes.', verbose_name='Calculate commutes?')),
                ('commute_date', models.DateField(blank=True, default=acm_placement_app.placements.models.get_tomorrow_date, help_text='Required if calculating commutes. Choose a date that represents normal traffic.', verbose_name='Travel date for commute calculations')),
                ('commutes_reference_file', models.FileField(blank=True, help_text="After placements are made, you will find a 'Output_Commute_Reference.csv' file in the results. If you want to run additional placement processes, upload that file here to avoid commute calculation wait time and cost.", upload_to=acm_placement_app.placements.models.input_upload_path)),
                ('commute_factor', models.IntegerField(default=1, verbose_name='Importance of commute')),
                ('ethnicity_factor', models.IntegerField(default=1, verbose_name='Importance of ethnic diversity')),
                ('gender_factor', models.IntegerField(default=1, verbose_name='Importance of gender diversity')),
                ('edscore_factor', models.IntegerField(default=1, verbose_name='Importance of educational attainment diversity')),
                ('spanish_factor', models.IntegerField(default=1, verbose_name='Importance of matching Spanish speaker targets')),
                ('errors', models.TextField(blank=True)),
                ('requested_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlacementResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('commutes_file', models.FileField(upload_to=acm_placement_app.placements.models.output_upload_path)),
                ('placements_file', models.FileField(upload_to=acm_placement_app.placements.models.output_upload_path)),
                ('trace_file', models.FileField(upload_to=acm_placement_app.placements.models.output_upload_path)),
                ('placementrequest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='placements.PlacementRequest')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
