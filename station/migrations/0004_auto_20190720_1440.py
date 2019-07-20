# Generated by Django 2.2.3 on 2019-07-20 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0003_auto_20190720_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='station.Station'),
            preserve_default=False,
        ),
    ]