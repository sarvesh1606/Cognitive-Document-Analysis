# Generated by Django 3.1.6 on 2021-03-21 13:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210318_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('acc_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
