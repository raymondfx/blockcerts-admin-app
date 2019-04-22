from django.db import models
from uuid import uuid4
# Create your models here.

def get_uuid():
    return str(uuid4())

class Credential(models.Model):
    title = models.TextField()
    description = models.TextField()
    narrative = models.TextField()
    issuing_department = models.CharField(max_length=50)
    badge_id = models.TextField(default=get_uuid)


class Issuance(models.Model):
    date_issue = models.DateField()
    certificate_template = models.TextField(default='')
    url_id = models.TextField(default='')
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE)


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    public_address = models.CharField(max_length=250, default='')
    nonce = models.CharField(max_length=50, default='')
    add_issuer_timestamp = models.DateTimeField(auto_now_add=True)


class CertMailerConfig(models.Model):
    config = models.TextField()


class CertToolsConfig(models.Model):
    config = models.TextField()


class PersonIssuances(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    issuance = models.ForeignKey(Issuance, on_delete=models.CASCADE)
    is_issued = models.BooleanField(default=False)
    unsigned_certificate = models.TextField(default='')