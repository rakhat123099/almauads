# Generated by Django 4.1.3 on 2022-11-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.CharField(choices=[('Lost', 'Lost'), ('Roommates', 'Roommates'), ('Job', 'Job'), ('Vacancies', 'Vacancies'), ('Events', 'Events'), ('Services', 'Services'), ('Garagesale', 'Garagesale'), ('Other', 'Other')], default='Other', max_length=255),
        ),
    ]