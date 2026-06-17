import json
from ..models.base_model import AppwriteModel
from ..enums.runtime import Runtime
from ..enums.scopes import Scopes
from ..enums.runtimes import Runtimes
from ..enums.use_cases import UseCases
from ..enums.range import Range
from ..enums.type import Type
from ..enums.method import Method
from ..enums.code import Code
from ..enums.theme import Theme
from ..enums.timezone import Timezone
from ..enums.permissions import Permissions
from ..enums.output import Output
from ..enums.cart_io_direction import CartIoDirection
from ..enums.cart_io_apply_mode import CartIoApplyMode
from ..enums.cart_io_entity import CartIoEntity
from ..enums.cart_io_format import CartIoFormat
from ..enums.cart_item_type import CartItemType
from ..enums.cart_export_format import CartExportFormat
from ..enums.channel_status import ChannelStatus
from ..enums.channel_type import ChannelType
from ..enums.address_type import AddressType
from ..enums.contact_role import ContactRole
from ..enums.contact_status import ContactStatus
from ..enums.organization_status import OrganizationStatus
from ..enums.location_type import LocationType
from ..enums.market_status import MarketStatus
from ..enums.priority import Priority
from ..enums.order_comment_visibility import OrderCommentVisibility
from ..enums.order_payment_status import OrderPaymentStatus
from ..enums.page_status import PageStatus
from ..enums.payment_fee_type import PaymentFeeType
from ..enums.payment_method_kind import PaymentMethodKind
from ..enums.price_list_status import PriceListStatus
from ..enums.price_entry_type import PriceEntryType
from ..enums.collection import Collection
from ..enums.shipping_method_matrix_basis import ShippingMethodMatrixBasis
from ..enums.shipping_method_pricing_type import ShippingMethodPricingType
from ..enums.build_runtime import BuildRuntime
from ..enums.framework import Framework
from ..enums.adapter import Adapter
from ..enums.visibility import Visibility
from ..enums.order_item_type import OrderItemType
from ..enums.store_asset_request_visibility import StoreAssetRequestVisibility
from ..enums.attribute_boolean_status import AttributeBooleanStatus
from ..enums.attribute_datetime_status import AttributeDatetimeStatus
from ..enums.attribute_email_status import AttributeEmailStatus
from ..enums.attribute_enum_status import AttributeEnumStatus
from ..enums.attribute_float_status import AttributeFloatStatus
from ..enums.attribute_integer_status import AttributeIntegerStatus
from ..enums.attribute_ip_status import AttributeIpStatus
from ..enums.attribute_line_status import AttributeLineStatus
from ..enums.attribute_longtext_status import AttributeLongtextStatus
from ..enums.attribute_mediumtext_status import AttributeMediumtextStatus
from ..enums.attribute_point_status import AttributePointStatus
from ..enums.attribute_polygon_status import AttributePolygonStatus
from ..enums.attribute_relationship_status import AttributeRelationshipStatus
from ..enums.attribute_string_status import AttributeStringStatus
from ..enums.attribute_text_status import AttributeTextStatus
from ..enums.attribute_url_status import AttributeUrlStatus
from ..enums.attribute_varchar_status import AttributeVarcharStatus
from ..enums.column_boolean_status import ColumnBooleanStatus
from ..enums.column_datetime_status import ColumnDatetimeStatus
from ..enums.column_email_status import ColumnEmailStatus
from ..enums.column_enum_status import ColumnEnumStatus
from ..enums.column_float_status import ColumnFloatStatus
from ..enums.column_integer_status import ColumnIntegerStatus
from ..enums.column_ip_status import ColumnIpStatus
from ..enums.column_line_status import ColumnLineStatus
from ..enums.column_longtext_status import ColumnLongtextStatus
from ..enums.column_mediumtext_status import ColumnMediumtextStatus
from ..enums.column_point_status import ColumnPointStatus
from ..enums.column_polygon_status import ColumnPolygonStatus
from ..enums.column_relationship_status import ColumnRelationshipStatus
from ..enums.column_string_status import ColumnStringStatus
from ..enums.column_text_status import ColumnTextStatus
from ..enums.column_url_status import ColumnUrlStatus
from ..enums.column_varchar_status import ColumnVarcharStatus
from ..enums.database_type import DatabaseType
from ..enums.deployment_status import DeploymentStatus
from ..enums.execution_status import ExecutionStatus
from ..enums.execution_trigger import ExecutionTrigger
from ..enums.health_antivirus_status import HealthAntivirusStatus
from ..enums.health_status_status import HealthStatusStatus
from ..enums.index_status import IndexStatus
from ..enums.message_status import MessageStatus

class ValueClassEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, AppwriteModel):
            return o.to_dict()

        if isinstance(o, Runtime):
            return o.value

        if isinstance(o, Scopes):
            return o.value

        if isinstance(o, Runtimes):
            return o.value

        if isinstance(o, UseCases):
            return o.value

        if isinstance(o, Range):
            return o.value

        if isinstance(o, Type):
            return o.value

        if isinstance(o, Method):
            return o.value

        if isinstance(o, Code):
            return o.value

        if isinstance(o, Theme):
            return o.value

        if isinstance(o, Timezone):
            return o.value

        if isinstance(o, Permissions):
            return o.value

        if isinstance(o, Output):
            return o.value

        if isinstance(o, CartIoDirection):
            return o.value

        if isinstance(o, CartIoApplyMode):
            return o.value

        if isinstance(o, CartIoEntity):
            return o.value

        if isinstance(o, CartIoFormat):
            return o.value

        if isinstance(o, CartItemType):
            return o.value

        if isinstance(o, CartExportFormat):
            return o.value

        if isinstance(o, ChannelStatus):
            return o.value

        if isinstance(o, ChannelType):
            return o.value

        if isinstance(o, AddressType):
            return o.value

        if isinstance(o, ContactRole):
            return o.value

        if isinstance(o, ContactStatus):
            return o.value

        if isinstance(o, OrganizationStatus):
            return o.value

        if isinstance(o, LocationType):
            return o.value

        if isinstance(o, MarketStatus):
            return o.value

        if isinstance(o, Priority):
            return o.value

        if isinstance(o, OrderCommentVisibility):
            return o.value

        if isinstance(o, OrderPaymentStatus):
            return o.value

        if isinstance(o, PageStatus):
            return o.value

        if isinstance(o, PaymentFeeType):
            return o.value

        if isinstance(o, PaymentMethodKind):
            return o.value

        if isinstance(o, PriceListStatus):
            return o.value

        if isinstance(o, PriceEntryType):
            return o.value

        if isinstance(o, Collection):
            return o.value

        if isinstance(o, ShippingMethodMatrixBasis):
            return o.value

        if isinstance(o, ShippingMethodPricingType):
            return o.value

        if isinstance(o, BuildRuntime):
            return o.value

        if isinstance(o, Framework):
            return o.value

        if isinstance(o, Adapter):
            return o.value

        if isinstance(o, Visibility):
            return o.value

        if isinstance(o, OrderItemType):
            return o.value

        if isinstance(o, StoreAssetRequestVisibility):
            return o.value

        if isinstance(o, AttributeBooleanStatus):
            return o.value

        if isinstance(o, AttributeDatetimeStatus):
            return o.value

        if isinstance(o, AttributeEmailStatus):
            return o.value

        if isinstance(o, AttributeEnumStatus):
            return o.value

        if isinstance(o, AttributeFloatStatus):
            return o.value

        if isinstance(o, AttributeIntegerStatus):
            return o.value

        if isinstance(o, AttributeIpStatus):
            return o.value

        if isinstance(o, AttributeLineStatus):
            return o.value

        if isinstance(o, AttributeLongtextStatus):
            return o.value

        if isinstance(o, AttributeMediumtextStatus):
            return o.value

        if isinstance(o, AttributePointStatus):
            return o.value

        if isinstance(o, AttributePolygonStatus):
            return o.value

        if isinstance(o, AttributeRelationshipStatus):
            return o.value

        if isinstance(o, AttributeStringStatus):
            return o.value

        if isinstance(o, AttributeTextStatus):
            return o.value

        if isinstance(o, AttributeUrlStatus):
            return o.value

        if isinstance(o, AttributeVarcharStatus):
            return o.value

        if isinstance(o, ColumnBooleanStatus):
            return o.value

        if isinstance(o, ColumnDatetimeStatus):
            return o.value

        if isinstance(o, ColumnEmailStatus):
            return o.value

        if isinstance(o, ColumnEnumStatus):
            return o.value

        if isinstance(o, ColumnFloatStatus):
            return o.value

        if isinstance(o, ColumnIntegerStatus):
            return o.value

        if isinstance(o, ColumnIpStatus):
            return o.value

        if isinstance(o, ColumnLineStatus):
            return o.value

        if isinstance(o, ColumnLongtextStatus):
            return o.value

        if isinstance(o, ColumnMediumtextStatus):
            return o.value

        if isinstance(o, ColumnPointStatus):
            return o.value

        if isinstance(o, ColumnPolygonStatus):
            return o.value

        if isinstance(o, ColumnRelationshipStatus):
            return o.value

        if isinstance(o, ColumnStringStatus):
            return o.value

        if isinstance(o, ColumnTextStatus):
            return o.value

        if isinstance(o, ColumnUrlStatus):
            return o.value

        if isinstance(o, ColumnVarcharStatus):
            return o.value

        if isinstance(o, DatabaseType):
            return o.value

        if isinstance(o, DeploymentStatus):
            return o.value

        if isinstance(o, ExecutionStatus):
            return o.value

        if isinstance(o, ExecutionTrigger):
            return o.value

        if isinstance(o, HealthAntivirusStatus):
            return o.value

        if isinstance(o, HealthStatusStatus):
            return o.value

        if isinstance(o, IndexStatus):
            return o.value

        if isinstance(o, MessageStatus):
            return o.value

        return super().default(o)
