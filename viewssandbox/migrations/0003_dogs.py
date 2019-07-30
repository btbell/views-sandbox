# Generated by Django 2.0 on 2019-07-30 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewssandbox', '0002_auto_20190726_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('commonfield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewssandbox.CommonField')),
                ('pet_name', models.CharField(help_text='Please enter a first name.', max_length=40)),
                ('owner_last_name', models.CharField(max_length=60)),
                ('attend_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('viewssandbox.commonfield',),
        ),
    ]