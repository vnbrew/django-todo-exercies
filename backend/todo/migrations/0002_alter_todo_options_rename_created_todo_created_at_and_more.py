# Generated by Django 4.1.6 on 2023-02-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
