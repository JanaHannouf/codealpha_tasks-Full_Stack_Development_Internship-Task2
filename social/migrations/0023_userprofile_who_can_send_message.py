# Generated by Django 5.1.1 on 2024-10-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0022_tag_comment_tags_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='who_can_send_message',
            field=models.IntegerField(default=1),
        ),
    ]