# Generated by Django 2.1.7 on 2019-03-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/comments'),
        ),
    ]