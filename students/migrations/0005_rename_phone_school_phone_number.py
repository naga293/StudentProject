# Generated by Django 4.1.1 on 2022-09-07 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_book_page_count_school_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='phone',
            new_name='phone_number',
        ),
    ]