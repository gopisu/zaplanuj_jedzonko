# Generated by Django 2.2.6 on 2019-11-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0004_auto_20191112_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeplan',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
