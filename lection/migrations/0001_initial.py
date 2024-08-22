# Generated by Django 4.1.13 on 2024-08-22 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Lection',
            fields=[
                ('lection_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название лекции')),
                ('annotation', models.TextField(verbose_name='Анонс лекции')),
                ('img', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
            ],
            options={
                'verbose_name': 'Лекция',
                'verbose_name_plural': 'Лекции',
                'ordering': ['title'],
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
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('tour_id', models.AutoField(primary_key=True, serialize=False)),
                ('title_tour', models.CharField(max_length=200, verbose_name='Название лекции')),
                ('price_single', models.CharField(blank=True, max_length=200, null=True, verbose_name='Цена для одного')),
                ('price_group', models.CharField(blank=True, max_length=200, null=True, verbose_name='Цена для группы')),
                ('meet_point', models.CharField(blank=True, max_length=200, null=True, verbose_name='Точка сборки')),
                ('duration', models.CharField(blank=True, max_length=200, null=True, verbose_name='Длительность')),
                ('annotation_tour', models.TextField(verbose_name='Анонс лекции')),
                ('questions', models.TextField(verbose_name='Вы узнаете ответы')),
                ('img_tour_main', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_1', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_2', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_3', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_4', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_5', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_6', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_7', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
                ('img_tour_8', models.ImageField(blank=True, null=True, upload_to='lection/', verbose_name='Фото в шапку страницы')),
            ],
            options={
                'verbose_name': 'Экскурсия',
                'verbose_name_plural': 'Экскурсии',
                'ordering': ['title_tour'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=60, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'ordering': ['type'],
            },
        ),
        migrations.AddIndex(
            model_name='type',
            index=models.Index(fields=['type'], name='lection_typ_type_da8fa6_idx'),
        ),
        migrations.AddField(
            model_name='tour',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_categories', to='lection.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tours', to='lection.tag'),
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['tag'], name='lection_tag_tag_a55f1f_idx'),
        ),
        migrations.AddField(
            model_name='lection',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lection_categories', to='lection.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='lection',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='lectures', to='lection.tag'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['category'], name='lection_cat_categor_68d33f_idx'),
        ),
        migrations.AddIndex(
            model_name='tour',
            index=models.Index(fields=['title_tour'], name='lection_tou_title_t_a32b4c_idx'),
        ),
        migrations.AddIndex(
            model_name='lection',
            index=models.Index(fields=['title'], name='lection_lec_title_a40bdc_idx'),
        ),
    ]