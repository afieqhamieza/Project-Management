# Generated by Django 3.0.7 on 2020-07-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Projects',
            field=models.ManyToManyField(to='employee.Project'),
        ),
    ]
