# Generated by Django 4.0.4 on 2022-06-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.CharField(default='admin', max_length=40),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
