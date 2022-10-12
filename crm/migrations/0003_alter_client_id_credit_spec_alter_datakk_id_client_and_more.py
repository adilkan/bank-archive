# Generated by Django 4.1.1 on 2022-10-11 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('crm', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_credit_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.specuser', verbose_name='Кредитный специалист'),
        ),
        migrations.AlterField(
            model_name='datakk',
            name='id_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.entity', verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='datakk',
            name='id_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.specuser', verbose_name='Кредитный спец'),
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to='company_files/%Y/%m/%d', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='files',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.property', verbose_name='Залоговое имущество'),
        ),
    ]
