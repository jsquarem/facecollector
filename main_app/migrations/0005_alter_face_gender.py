# Generated by Django 4.1 on 2022-08-31 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_picture_face_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Non-Binary'), ('R', 'Rather Not Say')], default='N', max_length=1),
        ),
    ]