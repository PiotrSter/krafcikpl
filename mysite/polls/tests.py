from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Client, Supplier
from rest_framework import status
from django.utils.http import urlencode
from django import urls

class ClientTests(APITestCase):
    def post_client(self, name, surname, address, phone_number):
        url = reverse(views.ClientList)
        data = {'name':name, 'surname':surname, 'address':address, 'phone_number': phone_number}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_client(self):
        new_client_name = 'Kamil'
        new_client_surname = 'Stoch'
        new_client_address = 'Krucza 23/7'
        new_client_phone_number =  501481772
        response = self.post_client(new_client_name, new_client_surname, new_client_address, new_client_phone_number)
        print("PK {0}".format(Client.object.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Client.object.count() == 1
        assert Client.object.get().name == new_client_name
        assert Client.object.get().surname == new_client_surname
        assert Client.object.get().address == new_client_address
        assert Client.object.get().phone_number == new_client_phone_number

    def test_post_existing_client_name(self):
        url = reverse(views.ClientList.name, views.ClientList.surname, views.ClientList.address,
                      views.ClientList.phone_number)
        new_client_name = 'Duplicate Kamil'
        new_client_surname = 'Duplicate Stoch'
        new_client_address = 'Duplicate Krucza 23/7'
        new_client_phone_number = 501481772
        response_one = self.post_client(new_client_name, new_client_surname, new_client_address,
                                        new_client_phone_number)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_client(new_client_name, new_client_surname, new_client_address,
                                        new_client_phone_number)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_client_by_name(self):
        client_name_one = 'Kamil'
        client_surname_one = 'Stoch'
        client_address_one = 'Krucza 23/7'
        client_phone_number_one = 501481772
        client_name_two = 'Agnieszka'
        client_surname_two = 'Radwańska'
        client_address_two = 'Klonowa 17'
        client_phone_number_two = 503677915
        self.post_client(client_name_one, client_surname_one, client_address_one, client_phone_number_one)
        self.post_client(client_name_two, client_surname_two, client_address_two, client_phone_number_two)
        filter_by_name = {'name': client_name_one}
        url = '{0}?{1}'.format(reverse(views.ClientList.name, views.ClientList.surname, views.ClientList.address,
                      views.ClientList.phone_number), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == client_name_one

    def test_filter_client_by_surname(self):
        client_name_one = 'Kamil'
        client_surname_one = 'Stoch'
        client_address_one = 'Krucza 23/7'
        client_phone_number_one = 501481772
        client_name_two = 'Agnieszka'
        client_surname_two = 'Radwańska'
        client_address_two = 'Klonowa 17'
        client_phone_number_two = 503677915
        self.post_client(client_name_one, client_surname_one, client_address_one, client_phone_number_one)
        self.post_client(client_name_two, client_surname_two, client_address_two, client_phone_number_two)
        filter_by_surname = {'surname': client_surname_one}
        url = '{0}?{1}'.format(reverse(views.ClientList.name, views.ClientList.surname, views.ClientList.address,
                      views.ClientList.phone_number), urlencode(filter_by_surname))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['surname'] == client_surname_one

    def test_filter_client_by_address(self):
        client_name_one = 'Kamil'
        client_surname_one = 'Stoch'
        client_address_one = 'Krucza 23/7'
        client_phone_number_one = 501481772
        client_name_two = 'Agnieszka'
        client_surname_two = 'Radwańska'
        client_address_two = 'Klonowa 17'
        client_phone_number_two = 503677915
        self.post_client(client_name_one, client_surname_one, client_address_one, client_phone_number_one)
        self.post_client(client_name_two, client_surname_two, client_address_two, client_phone_number_two)
        filter_by_address = {'address': client_address_one}
        url = '{0}?{1}'.format(reverse(views.ClientList.name, views.ClientList.surname, views.ClientList.address,
                      views.ClientList.phone_number), urlencode(filter_by_address))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['address'] == client_address_one

    def test_filter_client_by_phone_number(self):
        client_name_one = 'Kamil'
        client_surname_one = 'Stoch'
        client_address_one = 'Krucza 23/7'
        client_phone_number_one = 501481772
        client_name_two = 'Agnieszka'
        client_surname_two = 'Radwańska'
        client_address_two = 'Klonowa 17'
        client_phone_number_two = 503677915
        self.post_client(client_name_one, client_surname_one, client_address_one, client_phone_number_one)
        self.post_client(client_name_two, client_surname_two, client_address_two, client_phone_number_two)
        filter_by_phone_number = {'phone_number': client_phone_number_one}
        url = '{0}?{1}'.format(reverse(views.ClientList.name, views.ClientList.surname, views.ClientList.address,
                      views.ClientList.phone_number), urlencode(filter_by_phone_number))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['phone_number'] == client_phone_number_one

    def test_get_client_collection(self):
        new_client_name = 'Robert'
        new_client_surname = 'Lewandowski'
        new_client_address = 'Szkolna 11/11'
        new_client_phone_number = 504233819
        url = reverse(views.ClientList.name, views.ClientList.surname, views.ClientList.address,
                      views.ClientList.phone_number)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_client_name
        assert response.data['results'][0]['surname'] == new_client_surname
        assert response.data['results'][0]['address'] == new_client_address
        assert response.data['results'][0]['phone_number'] == new_client_phone_number

    def test_update_client(self):
        client_name = 'Kamil'
        client_surname = 'Stoch'
        client_address = 'Krucza 23/7'
        client_phone_number = 501481772
        response = self.post_client(client_name, client_surname, client_address, client_phone_number)
        url = urls.reverse(views.ClientDetail.name, views.ClientDetail.surname, views.ClientDetail.address,
                           views.ClientDetail.phone_number,None,{response.data['pk']})
        updated_client_name = 'Andrzej'
        data = {'name': updated_client_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_client_name

    def test_get_client(self):
        client_name = 'Kamil'
        client_surname = 'Stoch'
        client_address = 'Krucza 23/7'
        client_phone_number = 501481772
        response = self.post_client(client_name, client_surname, client_address, client_phone_number)
        url = urls.reverse(views.ClientDetail.name, views.ClientDetail.surname, views.ClientDetail.address,
                           views.ClientDetail.phone_number,None,{response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == client_name
        assert get_response.data['surname'] == client_surname
        assert get_response.data['address'] == client_address
        assert get_response.data['phone_number'] == client_phone_number

class Supplier(APITestCase):
    def post_supplier(self, name, surname, vechicle):
        url = reverse(views.SupplierList)
        data = {'name':name, 'surname':surname, 'vechicle':vechicle}
        response = self.supplier.post(url, data, format='json')
        return response

    def test_post_and_get_supplier(self):
        new_supplier_name = 'Alicja'
        new_supplier_surname = 'Iksińska'
        new_supplier_vechicle = 'Car'
        response = self.post_client(new_supplier_name, new_supplier_surname, new_supplier_vechicle)
        print("PK {0}".format(Supplier.object.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Supplier.object.count() == 1
        assert Supplier.object.get().name == new_supplier_name
        assert Supplier.object.get().surname == new_supplier_surname
        assert Supplier.object.get().vechicle == new_supplier_vechicle

    def test_post_existing_supplier_name(self):
        url = reverse(views.SupplierList.name, views.SupplierList.surname, views.SupplierList.vechicle)
        new_supplier_name = 'Alicja'
        new_supplier_surname = 'Iksińska'
        new_supplier_vechicle = 'Car'
        response_one = self.post_client(new_supplier_name, new_supplier_surname, new_supplier_vechicle)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_client(new_supplier_name, new_supplier_surname, new_supplier_vechicle)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_supplier_by_name(self):
        supplier_name_one = 'Alicja'
        supplier_surname_one = 'Iksińska'
        supplier_vechicle_one = 'Car'
        supplier_name_two = 'Patryk'
        supplier_surname_two = 'Jop'
        supplier_vechicle_two = 'Bike'
        self.post_client(supplier_name_one, supplier_surname_one, supplier_vechicle_one)
        self.post_client(supplier_name_two, supplier_surname_two, supplier_vechicle_two)
        filter_by_name = {'name': supplier_name_one}
        url = '{0}?{1}'.format(reverse(views.SupplierList.name, views.SupplierList.surname, views.SupplierList.vechicle)
                               , urlencode(filter_by_name))
        print(url)
        response = self.supplier.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == supplier_name_one

    def test_filter_supplier_by_surname(self):
        supplier_name_one = 'Alicja'
        supplier_surname_one = 'Iksińska'
        supplier_vechicle_one = 'Car'
        supplier_name_two = 'Patryk'
        supplier_surname_two = 'Jop'
        supplier_vechicle_two = 'Bike'
        self.post_client(supplier_name_one, supplier_surname_one, supplier_vechicle_one)
        self.post_client(supplier_name_two, supplier_surname_two, supplier_vechicle_two)
        filter_by_surname = {'name': supplier_name_one}
        url = '{0}?{1}'.format(reverse(views.SupplierList.name, views.SupplierList.surname, views.SupplierList.vechicle)
                               , urlencode(filter_by_surname))
        print(url)
        response = self.supplier.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['surname'] == supplier_surname_one

    def test_filter_supplier_by_vechicle(self):
        supplier_name_one = 'Alicja'
        supplier_surname_one = 'Iksińska'
        supplier_vechicle_one = 'Car'
        supplier_name_two = 'Patryk'
        supplier_surname_two = 'Jop'
        supplier_vechicle_two = 'Bike'
        self.post_client(supplier_name_one, supplier_surname_one, supplier_vechicle_one)
        self.post_client(supplier_name_two, supplier_surname_two, supplier_vechicle_two)
        filter_by_vechicle = {'name': supplier_name_one}
        url = '{0}?{1}'.format(reverse(views.SupplierList.name, views.SupplierList.surname, views.SupplierList.vechicle)
                               , urlencode(filter_by_vechicle))
        print(url)
        response = self.supplier.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['surname'] == supplier_vechicle_one

    def test_get_supplier_collection(self):
        new_supplier_name = 'Julia'
        new_supplier_surname = 'Zalewska'
        new_supplier_vechicle = 'Bike'
        url = reverse(views.SupplierList.name, views.SupplierList.surname, views.SupplierList.vechicle)
        response = self.supplier.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_supplier_name
        assert response.data['results'][0]['surname'] == new_supplier_surname
        assert response.data['results'][0]['vechicle'] == new_supplier_vechicle

    def test_update_supplier(self):
        supplier_name = 'Alicja'
        supplier_surname = 'Iksińska'
        supplier_vechicle = 'Car'
        response = self.post_client(supplier_name, supplier_surname, supplier_vechicle)
        url = urls.reverse(views.SupplierDetail.name, views.SupplierDetail.surname, views.SupplierDetail.vechicle,
                           None,{response.data['pk']})
        updated_supplier_name = 'Karolina'
        data = {'name': updated_supplier_name}
        patch_response = self.supplier.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_supplier_name

    def test_get_supplier(self):
        supplier_name = 'Alicja'
        supplier_surname = 'Iksińska'
        supplier_vechicle = 'Car'
        response = self.post_client(supplier_name, supplier_surname, supplier_vechicle)
        url = urls.reverse(views.SupplierDetail.name, views.SupplierDetail.surname, views.SupplierDetail.vechicle,
                           None,{response.data['pk']})
        get_response = self.supplier.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == supplier_name
        assert get_response.data['surname'] == supplier_surname
        assert get_response.data['vechicle'] == supplier_vechicle