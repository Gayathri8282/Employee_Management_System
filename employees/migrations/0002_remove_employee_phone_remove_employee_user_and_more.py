# Generated by Django 5.1.2 on 2024-12-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AlterField(
            model_name='employee',
            name='courses',
            field=models.CharField(choices=[('MCA', 'MCA'), ('BCA', 'BCA'), ('BSC', 'BSC')], max_length=3),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(choices=[('HR', 'HR'), ('Manager', 'Manager'), ('Sales', 'Sales')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
