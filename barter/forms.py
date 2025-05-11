from django import forms
from barter.models import Ad, ExchangeProposal

# def id_dec(old_init):
#     def new_init(self, user_id):
#         old_init()

class EditAdForm(forms.ModelForm):

    cat = forms.ChoiceField(label="Category", choices=((0, 'стул'), (1, 'стол')))
    cond = forms.ChoiceField(label="Condition", choices=((0, 'норм'), (1, 'увы')))
    class Meta:
        model = Ad
        exclude = ('user', 'category', 'condition', )

    def __init__(self, ad_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ad = Ad.objects.get(id=ad_id)
        #self.fields['title'].initial = ad.title


class FilterForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ('user', 'image_url', 'created_at', )

    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    category = forms.ChoiceField(required=False, choices=((None, '----'), (0, 'стул'), (1, 'стол')))
    condition = forms.ChoiceField(required=False, choices=((None, '----'), (0, 'норм'), (1, 'увы')))



class NewAdForm(forms.ModelForm):

    category = forms.ChoiceField(label="Category", choices=((0, 'стул'), (1, 'стол')))
    condition = forms.ChoiceField(label="Condition", choices=((0, 'норм'), (1, 'увы')))

    class Meta:
        model = Ad
        exclude = ('user', 'category', 'condition', )



class OfferBarter(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ["ad_sender", "ad_receiver", "comment"]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)                                   # Обращаемся к конструктору суперкласса
        self.fields['ad_sender'].queryset = Ad.objects.filter(user=user)    # Выводим объявления только текущего пользователя
        self.fields['ad_receiver'].queryset = Ad.objects.exclude(user=user)
