from django.test import TestCase
from listings.models import Seat, Room, Listing, ProductDetail
from django.contrib.auth import get_user_model
from accounts.models import User, Supplier


class TestSeat(TestCase):
    def setUp(self):
        cus_user = User.objects.create_user(
            email='tester@gmail.com',
            username='tester',
            password='1234',
            user_role=2
        )
        supplier = User.objects.create_user(
            email='sup@gmail.com',
            username='sup',
            password='1234',
            user_role=3
        )
        supplier_detail = Supplier.objects.create(
            user = supplier,
            name= 'test supplier',
            phone_number='010-8888-8888',
        )
        product_detail = ProductDetail.objects.create(
            act_type='all',
            long_name_kr='콘센트'
        )

        listing = Listing.objects.create(
            owner=supplier,
            name='test_academy',
            address='Shinchon Korea',
            geo_lat=38.0001,
            geo_lng=19.0021,
            listing_type='acd',
            operational_hours_24=False,
            operational_hours_start=9,
            operational_hours_end=23,
            rent_room=False,
            rent_seat=True,
            rent_seat_total = 0,
            rent_room_total = 0
        )

        seat = Seat.objects.create(
            nth_seat=1,
            extendable=True,
            listing=listing,
            in_use=False,
            in_use_until=None
        )
        seat.__setattr__('detail', product_detail)

    def test_seat_register(self):
        customer = User.objects.filter(email='tester@gmail.com')[0]
        supplier = User.objects.filter(email='sup@gmail.com')[0]
        print(supplier.email)
        listing = Listing.objects.filter(owner__id = supplier.id)[0]
        seat = Seat.objects.filter(listing__id=listing.id)

        print('is_time_available')
        print(seat.is_time_available(60))

        print('get_seat')
        print(seat.get_seat())

        print('is_owner')
        print(seat.is_owner(customer))