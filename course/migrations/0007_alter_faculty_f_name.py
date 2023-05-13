# Generated by Django 3.2 on 2023-05-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20230512_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='f_name',
            field=models.CharField(choices=[('Agricultural Science', 'Agricultural Science'), ('Arts', 'Arts'), ('Biological Science', 'Biological Science'), ('Management Science', 'Management Science'), ('Densitry', 'Densitry'), ('Education', 'Education'), ('Engineering', 'Engineering'), ('Health Science and Technology', 'Health Science and Technology'), ('Law', 'Law'), ('Medical Science', 'Medical Science'), ('Pharmaceutical Science', 'Pharmaceutical Science'), ('Physical Science', 'Physical Science'), ('Veterinary Medicine', 'Veterinary Medicine'), ('', 'Choose A Faculty')], default='', max_length=100, verbose_name='Faculty'),
        ),
    ]
