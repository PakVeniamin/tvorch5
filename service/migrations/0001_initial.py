# Generated by Django 4.1.7 on 2023-03-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('credit_term', models.IntegerField(choices=[(4, '4 месяца'), (6, '6 месяцев')])),
                ('commission', models.DecimalField(decimal_places=2, max_digits=8)),
                ('commission_held', models.BooleanField(default=False)),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]