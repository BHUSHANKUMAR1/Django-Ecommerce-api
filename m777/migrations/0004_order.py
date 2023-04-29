# Generated by Django 4.1.3 on 2023-04-05 07:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("m777", "0003_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.TextField(max_length=400, null=True)),
                ("mobile_no", models.BigIntegerField()),
                ("quantity", models.IntegerField()),
                ("price", models.IntegerField()),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 4, 5, 12, 48, 2, 907519)
                    ),
                ),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="m777.signup"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="m777.product"
                    ),
                ),
            ],
        ),
    ]