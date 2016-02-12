from .models import Countries, Cities, Regions, Employees, Clients, Stores, Tags, Categories, Departments, Sensors, \
    Brands, PromotionsTypes, PromotionsFilters, PromotionsLoyalties, PromotionsSpecials, Promotions, PromotionsImpacts
from .serializers import CountriesSerializer, CitiesSerializer, RegionsSerializer, EmployeeSerializer, ClientsSerializer, StoresSerializer, TagsSerializer, CategoriesSerializer, DepartmentsSerializer, SensorsSerializer, BrandsSerializer, PromotionsTypesSerializer, PromotionsFiltersSerializer, PromotionsLoyaltiesSerializer, PromotionsSpecialsSerializer, PromotionsSerializer, PromotionsImpactsSerializer
from rest_framework import generics
import random
import string

from rest_framework.response import Response
from rest_framework import status


def create_client_admin(request):
    try:
        if request.method == 'POST':
            new_name = request.DATA.get('name')
            new_last_name = request.DATA.get('lastname')
            new_username = request.DATA.get('username')
            new_email = request.DATA.get('email')
            new_password = request.DATA.get('password')

            #if CustomUser.objects.filter(email=new_email).count() != 0:
            #    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": "duplicate_email"})
            #if CustomUser.objects.filter(username=new_username).count() != 0:
            #    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": "duplicate_username"})

            confirmation_code = ''.join(
                random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(66))

            e = Clients.objects.create(first_name=new_name, last_name=new_last_name, username=new_username,
                                       email=new_email, is_customer_admin=True, is_active=True,
                                       confirmation_code=confirmation_code,)
            e.set_password(new_password)
            e.save()

            confirmation_link = "/registration/admin_user/confirm/" + e.username + "/" + e.confirmation_code

            about_text = "Activate your Bizwi account."
            message_welcome = "Hi {{ client }}!"
            message_text = "You have registered to use Bizwi. Confirm your email to start using our service. Go to {{ link }}"

            message_welcome = message_welcome.replace("{{ client }}", str(e.get_short_name()))
            message_text = message_text.replace("{{ link }}", str(confirmation_link))

            """
            mail = get_template('mail.html')
            d = Context({
                'message_welcome': message_welcome,
                'message_text': message_text,
                'uppercolor': '#70bbd9',
                'lowercolor': '#ee4c50',
                # 'logo': msg.sender.img_url,
                'title': about_text,
                'year': datetime.now().year,
                'customer': "Bizwi"
            })
            """

            #content_text = mail.render(d)

            #send_email(source=EMAIL_INFO,
            #           to=e.email,
            #           about=about_text,
            #           content=content_text,
            #           message_format='html')

            return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        print e
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Countries,
class CountriesList(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


# Cities,
class CitiesList(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


# Regions,
class RegionsList(generics.ListCreateAPIView):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer


# Employees,
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


# Clients,
class ClientsList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


# Stores,
class StoresList(generics.ListCreateAPIView):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer


# Tags,
class TagsList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


# Categories,
class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


# Departments,
class DepartmentsList(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


# Sensors,
class SensorsList(generics.ListCreateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


# Brands,
class BrandsList(generics.ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


# PromotionsTypes,
class PromotionsTypesList(generics.ListCreateAPIView):
    queryset = PromotionsTypes.objects.all()
    serializer_class = PromotionsTypesSerializer


class PromotionTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromotionsTypes.objects.all()
    serializer_class = PromotionsTypesSerializer

# PromotionsFilters,
class PromotionsFiltersList(generics.ListCreateAPIView):
    queryset = PromotionsFilters.objects.all()
    serializer_class = PromotionsFiltersSerializer


class PromotionFilterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromotionsFilters.objects.all()
    serializer_class = PromotionsFiltersSerializer

# PromotionsLoyalties,
class PromotionsLoyaltiesList(generics.ListCreateAPIView):
    queryset = PromotionsLoyalties.objects.all()
    serializer_class = PromotionsLoyaltiesSerializer


class PromotionLoyaltyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromotionsLoyalties.objects.all()
    serializer_class = PromotionsLoyaltiesSerializer

# PromotionsSpecials,
class PromotionsSpecialsList(generics.ListCreateAPIView):
    queryset = PromotionsSpecials.objects.all()
    serializer_class = PromotionsSpecialsSerializer


class PromotionSpecialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromotionsSpecials.objects.all()
    serializer_class = PromotionsSpecialsSerializer

# Promotions,
class PromotionsList(generics.ListCreateAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer


class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer

# PromotionsImpacts
class PromotionsImpactsList(generics.ListCreateAPIView):
    queryset = PromotionsImpacts.objects.all()
    serializer_class = PromotionsImpactsSerializer


class PromotionImpactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromotionsImpacts.objects.all()
    serializer_class = PromotionsImpactsSerializer