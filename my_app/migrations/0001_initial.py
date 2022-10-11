# Generated by Django 4.0.5 on 2022-09-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.CharField(max_length=5, null=True)),
                ('batchname', models.CharField(max_length=5, null=True)),
                ('goodsserial', models.CharField(max_length=20, null=True)),
                ('barcode', models.CharField(max_length=20, null=True)),
                ('goodsname', models.CharField(max_length=20, null=True)),
                ('goodstype', models.CharField(max_length=20, null=True)),
                ('inputsize', models.CharField(max_length=20, null=True)),
                ('quantity', models.CharField(max_length=20, null=True)),
                ('totalprice', models.CharField(max_length=20, null=True)),
                ('unitprice', models.CharField(max_length=20, null=True)),
                ('costunitprice', models.CharField(max_length=20, null=True)),
                ('costtotalprice', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=10, null=True)),
                ('createtime', models.DateTimeField(auto_now=True)),
                ('beizhu', models.CharField(max_length=500)),
            ],
        ),
    ]
