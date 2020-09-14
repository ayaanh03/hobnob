from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(label='email')

    phone = forms.IntegerField()

    date_of_birth = forms.DateField()

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = forms.ChoiceField(choices=gender_choice)

    country = forms.CharField(max_length=255)

    state = forms.CharField(max_length=255)

    district = forms.CharField(max_length=255)

    role_choice = (
        ("SOCIAL MEDIA STAR", "SOCIAL MEDIA STAR"),
        ("MOM/DAD INFLUENCER", "MOM/DAD INFLUENCER"),
        ("CAMPUS AMBASSADOR", "CAMPUS AMBASSADOR"),
        ("WORKING PROFESSIONAL", "WORKING PROFESSIONAL"),
    )
    your_role = forms.ChoiceField(choices=role_choice)

