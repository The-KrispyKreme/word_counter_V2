# Generated by Django 4.0.5 on 2022-06-16 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('year', models.IntegerField(max_length=4)),
                ('author', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WordCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_counts', to='word_app.document')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_counts', to='word_app.word')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='words',
            field=models.ManyToManyField(related_name='documents', to='word_app.word'),
        ),
    ]