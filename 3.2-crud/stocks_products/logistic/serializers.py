from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        stock_positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for pos in stock_positions:
            StockProduct.objects.create(**pos, stock=stock)

        return stock

    def update(self, instance, validated_data):
        stock_positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for pos in stock_positions:
            product = pos.get('product')
            if product:
                StockProduct.objects.filter(stock=stock, product=product).delete()
                if pos.get('quantity') > 0:
                    StockProduct.objects.create(**pos, stock=stock)

        return stock
