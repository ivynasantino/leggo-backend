# Generated by Django 2.1.3 on 2018-12-17 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_tramitacaoevent_texto_tramitacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tramitacaoevent',
            name='texto',
        ),
    ]
