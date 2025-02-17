# Generated by Django 3.0.7 on 2020-07-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagement', '0004_auto_20200626_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('staffId', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='engagement',
            name='staff',
        ),
        migrations.AddField(
            model_name='engagement',
            name='staff',
            field=models.ManyToManyField(to='engagement.Staff'),
        ),
    ]
