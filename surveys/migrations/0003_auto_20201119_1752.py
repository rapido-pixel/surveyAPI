# Generated by Django 2.2 on 2020-11-19 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20201119_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_for_question', to='surveys.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]