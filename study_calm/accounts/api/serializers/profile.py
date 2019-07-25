from rest_framework import serializers

class UserProfile(serializers.ModelSerializer):
    pass

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'accounts.User'
        fields = [
            'user',
            'name',
            'phone_number',
            'registered_at',
            'last_login',
            'last_login_ip'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

class SupplierProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'accounts.User'
        fields = [
            'email',
            'user_role',
            'username',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
