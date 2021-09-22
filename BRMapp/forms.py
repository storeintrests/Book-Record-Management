from django import forms


class NewBookForm(forms.Form):
    title = forms.CharField(label="Name", max_length=100)
    price = forms.FloatField(label="Phone Number")
    author = forms.CharField(label="Email")
    publisher = forms.CharField(label="Position")


class SearchForm(forms.Form):
    title = forms.CharField(label="Name", max_length=100)
