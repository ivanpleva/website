# Generated by Django 2.2.3 on 2019-09-23 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("weblate_web", "0022_auto_20190923_1725")]

    operations = [
        migrations.AddField(
            model_name="report",
            name="service",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="weblate_web.Service",
            ),
        )
    ]
