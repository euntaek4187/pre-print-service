# Generated by Django 4.2.3 on 2024-08-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("preprint", "0003_order_locker_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_pages",
            field=models.IntegerField(default=0, verbose_name="총 페이지 수"),
        ),
    ]
