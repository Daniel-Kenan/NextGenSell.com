from django.db import models


class BusinessInfo(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class BusinessType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Client(models.Model):
    business_info = models.ForeignKey(BusinessInfo, on_delete=models.CASCADE)
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    industry = models.CharField(max_length=255, blank=True)
    employees = models.PositiveIntegerField(blank=True, null=True)
    locations = models.PositiveIntegerField(blank=True, null=True)
    years_in_operation = models.PositiveIntegerField(blank=True, null=True)
    current_pos_system = models.CharField(max_length=255, blank=True)
    reasons_for_change = models.TextField(blank=True)
    challenges_with_current_system = models.TextField(blank=True)

    desired_features = models.TextField(blank=True)
    integration_requirements = models.TextField(blank=True)
    budget = models.TextField(blank=True)

    avg_transactions_per_month = models.PositiveIntegerField(blank=True, null=True)
    peak_hours = models.CharField(max_length=255, blank=True)
    payment_methods_accepted = models.TextField(blank=True)

    customer_demographics = models.TextField(blank=True)
    loyalty_programs = models.TextField(blank=True)
    crm_needs = models.TextField(blank=True)

    TECHNICAL_EXPERTISE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    technical_expertise = models.CharField(max_length=10, choices=TECHNICAL_EXPERTISE_CHOICES, blank=True)
    training_availability = models.BooleanField(default=False)
    support_method = models.CharField(max_length=20, blank=True)

    expansion_plans = models.TextField(blank=True)
    scalability_requirements = models.TextField(blank=True)

    compliance_requirements = models.TextField(blank=True)
    industry_regulations = models.TextField(blank=True)

    previous_interactions = models.TextField(blank=True)
    meeting_notes = models.TextField(blank=True)

    competitors = models.TextField(blank=True)
    unique_selling_points = models.TextField(blank=True)

    decision_timeline = models.CharField(max_length=255, blank=True)
    decision_makers = models.TextField(blank=True)

    STATUS_CHOICES = [
        ('Potential', 'Potential Client'),
        ('Existing', 'Existing Client'),
        ('Lost', 'Lost Client'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Potential')

    def __str__(self):
        return self.business_info.name

class Device(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    installation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_name} - {self.client.business_info.name}"
    
class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    subscription_start_date = models.DateField()
    subscription_end_date = models.DateField()


class Doc(models.Model):
    name = models.CharField(max_length=18, unique=True)
    url = models.CharField(max_length=50)
    