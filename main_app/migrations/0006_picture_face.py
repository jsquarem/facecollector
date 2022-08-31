# Generated by Django 4.1 on 2022-08-31 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_face_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='face',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.face'),
            preserve_default=False,
        ),
    ]