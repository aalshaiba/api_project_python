# Generated by Django 2.2.4 on 2019-11-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islam_api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Droosuae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('shaikh', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'droosUAE',
                'managed': False,
            },
        ),
    ]