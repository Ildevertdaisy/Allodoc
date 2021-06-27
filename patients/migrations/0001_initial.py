# Generated by Django 3.2.3 on 2021-06-27 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('photo', models.ImageField(null=True, upload_to='patients/%Y/%m/%d/')),
                ('street', models.CharField(max_length=200, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.city')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.state')),
                ('zip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.zip')),
            ],
        ),
    ]