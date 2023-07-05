# Generated by Django 4.1.7 on 2023-07-05 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('round', models.IntegerField()),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('academic_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.academicprogram')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.gender')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.institute')),
                ('seat_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.seattype')),
            ],
        ),
        migrations.AddField(
            model_name='academicprogram',
            name='institute_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.institute'),
        ),
        migrations.AlterUniqueTogether(
            name='academicprogram',
            unique_together={('institute_name', 'name')},
        ),
    ]