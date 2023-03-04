# Generated by Django 4.1.7 on 2023-03-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_player_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='clubs',
            field=models.ManyToManyField(blank=True, null=True, related_name='players', to='webapp.club'),
        ),
    ]
