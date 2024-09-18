# Generated by Django 4.2.13 on 2024-09-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("overview", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField()),
                ("author", models.CharField(max_length=255)),
                ("thumbnail", models.ImageField(blank=True, null=True, upload_to="")),
                ("featured", models.BooleanField(default=False)),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
    ]
