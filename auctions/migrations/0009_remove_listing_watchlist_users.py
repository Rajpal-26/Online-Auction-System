# Generated by Django 3.2.5 on 2021-07-16 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_watchlist_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist_users',
        ),
    ]
