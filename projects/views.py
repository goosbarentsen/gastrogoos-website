from django.shortcuts import render
from projects.models import Project
#,ProjectImage
from django.db.models import Q

def project_index(request):
#    projects = Project.objects.all()
#    context = {
#        'projects': projects
#    }
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    projects = get_project_queryset(query)   
    context['projects'] = projects
    
    return render(request, 'project_index.html', context)



def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    imagelist = project.images.all()
    context = {
        'project': project,
        'imagelist' : imagelist
    }
    return render(request, 'project_detail.html', context)

def get_project_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        recipes = Project.objects.filter(
                Q(titel__icontains=q) | Q(ingredient__icontains=q)
                ).distinct()
        for recipe in recipes:
            queryset.append(recipe)
    
    return list(set(queryset))

