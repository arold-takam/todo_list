# Generated by Django 5.1 on 2024-08-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('day', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('draft', 'Brouillon'), ('published', 'Publier')], default='draft', max_length=10)),
            ],
        ),
    ]
