# Generated by Django 4.0.6 on 2022-08-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_name_person_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Person_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='Person_phno',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
