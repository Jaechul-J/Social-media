# Generated by Django 4.0.3 on 2022-06-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect', '0002_post_alter_profile_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
