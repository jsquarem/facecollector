# Generated by Django 4.1 on 2022-08-29 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_face_hotess'),
    ]

    operations = [
        migrations.RenameField(
            model_name='face',
            old_name='hotess',
            new_name='hotness',
        ),
    ]