# Generated by Django 2.0 on 2017-12-31 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171230_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['visible', '-date_time_modification']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_published',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
