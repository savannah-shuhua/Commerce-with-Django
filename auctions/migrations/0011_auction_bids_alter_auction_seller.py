# Generated by Django 4.0.6 on 2022-08-21 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_user_watchlist_auction_fav'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='bids',
            field=models.ManyToManyField(through='auctions.Bid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales', to=settings.AUTH_USER_MODEL),
        ),
    ]
