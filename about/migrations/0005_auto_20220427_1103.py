# Generated by Django 3.2 on 2022-04-27 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_beds_equipmentinfo_staff'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Beds',
            new_name='Bed',
        ),
        migrations.AddField(
            model_name='equipmentinfo',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='about.hospital'),
        ),
        migrations.AddField(
            model_name='staff',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='about.hospital'),
        ),
        migrations.AddField(
            model_name='staff',
            name='number',
            field=models.CharField(blank=True, choices=[('Permanent', 'Permanent'), ('Temporary', 'Temporary'), ('Development Committee', 'Development Committee')], max_length=255, null=True),
        ),
    ]
