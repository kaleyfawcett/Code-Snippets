# Generated by Django 3.0.6 on 2020-06-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200608_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesnippet',
            name='language',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JAVASCRIPT', 'JavaScript'), ('PYTHON', 'Python')], default='HTML', max_length=100),
        ),
    ]