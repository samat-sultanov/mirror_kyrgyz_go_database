# Generated by Django 4.1.7 on 2023-03-02 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_file_remove_player_egf_placement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок новости')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст новости')),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='news_images', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='news', to=settings.AUTH_USER_MODEL, verbose_name='Автор новости')),
            ],
        ),
    ]
