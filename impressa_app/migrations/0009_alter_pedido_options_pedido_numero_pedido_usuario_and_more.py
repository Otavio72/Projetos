# Generated by Django 5.1.7 on 2025-06-27 13:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impressa_app', '0008_rename_endereco2_pedido_complemento'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-data_criado']},
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero_pedido_usuario',
            field=models.PositiveBigIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pedido',
            unique_together={('user', 'numero_pedido_usuario')},
        ),
    ]
