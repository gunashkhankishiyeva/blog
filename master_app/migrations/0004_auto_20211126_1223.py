# Generated by Django 3.2.9 on 2021-11-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0003_bloginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogvillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villages', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogInfo',
        ),
    ]
