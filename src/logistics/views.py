from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Package, Carrier, Client
from .form import PackageForm
import random
from .serializers import PackageSerializer


class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response("OK", status=status.HTTP_200_OK)


class ClientPackagesView(View):
    template_name = 'client_packages.html'

    def get(self, request, client_id):
        packages = Package.objects.filter(client_id=client_id)
        client = Client.objects.get(pk=client_id)
        return render(request, self.template_name, {'packages': packages, 'client': client})

class CarrierPackagesView(View):
    template_name = 'carrier_packages.html'

    def get(self, request, carrier_id):
        packages = Package.objects.filter(carrier_id=carrier_id)
        carrier = Carrier.objects.get(pk=carrier_id)
        return render(request, self.template_name, {'packages': packages, 'carrier': carrier})


class CreatePackageView(View):
    template_name = 'create_package.html'

    def get(self, request):
        form = PackageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save()
            return redirect('package_details', pk=package.pk)
        return render(request, self.template_name, {'form': form})

class PackageDetailsView(View):
    template_name = 'package_details.html'

    def get(self, request, pk):
        package = Package.objects.get(pk=pk)
        return render(request, self.template_name, {'package': package})

class PackageListView(View):
    template_name = 'package_list.html'

    def get(self, request):
        packages = Package.objects.all()
        return render(request, self.template_name, {'packages': packages})

class EditPackageView(View):
    template_name = 'edit_package.html'

    def get(self, request, pk):
        package = get_object_or_404(Package, pk=pk)
        form = PackageForm(instance=package)
        return render(request, self.template_name, {'form': form, 'package': package})

    def post(self, request, pk):
        package = get_object_or_404(Package, pk=pk)
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            package = form.save()
            return redirect('package_details', pk=package.pk)
        return render(request, self.template_name, {'form': form, 'package': package})


class DeletePackageView(View):
    template_name = 'delete_package.html'

    def get(self, request, pk):
        package = get_object_or_404(Package, pk=pk)
        return render(request, self.template_name, {'package': package})

    def post(self, request, pk):
        package = get_object_or_404(Package, pk=pk)
        package.delete()
        return redirect('package_list')

class AssignCarrierView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            package_id = request.data['package_id']
            package = Package.objects.get(pk=package_id)
            carriers = Carrier.objects.all()

            if carriers.exists():
                random_carrier = random.choice(carriers)
                package.carrier = random_carrier
                package.save()

                serializer = PackageSerializer(package)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No carriers available.'}, status=status.HTTP_404_NOT_FOUND)
        except Package.DoesNotExist:
            return Response({'error': 'Package not found.'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({'error': 'Missing package_id in request data.'}, status=status.HTTP_400_BAD_REQUEST)