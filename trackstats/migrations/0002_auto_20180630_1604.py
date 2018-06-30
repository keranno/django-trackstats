from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackstats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='StatisticByDate',
            name='value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='StatisticByDateAndObject',
            name='value',
            field=models.FloatField(null=True),
        ),
    ]
