from django import forms
from .models import search_tag

class search_tag_form(forms.ModelForm):
	class Meta:
		model = search_tag
		fields = [
			"tag",
		]