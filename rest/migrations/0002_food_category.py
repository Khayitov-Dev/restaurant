# Generated by Django 3.2.9 on 2021-11-16 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='rest.category'),
            preserve_default=False,
        ),
    ]
