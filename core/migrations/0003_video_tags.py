# Generated by Django 5.1.2 on 2024-10-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag_alter_video_options_alter_video_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='core.tag'),
        ),
    ]