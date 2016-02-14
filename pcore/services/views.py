from django.views.generic import ListView
from .models import Countries, Cities, Regions, Employees, Clients, Stores, Tags, Categories, Departments, Sensors, \
    Brands, PromotionsTypes, PromotionsFilters, PromotionsLoyalties, PromotionsSpecials, Promotions, \
    PromotionsImpacts, CustomUser
from .serializers import CountriesSerializer, CitiesSerializer, RegionsSerializer, EmployeeSerializer, \
    ClientsSerializer, StoresSerializer, TagsSerializer, CategoriesSerializer, DepartmentsSerializer, \
    SensorsSerializer, BrandsSerializer, PromotionsTypesSerializer, PromotionsFiltersSerializer, \
    PromotionsLoyaltiesSerializer, PromotionsSpecialsSerializer, PromotionsSerializer, \
    PromotionsImpactsSerializer, CustomUserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
import random
import string
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


@api_view(['POST'])
def auth(request):
    try:
        if request.method == 'POST':
            username = request.data.get('username')
            password = request.data.get('password')
            data = {'error': True}
            try:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        data['user'] = {'id': user.id, 'username': user.username}
                        data['error'] = False
            except CustomUser.DoesNotExist as e:
                print e
                data['error'] = True

            return Response(data=data, status=status.HTTP_200_OK)

    except Exception as e:
        print e


@api_view(['GET', 'POST'])
def custom_user(request, user_id):
    try:
        if request.method == "GET":
            serializer = CustomUserSerializer(CustomUser.objects.get(id=user_id))
            return Response(serializer.data)

        elif request.method == 'POST':
            username = request.data.get('username')
            email = request.data.get('email')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            gender = request.data.get('gender')
            birthday = request.data.get('birthday')
            lang = request.data.get('lang')
            checkpass = bool(request.data.get('checkpass'))
            password = request.data.get('password')

            usr = CustomUser.objects.get(id=user_id)
            usr.username = username
            usr.email = email
            usr.first_name = first_name
            usr.last_name = last_name
            usr.gender = gender
            usr.birthday = birthday
            usr.lang = lang
            if checkpass:
                usr.set_password(password)
            usr.save()

            return Response(status=status.HTTP_200_OK)

    except Exception as e:
        print e
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


""""
    My zone
"""""


@api_view(['POST'])
def set_password(request, id):
    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(id=id)
            new_password = request.data.get('pass')
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except CustomUser.DoesNotExist:
            return HttpResponse(status=404)


@api_view(['GET', 'POST'])
def client(request, client_id):
    try:
        if request.method == "GET":
            serializer = ClientsSerializer(Clients.objects.get(id=client_id))
            return Response(serializer.data)

        elif request.method == 'POST':
            client_name = request.data.get('client_name')
            web_site = request.data.get('web_site')
            telephone = request.data.get('telephone')
            description = request.data.get('description')
            logo_url = request.data.get('logo_url')
            background_color = request.data.get('background_color')
            foreground_color = request.data.get('foreground_color')
            background_img = request.data.get('background_img')
            ttf_font = request.data.get('ttf_font')
            country = request.data.get('country')
            city = request.data.get('city')
            facebook_fan_page = request.data.get('facebook_fan_page')
            twitter_account = request.data.get('twitter_account')
            gplus_id = request.data.get('gplus_id')
            language = request.data.get('language')
            timezone = request.data.get('timezone')


            cli = Clients.objects.get(id=client_id)
            cli.client_name = client_name
            cli.web_site = web_site
            cli.telephone = telephone
            cli.description = description
            cli.logo_url = logo_url
            cli.background_color = background_color
            cli.foreground_color = foreground_color
            cli.background_img = background_img
            cli.background_img = background_img
            cli.ttf_font = ttf_font
            cli.country = country
            cli.city = city
            cli.facebook_fan_page = facebook_fan_page
            cli.twitter_account = twitter_account
            cli.gplus_id = gplus_id
            cli.twitter_account = twitter_account
            cli.language = language
            cli.timezone = timezone
            cli.save()
            return Response(status=status.HTTP_200_OK)

    except Exception as e:
        print e
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)






