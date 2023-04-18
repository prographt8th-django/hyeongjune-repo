# Generated by Django 4.1.7 on 2023-04-11 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=31)),
                ('name', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='AreaVisitStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('all', 'all'), ('female', 'female'), ('male', 'male')], default='all', max_length=31)),
                ('age_group', models.CharField(choices=[('ten', 'ten'), ('female', 'twenty'), ('male', 'thirty'), ('forty', 'forty'), ('fifty', 'fifty'), ('sixty_over', 'sixty_over')], default='female', max_length=31)),
                ('companion', models.CharField(choices=[('family', 'family'), ('not_family', 'not_family'), ('family_with_child', 'family_with_child')], default='not_family', max_length=31)),
                ('travel_count', models.PositiveIntegerField(default=0)),
                ('travel_date', models.DateField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.area')),
            ],
        ),
    ]
