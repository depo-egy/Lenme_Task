# Generated by Django 3.0.5 on 2021-06-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenme', '0002_auto_20210619_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='investor',
            name='fName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='investor',
            name='lName',
            field=models.CharField(max_length=50),
        ),
    ]
