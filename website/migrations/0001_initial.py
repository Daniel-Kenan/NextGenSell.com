# Generated by Django 5.0.3 on 2024-04-12 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_name', models.CharField(blank=True, max_length=255)),
                ('position', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18, unique=True)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(blank=True, max_length=255)),
                ('employees', models.PositiveIntegerField(blank=True, null=True)),
                ('locations', models.PositiveIntegerField(blank=True, null=True)),
                ('years_in_operation', models.PositiveIntegerField(blank=True, null=True)),
                ('current_pos_system', models.CharField(blank=True, max_length=255)),
                ('reasons_for_change', models.TextField(blank=True)),
                ('challenges_with_current_system', models.TextField(blank=True)),
                ('desired_features', models.TextField(blank=True)),
                ('integration_requirements', models.TextField(blank=True)),
                ('budget', models.TextField(blank=True)),
                ('avg_transactions_per_month', models.PositiveIntegerField(blank=True, null=True)),
                ('peak_hours', models.CharField(blank=True, max_length=255)),
                ('payment_methods_accepted', models.TextField(blank=True)),
                ('customer_demographics', models.TextField(blank=True)),
                ('loyalty_programs', models.TextField(blank=True)),
                ('crm_needs', models.TextField(blank=True)),
                ('technical_expertise', models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=10)),
                ('training_availability', models.BooleanField(default=False)),
                ('support_method', models.CharField(blank=True, max_length=20)),
                ('expansion_plans', models.TextField(blank=True)),
                ('scalability_requirements', models.TextField(blank=True)),
                ('compliance_requirements', models.TextField(blank=True)),
                ('industry_regulations', models.TextField(blank=True)),
                ('previous_interactions', models.TextField(blank=True)),
                ('meeting_notes', models.TextField(blank=True)),
                ('competitors', models.TextField(blank=True)),
                ('unique_selling_points', models.TextField(blank=True)),
                ('decision_timeline', models.CharField(blank=True, max_length=255)),
                ('decision_makers', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Potential', 'Potential Client'), ('Existing', 'Existing Client'), ('Lost', 'Lost Client')], default='Potential', max_length=10)),
                ('business_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.businessinfo')),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.businesstype')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=255)),
                ('installation_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.client')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('subscription_start_date', models.DateField()),
                ('subscription_end_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.client')),
            ],
        ),
    ]
