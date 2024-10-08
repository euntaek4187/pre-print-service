# Generated by Django 4.2.3 on 2024-08-23 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("preprint", "0004_order_total_pages"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArchivedOrder",
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
                ("order_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("order_pw", models.CharField(max_length=4)),
                ("order_color", models.CharField(max_length=2)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("locker_number", models.IntegerField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("requested", "주문요청"),
                            ("failed_payment", "결제실패"),
                            ("paid", "결제완료"),
                            ("prepared_product", "상품준비중"),
                            ("shipped", "배송중"),
                            ("delivered", "배송완료"),
                            ("cancelled", "주문취소"),
                        ],
                        default="requested",
                        max_length=20,
                    ),
                ),
                ("total_pages", models.IntegerField(default=0)),
                ("archived_at", models.DateTimeField(auto_now_add=True)),
                (
                    "order_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Archived Order",
                "verbose_name_plural": "Archived Orders",
                "db_table": "archived_order",
            },
        ),
        migrations.CreateModel(
            name="ArchivedOrderPayment",
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
                (
                    "meta",
                    models.JSONField(
                        default=dict, editable=False, verbose_name="포트원 결제내역"
                    ),
                ),
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        verbose_name="쇼핑몰 결제식별자",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="결제명")),
                (
                    "desired_amount",
                    models.PositiveIntegerField(
                        editable=False, verbose_name="결제금액"
                    ),
                ),
                (
                    "buyer_name",
                    models.CharField(
                        editable=False, max_length=100, verbose_name="구매자 이름"
                    ),
                ),
                (
                    "buyer_email",
                    models.EmailField(
                        editable=False, max_length=254, verbose_name="구매자 이메일"
                    ),
                ),
                (
                    "pay_method",
                    models.CharField(
                        choices=[("card", "신용카드")],
                        default="card",
                        max_length=20,
                        verbose_name="결제수단",
                    ),
                ),
                (
                    "pay_status",
                    models.CharField(
                        choices=[
                            ("ready", "결제 준비"),
                            ("paid", "결제 완료"),
                            ("cancelled", "결제 취소"),
                            ("failed", "결제 실패"),
                        ],
                        default="ready",
                        max_length=20,
                        verbose_name="결제상태",
                    ),
                ),
                (
                    "is_paid_ok",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        editable=False,
                        verbose_name="결제성공 여부",
                    ),
                ),
                (
                    "archived_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="아카이빙 날짜"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="preprint.archivedorder",
                    ),
                ),
            ],
            options={
                "verbose_name": "Archived Order Payment",
                "verbose_name_plural": "Archived Order Payments",
                "db_table": "archived_order_payment",
            },
        ),
        migrations.CreateModel(
            name="ArchivedOrderFile",
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
                ("file", models.FileField(upload_to="archived_files/")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="preprint.archivedorder",
                    ),
                ),
            ],
            options={
                "verbose_name": "Archived Order File",
                "verbose_name_plural": "Archived Order Files",
                "db_table": "archived_order_file",
            },
        ),
    ]
