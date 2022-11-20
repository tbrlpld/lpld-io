# Generated by Django 4.0.8 on 2022-11-20 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0002_copy_data'),
        ('projects', '0004_projectpage_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttechnologyrelation',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_projects', to='technologies.technology'),
        ),
    ]
