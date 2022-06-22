# Generated by Django 4.0.1 on 2022-01-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0012_account_djstripe_owner_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="api_version",
            field=models.CharField(
                blank=True,
                help_text="the API version at which the event data was rendered. Blank for old entries only, all new entries will have this value",
                max_length=64,
            ),
        ),
        migrations.AlterField(
            model_name="webhookendpoint",
            name="api_version",
            field=models.CharField(
                max_length=64,
                blank=True,
                help_text="The API version events are rendered as for this webhook endpoint. Defaults to the configured Stripe API Version.",
            ),
        ),
    ]