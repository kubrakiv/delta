# Generated by Django 4.2.6 on 2024-04-28 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_platform_order_platform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="base.paymenttype",
            ),
        ),
    ]
