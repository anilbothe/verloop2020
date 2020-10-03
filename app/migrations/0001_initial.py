# Generated by Django 3.0.10 on 2020-10-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodReadsAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('average_rating', models.CharField(max_length=50, null=True)),
                ('ratings_count', models.CharField(max_length=50, null=True)),
                ('num_pages', models.CharField(max_length=50, null=True)),
                ('image_url', models.CharField(max_length=50, null=True)),
                ('publication_year', models.CharField(max_length=50, null=True)),
                ('authors', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]