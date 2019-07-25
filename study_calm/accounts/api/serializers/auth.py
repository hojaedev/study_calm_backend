from rest_framework import serializers
from accounts.models import User
from django.core.validators import ValidationError


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'user_role',
            'acc_type',
            'token',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

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

    # id = serializers.UUIDField(read_only=True, default=uuid.uuid4)
    acc_type = serializers.CharField(max_length=3, required=True, allow_blank=False)
    user_role = serializers.IntegerField(required=True)
    email = serializers.EmailField()
    token = serializers.CharField(read_only=True, required=False)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        acc_type = data.get('acc_type', None)
        user_role = data.get('user_role', None)

        if not email or not password:
            raise ValidationError('A email field and password field is required to login.')
        if not acc_type or not user_role:
            raise ValidationError('User role and Account type must be specified')

        user = User.objects.filter(email=email).distinct()
        if user and user.count() == 1:
            user = user.first()
        else:
            raise ValidationError('The email is not valid (not registered)')
        if user:
            if not user.check_password(password):
                raise ValidationError('Incorrect password/email pair please try again')
            if not (user.acc_type == acc_type or user.user_role == user_role):
                raise ValidationError('Incorrect account type and user role')

        data['token'] = 'SOME RANDOM TOKEN'

        return data


class UserCreateSerializer(serializers.ModelSerializer):
    # (1, 'ADMIN'),
    # (2, 'CUSTOMER'),
    # (3, 'SUPPLIER'),
    class Meta:
        model = User
        fields = [
            'email',
            'user_role',
            'username',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, data):
        user = User.objects.create_user(
            data['email'],
            data['username'],
            data['password'],
            data['user_role']
        )
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'acc_type',
            'user_role'
            'is_active',
            'token'
        ]

class UserDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'is_active',
        ]