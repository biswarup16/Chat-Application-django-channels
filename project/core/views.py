from django.shortcuts import render

# Create your views here.
def index(request, group_name):
  print("Group Name...", group_name)
  return render(request, 'index.html', {'groupname':group_name})

def group(request):
  return render(request,'group.html')