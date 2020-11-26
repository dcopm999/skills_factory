from skills_factory.educations import models


def cource_list(request):
    return {"cource_list": models.Cource.objects.all()}
