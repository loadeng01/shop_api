# Generated by Django 4.2.7 on 2023-11-23 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.CharField(choices=[('in_stock', 'в наличии'), ('out_of_stock', 'нет в наличии')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='category.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
