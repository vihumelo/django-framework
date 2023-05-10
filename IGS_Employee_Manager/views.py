from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import StaffMember, Department
import json

@method_decorator(csrf_exempt, name='dispatch')
### Class StaffMember to receive requests (get, post and delete)
class StaffMemberView(View):
    def get(self, request):
        members = StaffMember.objects.all()
        data = [member.to_dict() for member in members]
        return JsonResponse(data, safe=False)

    def post(self, request):

        data = json.loads(request.body.decode('utf-8'))
        department = get_object_or_404(Department, name=data['department'])
        member = StaffMember(name=data['name'], email=data['email'], department=department)
        member.save()
        data = {'message': 'Successful!'}
        return JsonResponse(data)

    def delete(self, request):
        name = request.GET.get('name', None)
        if name is None:
            data = {'message': 'No name sent!'}
            return JsonResponse(data, status=400)

        members = StaffMember.objects.filter(name=name)
        members.delete()
        data = {'message': f'Staff member(s) with name(s) "{name}" have been deleted successfully.'}
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
### Class Department to receive requests (get, post and delete)
class DepartmentView(View):
    def get(self, request):
        departments = Department.objects.all()
        data = [departamento.to_dict() for departamento in departments]
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        department = Department(name=data['name'])
        department.save()
        data = {'message': 'Successful!'}
        return JsonResponse(data)

    def delete(self, request):
        name = request.GET.get('name', None)
        if name is None:
            data = {'message': 'No name sent!'}
            return JsonResponse(data, status=400)
        department = Department.objects.filter(name=name)
        department.delete()
        data = {'message': f'Department(s) with name(s) "{name}" have been deleted successfully.'}
        return JsonResponse(data)

### Function to connect to the public site
def public_list(request):
	members = StaffMember.objects.all()
	return render(request, 'public.html', {'members': members})