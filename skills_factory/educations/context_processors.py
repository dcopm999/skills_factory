from skills_factory.educations import models


def cource_list(request):
    return {"cource_list": models.Cource.objects.all()}


def category_list(request):
    return {"category_list": models.Category.objects.all()}
