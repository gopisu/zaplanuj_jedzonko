# Generated by Django 2.2.7 on 2019-11-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0005_recipeplan_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeplan',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
