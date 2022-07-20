# Generated by Django 4.0.6 on 2022-07-20 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_publication_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='blog.publication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]