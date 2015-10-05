from django import forms
from .models import *
class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Photos', 'Category', 'Title', 'BidStart','Timer']

class BidPostForm(forms.ModelForm):
    class Meta:
        model = Bids
        fields = ['BidPrice']

class SearchProductForm(forms.Form):
    name = forms.CharField();

class CategorySearchForm(forms.ModelForm):
   class Meta:
      model = Product
      fields = ['Category']

