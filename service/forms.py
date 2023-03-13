from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['full_name', 'phone_number', 'purchase_price', 'credit_term']

    commission = forms.DecimalField(required=False, min_value=500, max_value=100000, decimal_places=2)

    def clean(self):
        cleaned_data = super().clean()
        purchase_price = cleaned_data.get('purchase_price')
        credit_term = cleaned_data.get('credit_term')
        commission = cleaned_data.get('commission')
        if not commission:
            commission = 0
        if purchase_price * 0.75 + purchase_price * commission / 100 > 60000:
            raise forms.ValidationError('Кредитная часть не должна превышать 60 тысяч рублей')
        if credit_term != 4 and credit_term != 6:
            raise forms.ValidationError('Выберите срок рассрочки')
        if credit_term == 6 and commission:
            raise forms.ValidationError('Выберите комиссию за 6 месяцев рассрочки')
        return cleaned_data
