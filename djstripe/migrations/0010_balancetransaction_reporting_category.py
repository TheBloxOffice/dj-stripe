# Generated by Django 3.1a1 on 2020-05-31 05:43

from django.db import migrations

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0009_auto_20200531_0437"),
    ]

    operations = [
        migrations.AddField(
            model_name="balancetransaction",
            name="reporting_category",
            field=djstripe.fields.StripeEnumField(
                default="",
                enum=djstripe.enums.BalanceTransactionReportingCategory,
                help_text="More information: https://stripe.com/docs/reports/reporting-categories",
                max_length=29,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="balancetransaction",
            name="source",
            field=djstripe.fields.StripeIdField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
