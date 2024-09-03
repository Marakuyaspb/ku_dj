# Generated by Django 4.1.13 on 2024-09-03 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('img_article', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_article_1', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_article_2', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_article_3', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_article_4', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=60, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ключевое слово')),
            ],
            options={
                'verbose_name': 'Ключевое слово',
                'verbose_name_plural': 'Ключевые слова',
                'ordering': ['tag'],
            },
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['tag'], name='blog_tag_tag_00154f_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['category'], name='blog_catego_categor_dd353c_idx'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lection_categories', to='blog.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='lectures', to='blog.tag'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['title'], name='blog_articl_title_525ebf_idx'),
        ),
    ]
