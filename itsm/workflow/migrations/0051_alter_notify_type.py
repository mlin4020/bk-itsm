# Generated by Django 3.2.4 on 2022-04-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0050_auto_20220406_1748"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notify",
            name="type",
            field=models.CharField(default="EMAIL", max_length=32, verbose_name="通知渠道"),
        ),
    ]