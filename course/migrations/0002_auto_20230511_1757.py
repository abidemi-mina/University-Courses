# Generated by Django 3.2 on 2023-05-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name_plural': 'Draprtments'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name_plural': 'Faculties'},
        ),
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='depts',
            field=models.ManyToManyField(to='course.Department'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='dept',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='img',
            field=models.ImageField(blank=True, help_text='Upload your image ', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
