# Generated by Django 3.0.7 on 2020-06-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200622_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='stack',
            field=models.CharField(choices=[('android', 'android'), ('cloud', 'cloud'), ('web', 'web'), ('assistant', 'assistant'), ('firebase', 'firebase'), ('ml', 'ml'), ('security', 'security'), ('design', 'design'), ('keynote', 'keynote'), ('misc', 'misc')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personbadge',
            name='badge',
            field=models.ManyToManyField(to='core.Badge'),
        ),
    ]
