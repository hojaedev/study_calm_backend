from rest_framework import serializers
import uuid

class LoginSerializer(serializers.Serializer):
    ROLE_CHOICES = (
        (1, 'ADMIN'),
        (2, 'CUSTOMER'),
        (3, 'SUPPLIER'),
        (4, 'to_be_added_1'),
        (5, 'to_be_added_2'),
        (6, 'to_be_added_3'),
        (7, 'to_be_added_4'),
    )
    ACCOUNT_TYPE = (
        (1, 'Google'),
        (2, 'Facebook'),
        (3, 'Native'),
    )


    id = serializers.UUIDField(read_only=True, default=uuid.uuid4)
    acc_type = serializers.CharField(max_length=3, default='nat', required=True, allow_blank=False)
    user_role = serializers.PositiveSmallIntegerField(required=True, allow_blank=False, )

    email = serializers.EmailField(unique=True, verbose_name='Email')

    date_joined = serializers.DateTimeField(auto_now_add=True, verbose_name='Date of Registration')

    registered_at = serializers.DateTimeField(auto_now=False, auto_now_add=True)
    last_login = serializers.DateTimeField(auto_now=True, auto_now_add=False)
    last_login_ip = serializers.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)
    is_active = serializers.BooleanField(default=True, verbose_name='Active Activity Status')
    is_staff = serializers.BooleanField(default=True, verbose_name='Staff Status')

    def create(self, validated_data):
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def update(self, instance, validated_data):
        pass


