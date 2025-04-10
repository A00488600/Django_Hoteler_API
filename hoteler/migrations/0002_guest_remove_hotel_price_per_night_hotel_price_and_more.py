# Generated by Django 5.2 on 2025-04-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hoteler", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Guest",
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
                ("guest_name", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name="hotel",
            name="price_per_night",
        ),
        migrations.AddField(
            model_name="hotel",
            name="price",
            field=models.IntegerField(default=100),
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("hotel_name", models.CharField(max_length=100)),
                ("checkin", models.CharField(max_length=50)),
                ("checkout", models.CharField(max_length=50)),
                ("confirmation_number", models.CharField(max_length=100)),
                ("guests", models.ManyToManyField(to="hoteler.guest")),
            ],
        ),
    ]
