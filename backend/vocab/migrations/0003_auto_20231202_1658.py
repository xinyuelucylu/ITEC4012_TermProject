# Generated by Django 3.2.23 on 2023-12-02 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0002_auto_20231202_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservocabulary',
            name='numbers',
        ),
        migrations.DeleteModel(
            name='Numbers',
        ),
    ]