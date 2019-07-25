from accounts.models import User
from listings.models import Listing, Seat

user = User.objects.filter(email='johnyoon95@gmail.com')[0]
seat = Seat.objects.filter(id='74686c58-7002-4988-acb7-899fb4aa8536')[0]
listing = Listing.objects.filter(name='일번 학원')[0]
seat.select_seat(user, 120)


# manage.py shell <<EOF\ execfile('test.py') \EOF