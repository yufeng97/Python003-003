# Generated by Django 3.1.1 on 2020-09-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(max_length=1)),
                ('comment', models.TextField()),
            ],
        ),
    ]