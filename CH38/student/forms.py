from django import forms
from .models import Profile

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
)

JOB_CITY_CHOICE = [
    ("Delhi", "Delhi"),
    ("Pune", "Pune"),
    ("Ranchi", "Ranchi"),
    ("Mumbai", "Mumbai"),
    ("Dhanbad", "Dhanbad"),
    ("Bangalore", "Bangalore"),
]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "dob",
            "gender",
            "locality",
            "city",
            "pin",
            "state",
            "mobile",
            "email",
            "job_city",
            "profile_image",
            "my_file",
        ]
        labels = {
            "name": "Full Name",
            "pin": "PIN Code",
            "mobile": "Mobile Number",
            "dob": "Date of Birth",
        }
        help_texts = {
            "profile_image": "Optional: Upload a profile image",
            "my_file": "Optional: Attach any additional document (PDF, DOCX, etc.)",
        }
