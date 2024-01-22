from django.forms import formset_factory
from topic_form.forms import ArticleForm


def run():
    ArticleFormSet = formset_factory(ArticleForm, extra=2, max_num=1)
    formset = ArticleFormSet()
    print(formset)
    # for form in formset:
    #     print(form)
