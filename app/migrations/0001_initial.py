# Generated by Django 4.0.4 on 2022-05-26 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextArabic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=600)),
                ('audio', models.FileField(upload_to='media/audio')),
            ],
        ),
        migrations.CreateModel(
            name='TextFrench',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=600)),
                ('vocal_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.textarabic')),
            ],
        ),
    ]
