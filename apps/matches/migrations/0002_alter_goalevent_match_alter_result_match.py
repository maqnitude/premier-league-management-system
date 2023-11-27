# Generated by Django 4.2.7 on 2023-11-26 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalevent',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.match'),
        ),
        migrations.AlterField(
            model_name='result',
            name='match',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result', to='matches.match'),
        ),
    ]
