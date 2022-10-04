from django import forms

class CreateTodo(forms.Form):
    todo_name = forms.CharField()
    todo_text = forms.CharField(widget=forms.Textarea())