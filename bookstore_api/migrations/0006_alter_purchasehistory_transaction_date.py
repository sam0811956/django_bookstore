# Generated by Django 3.2 on 2021-04-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0005_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasehistory',
            name='transaction_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
