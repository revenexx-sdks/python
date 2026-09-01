from enum import Enum

class ShippingMethodMatrixBasis(Enum):
    WEIGHT = "weight"
    QUANTITY = "quantity"
    ORDER_VALUE = "order_value"
    ATTRIBUTE = "attribute"
