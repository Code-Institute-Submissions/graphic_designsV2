# Generated by Django 3.0.2 on 2020-06-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200622_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='finish',
            field=models.CharField(blank=True, default=False, max_length=254, null=True),
        ),
    ]