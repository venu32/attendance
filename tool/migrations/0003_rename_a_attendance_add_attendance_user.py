# Generated by Django 4.0.5 on 2022-06-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_alter_attendance_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='a',
            new_name='add',
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.CharField(default='', max_length=50),
        ),
    ]