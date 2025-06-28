
class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for Address model
    """
    full_address = serializers.SerializerMethodField()
    short_address = serializers.SerializerMethodField()
    
    class Meta:
        model = Address
        fields = [
            'id', 'street_address', 'apartment_unit', 'city', 
            'state_province', 'postal_code', 'country', 
            'address_type', 'is_primary', 'full_address', 
            'short_address', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'id']

    def get_full_address(self, obj):
        return obj.get_full_address()

    def get_short_address(self, obj):
        return obj.get_short_address()

    def validate(self, data):
        """Custom validation for address"""
        if not data.get('street_address'):
            raise serializers.ValidationError("Street address is required.")
        if not data.get('city'):
            raise serializers.ValidationError("City is required.")
        if not data.get('postal_code'):
            raise serializers.ValidationError("Postal code is required.")
        return data


class AddressCreateSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for creating addresses
    """
    class Meta:
        model = Address
        fields = [
            'street_address', 'apartment_unit', 'city', 
            'state_province', 'postal_code', 'country', 
            'address_type', 'is_primary'
        ]

