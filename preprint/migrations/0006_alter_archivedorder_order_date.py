# Generated by Django 4.2.3 on 2024-08-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("preprint", "0005_archivedorder_archivedorderpayment_archivedorderfile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archivedorder",
            name="order_date",
            field=models.DateTimeField(),
        ),
    ]
