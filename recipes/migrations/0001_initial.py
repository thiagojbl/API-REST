# Generated by Django 4.0 on 2022-08-02 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0002_remove_tag_content_type_remove_tag_object_id'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, verbose_name='Title')),
                ('description', models.CharField(max_length=165)),
                ('slug', models.SlugField(unique=True)),
                ('preparation_time', models.IntegerField()),
                ('preparation_time_unit', models.CharField(max_length=65)),
                ('servings', models.IntegerField()),
                ('servings_unit', models.CharField(max_length=65)),
                ('preparation_steps', models.TextField()),
                ('preparation_steps_is_html', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, default='', upload_to='recipes/covers/%Y/%m/%d/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='tag.Tag')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
            },
        ),
    ]
