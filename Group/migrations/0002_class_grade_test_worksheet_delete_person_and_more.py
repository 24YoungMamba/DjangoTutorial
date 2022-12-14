# Generated by Django 4.0.4 on 2022-09-22 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128, unique=True)),
                ('students', models.ManyToManyField(related_name='classes', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(choices=[('F', 0), ('D', 60), ('C', 70), ('B', 80), ('A', 100)], default=('F', 0))),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=52)),
                ('guide_lines', models.FileField(upload_to='guide_lines/')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Group.class')),
            ],
        ),
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet', models.FileField(upload_to='worksheets/')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_worksheets', to='Group.test')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='grade',
            name='worksheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Group.worksheet'),
        ),
    ]
