# Generated by Django 4.0.4 on 2022-06-16 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_topic_remove_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.topic'),
        ),
    ]