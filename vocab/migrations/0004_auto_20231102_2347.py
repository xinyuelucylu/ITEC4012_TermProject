# Generated by Django 3.2.22 on 2023-11-03 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0003_auto_20231102_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservocabulary',
            name='clothes',
        ),
        migrations.RemoveField(
            model_name='uservocabulary',
            name='family',
        ),
        migrations.RemoveField(
            model_name='uservocabulary',
            name='numbers',
        ),
        migrations.DeleteModel(
            name='Clothes',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='Numbers',
        ),
    ]