@api_view(['POST'])
def create_client_admin(request):
    try:
        if request.method == 'POST':
            new_name = request.data.get('name')
            new_last_name = request.data.get('lastname')
            new_username = request.data.get('username')
            new_email = request.data.get('email')
            new_password = request.data.get('password')
            new_client_name = request.data.get('client_name')
            new_telephone = request.data.get('telephone')


            # if CustomUser.objects.filter(email=new_email).count() != 0:
            #    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": "duplicate_email"})
            # if CustomUser.objects.filter(username=new_username).count() != 0:
            #    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": "duplicate_username"})

            confirmation_code = ''.join(
                random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(66))

            e = Clients.objects.create(first_name=new_name, last_name=new_last_name, username=new_username,
                                       email=new_email, is_client_admin=True, is_active=True, telephone=new_telephone,
                                       client_name=new_client_name)

            e.set_password(new_password)
            e.save()
            """
            confirmation_link = "/registration/admin_user/confirm/" + e.username + "/" + e.confirmation_code

            about_text = "Activate your Bizwi account."
            message_welcome = "Hi {{ client }}!"
            message_text = "You have registered to use Bizwi. Confirm your email to start using our service. Go to {{ link }}"

            message_welcome = message_welcome.replace("{{ client }}", str(e.get_short_name()))
            message_text = message_text.replace("{{ link }}", str(confirmation_link))
            """
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
            return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        print e
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def stores(request, client, id_local=None):
    try:
        if request.method == "GET":
            if id_local:
                serializer = StoresSerializer(Stores.objects.get(id=id_local))
            else:
                serializer = StoresSerializer(Stores.objects.filter(client_id=client), many=True)

            return Response(serializer.data)

        elif request.method == 'POST':
            name = request.data.get('name')
            telephone = request.data.get('telephone')
            web_site = request.data.get('web_site')
            description = request.data.get('name')
            country = request.data.get('country')
            city = request.data.get('city')
            region = request.data.get('region')
            address = request.data.get('address')
            logo_url = request.data.get('logo_url')
            background_color = request.data.get('background_color')
            foreground_color = request.data.get('foreground_color')
            background_img = request.data.get('background_img')
            ttf_font = request.data.get('ttf_font')

            print name

            if id_local:
                loc = Stores.objects.get(id=id_local)
                loc.name = name
                loc.country = country
                loc.city = city
                loc.address = address
                loc.region = region
                loc.logo_url = logo_url
                loc.background_color = background_color
                loc.foreground_color = foreground_color
                loc.ttf_font = ttf_font
                loc.save()
            else:
                loc = Stores(
                    client_id=client,
                    store_name=name,
                    telephone=telephone,
                    web_site=web_site,
                    description=description,
                    country=country,
                    city=city,
                    region=region,
                    address=address,
                    logo_url=logo_url,
                    background_color=background_color,
                    foreground_color=foreground_color,
                    background_img=background_img,
                    ttf_font=ttf_font,
                )
                loc.save()
            return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_employee_context(request, id):
    try:
        if request.method == 'GET':
            client = Clients.objects.get(id=id)

            language = client.language
            customer = client.customer

            if customer:
                id_customer = customer.id
                customer_name = customer.name
                time_zone = customer.timezone
            else:
                id_customer = ""
                customer_name = ""
                time_zone = ""

            data = {
                "client": hh,
                "full_name": full_name,
                "id_customer": id_customer,
                "customer_name": customer_name,
                "language": language,
                "timezone": time_zone,
                "id_location": "",
                "is_customer_admin": is_customer_admin,
            }

            return Response(data)
    except Exception as e:
        print e
        return HttpResponse(status=404)


@api_view(['GET', 'POST'])
def employee(request, id=None):
    try:
        employee = Employees.objects.get(id=id)
    except Employees.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        data = serializer.data
        return Response(data)
    elif request.method == 'POST':

        email = request.DATA.get('email')

        try:
            employee.email = email
            employee.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print e
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def employees_list(request, client_id, id_employee=None):
    try:
        if request.method == "GET":
                serializer = EmployeeSerializer(Employees.objects.filter(client_id=client_id))
                return Response(serializer.data)

        elif request.method == 'POST':
            username = request.DATA.get('username')
            email = request.DATA.get('email')
            first_name = request.DATA.get('first_name')
            phone = request.DATA.get('phone')
            last_name = request.DATA.get('last_name')
            language = request.DATA.get('language')
            checkpass = bool(request.DATA.get('checkpass'))
            password = request.DATA.get('password')
            location = Location.objects.get(id=request.DATA.get('location'))

            if id_employee:
                emp = Employee.objects.get(id=id_employee)
                emp.username = username
                emp.email = email
                emp.first_name = first_name
                emp.last_name = last_name
                emp.language = language
                emp.location = location
                emp.phone = phone
                if checkpass:
                    emp.set_password(password)
                emp.save()
            else:
                emp = Employee(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    language=language,
                    location=location,
                    phone = phone
                )
                emp.set_password(password)
                emp.save()
            return Response(status=status.HTTP_200_OK)

    except Exception as e:
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
