import json
from ..models.base_model import AppwriteModel
from ..enums.runtime import Runtime
from ..enums.scopes import Scopes
from ..enums.runtimes import Runtimes
from ..enums.use_cases import UseCases
from ..enums.range import Range
from ..enums.type import Type
from ..enums.apps_create_vcs_deployment_type import AppsCreateVcsDeploymentType
from ..enums.apps_get_deployment_download_type import AppsGetDeploymentDownloadType
from ..enums.method import Method
from ..enums.code import Code
from ..enums.avatars_get_credit_card_code import AvatarsGetCreditCardCode
from ..enums.avatars_get_flag_code import AvatarsGetFlagCode
from ..enums.theme import Theme
from ..enums.timezone import Timezone
from ..enums.permissions import Permissions
from ..enums.output import Output
from ..enums.cart_status import CartStatus
from ..enums.cart_merge_strategy import CartMergeStrategy
from ..enums.name import Name
from ..enums.cart_io_direction import CartIoDirection
from ..enums.cart_io_entity import CartIoEntity
from ..enums.cart_io_format import CartIoFormat
from ..enums.cart_io_apply_mode import CartIoApplyMode
from ..enums.cart_export_format import CartExportFormat
from ..enums.cart_item_type import CartItemType
from ..enums.channel_status import ChannelStatus
from ..enums.channel_unassigned_visibility import ChannelUnassignedVisibility
from ..enums.channel_type_tone import ChannelTypeTone
from ..enums.channels_vocabularies_get_name import ChannelsVocabulariesGetName
from ..enums.tone import Tone
from ..enums.customers_vocabularies_get_name import CustomersVocabulariesGetName
from ..enums.customers_organizations_list_status import CustomersOrganizationsListStatus
from ..enums.organization_status import OrganizationStatus
from ..enums.status import Status
from ..enums.registration_status import RegistrationStatus
from ..enums.customers_contacts_create_registration_status import CustomersContactsCreateRegistrationStatus
from ..enums.contact_status import ContactStatus
from ..enums.contact_activity_kind import ContactActivityKind
from ..enums.source import Source
from ..enums.segment_member_source import SegmentMemberSource
from ..enums.rule_match import RuleMatch
from ..enums.segment_rule_match import SegmentRuleMatch
from ..enums.target import Target
from ..enums.form_status import FormStatus
from ..enums.form_submission_status import FormSubmissionStatus
from ..enums.forms_submissions_prune_status import FormsSubmissionsPruneStatus
from ..enums.forms_vocabularies_get_name import FormsVocabulariesGetName
from ..enums.inventories_movements_list_type import InventoriesMovementsListType
from ..enums.inventories_vocabularies_get_name import InventoriesVocabulariesGetName
from ..enums.inventories_reservations_list_status import InventoriesReservationsListStatus
from ..enums.inventories_locations_list_type import InventoriesLocationsListType
from ..enums.location_type import LocationType
from ..enums.format import Format
from ..enums.mode import Mode
from ..enums.create_import_target import CreateImportTarget
from ..enums.direction import Direction
from ..enums.apply_mode import ApplyMode
from ..enums.markets_list_status import MarketsListStatus
from ..enums.market_status import MarketStatus
from ..enums.markets_vocabulary_name import MarketsVocabularyName
from ..enums.resource_type import ResourceType
from ..enums.scope import Scope
from ..enums.reason import Reason
from ..enums.message_class import MessageClass
from ..enums.whatsapp_category import WhatsappCategory
from ..enums.order_list_kind_tone import OrderListKindTone
from ..enums.orderlists_vocabularies_get_name import OrderlistsVocabulariesGetName
from ..enums.order_list_cart_mode import OrderListCartMode
from ..enums.order_status import OrderStatus
from ..enums.order_payment_status import OrderPaymentStatus
from ..enums.order_fulfillment_status import OrderFulfillmentStatus
from ..enums.orders_vocabularies_get_name import OrdersVocabulariesGetName
from ..enums.order_comment_visibility import OrderCommentVisibility
from ..enums.order_return_settlement import OrderReturnSettlement
from ..enums.order_return_refusal import OrderReturnRefusal
from ..enums.page_edit_state_status import PageEditStateStatus
from ..enums.page_status import PageStatus
from ..enums.pages_vocabularies_get_name import PagesVocabulariesGetName
from ..enums.payment_status import PaymentStatus
from ..enums.payment_method_kind import PaymentMethodKind
from ..enums.payment_dunning_stage import PaymentDunningStage
from ..enums.payments_vocabularies_get_name import PaymentsVocabulariesGetName
from ..enums.payment_fee_type import PaymentFeeType
from ..enums.price_list_status import PriceListStatus
from ..enums.price_list_tax_basis import PriceListTaxBasis
from ..enums.price_entry_type import PriceEntryType
from ..enums.price_ending_rule import PriceEndingRule
from ..enums.price_entries_bulk_mode import PriceEntriesBulkMode
from ..enums.prices_vocabularies_get_name import PricesVocabulariesGetName
from ..enums.kind import Kind
from ..enums.products_kind import ProductsKind
from ..enums.entity_type import EntityType
from ..enums.products_assets_list_source import ProductsAssetsListSource
from ..enums.assets_source import AssetsSource
from ..enums.categories_rule_match import CategoriesRuleMatch
from ..enums.category_rule_match import CategoryRuleMatch
from ..enums.product_categories_source import ProductCategoriesSource
from ..enums.collection import Collection
from ..enums.shipping_carriers_list_status import ShippingCarriersListStatus
from ..enums.shipping_carrier_status import ShippingCarrierStatus
from ..enums.pricing_type import PricingType
from ..enums.shipping_method_matrix_basis import ShippingMethodMatrixBasis
from ..enums.shipping_method_pricing_type import ShippingMethodPricingType
from ..enums.shipping_vocabularies_get_name import ShippingVocabulariesGetName
from ..enums.build_runtime import BuildRuntime
from ..enums.framework import Framework
from ..enums.adapter import Adapter
from ..enums.sites_create_template_deployment_type import SitesCreateTemplateDeploymentType
from ..enums.visibility import Visibility
from ..enums.address_type_row_tone import AddressTypeRowTone
from ..enums.address_type_row_create_request_tone import AddressTypeRowCreateRequestTone
from ..enums.address_type_row_update_request_tone import AddressTypeRowUpdateRequestTone
from ..enums.attribute_value_bucket import AttributeValueBucket
from ..enums.auth_mail_source import AuthMailSource
from ..enums.recovery_mail_source import RecoveryMailSource
from ..enums.cart_price_snapshot_mode import CartPriceSnapshotMode
from ..enums.cart_vocabulary_tone import CartVocabularyTone
from ..enums.cart_vocabulary_name import CartVocabularyName
from ..enums.cart_vocabulary_source import CartVocabularySource
from ..enums.cart_vocabulary_ref_name import CartVocabularyRefName
from ..enums.category_rule_operator import CategoryRuleOperator
from ..enums.channel_unresolved_reason import ChannelUnresolvedReason
from ..enums.channel_context_source import ChannelContextSource
from ..enums.channel_inactive_behavior import ChannelInactiveBehavior
from ..enums.channel_policy_source import ChannelPolicySource
from ..enums.channel_policy_tenant_default import ChannelPolicyTenantDefault
from ..enums.channel_unassigned_policy import ChannelUnassignedPolicy
from ..enums.channel_visibility_reason import ChannelVisibilityReason
from ..enums.channel_vocabulary_tone import ChannelVocabularyTone
from ..enums.channel_vocabulary_name import ChannelVocabularyName
from ..enums.channel_vocabulary_source import ChannelVocabularySource
from ..enums.channel_vocabulary_ref_name import ChannelVocabularyRefName
from ..enums.contact_registration_status import ContactRegistrationStatus
from ..enums.contact_create_request_registration_status import ContactCreateRequestRegistrationStatus
from ..enums.contact_event_kind_tone import ContactEventKindTone
from ..enums.contact_event_kind_create_request_tone import ContactEventKindCreateRequestTone
from ..enums.contact_event_kind_update_request_tone import ContactEventKindUpdateRequestTone
from ..enums.contact_permissions_permissions import ContactPermissionsPermissions
from ..enums.contact_update_request_registration_status import ContactUpdateRequestRegistrationStatus
from ..enums.form_notify_source import FormNotifySource
from ..enums.form_submission_prune_request_status import FormSubmissionPruneRequestStatus
from ..enums.forms_vocabulary_tone import FormsVocabularyTone
from ..enums.forms_vocabulary_name import FormsVocabularyName
from ..enums.forms_vocabulary_summary_name import FormsVocabularySummaryName
from ..enums.inventory_vocabulary_default_tone import InventoryVocabularyDefaultTone
from ..enums.inventory_vocabulary_source import InventoryVocabularySource
from ..enums.io_profile_resource_apply_mode import IoProfileResourceApplyMode
from ..enums.io_profile_resource_direction import IoProfileResourceDirection
from ..enums.lifecycle_stage_tone import LifecycleStageTone
from ..enums.lifecycle_stage_create_request_tone import LifecycleStageCreateRequestTone
from ..enums.lifecycle_stage_update_request_tone import LifecycleStageUpdateRequestTone
from ..enums.market_default_locale_source import MarketDefaultLocaleSource
from ..enums.market_locale_fallback import MarketLocaleFallback
from ..enums.market_locale_granularity import MarketLocaleGranularity
from ..enums.market_pricing_source import MarketPricingSource
from ..enums.market_tax_basis import MarketTaxBasis
from ..enums.market_readiness_blocking import MarketReadinessBlocking
from ..enums.market_readiness_warnings import MarketReadinessWarnings
from ..enums.market_readiness_check_id import MarketReadinessCheckId
from ..enums.market_readiness_severity import MarketReadinessSeverity
from ..enums.market_readiness_report_blocking import MarketReadinessReportBlocking
from ..enums.market_readiness_report_warnings import MarketReadinessReportWarnings
from ..enums.markets_vocabulary_tone import MarketsVocabularyTone
from ..enums.markets_vocabulary_source import MarketsVocabularySource
from ..enums.markets_vocabulary_summary_name import MarketsVocabularySummaryName
from ..enums.order_cancellation_scope import OrderCancellationScope
from ..enums.order_customer_rollup_request_statuses import OrderCustomerRollupRequestStatuses
from ..enums.order_customer_rollup_response_statuses import OrderCustomerRollupResponseStatuses
from ..enums.order_item_type import OrderItemType
from ..enums.order_list_kind_row_tone import OrderListKindRowTone
from ..enums.order_list_vocabulary_default_tone import OrderListVocabularyDefaultTone
from ..enums.order_list_vocabulary_name import OrderListVocabularyName
from ..enums.order_list_vocabulary_source import OrderListVocabularySource
from ..enums.order_list_vocabulary_tone import OrderListVocabularyTone
from ..enums.order_return_status import OrderReturnStatus
from ..enums.order_vocabulary_tone import OrderVocabularyTone
from ..enums.order_vocabulary_name import OrderVocabularyName
from ..enums.order_vocabulary_source import OrderVocabularySource
from ..enums.order_vocabulary_summary_name import OrderVocabularySummaryName
from ..enums.order_resolution_stage import OrderResolutionStage
from ..enums.pages_vocabulary_app import PagesVocabularyApp
from ..enums.pages_vocabulary_tone import PagesVocabularyTone
from ..enums.pages_vocabulary_name import PagesVocabularyName
from ..enums.pages_vocabulary_source import PagesVocabularySource
from ..enums.pages_vocabulary_index_app import PagesVocabularyIndexApp
from ..enums.payment_failure_code import PaymentFailureCode
from ..enums.payment_term_tone import PaymentTermTone
from ..enums.payment_term_create_request_tone import PaymentTermCreateRequestTone
from ..enums.payment_term_update_request_tone import PaymentTermUpdateRequestTone
from ..enums.payment_vocabulary_tone import PaymentVocabularyTone
from ..enums.price_entries_adjust_response_rounding import PriceEntriesAdjustResponseRounding
from ..enums.price_entries_adjust_response_rounding_mode import PriceEntriesAdjustResponseRoundingMode
from ..enums.price_rounding_mode import PriceRoundingMode
from ..enums.price_currency_source import PriceCurrencySource
from ..enums.price_list_tiebreak import PriceListTiebreak
from ..enums.price_tax_inclusive_default import PriceTaxInclusiveDefault
from ..enums.price_tax_unresolved_reason import PriceTaxUnresolvedReason
from ..enums.price_tax_market_source import PriceTaxMarketSource
from ..enums.price_vocabulary_tone import PriceVocabularyTone
from ..enums.price_vocabulary_name import PriceVocabularyName
from ..enums.price_vocabulary_source import PriceVocabularySource
from ..enums.price_vocabulary_ref_name import PriceVocabularyRefName
from ..enums.product_grid_column_source import ProductGridColumnSource
from ..enums.product_label_source import ProductLabelSource
from ..enums.product_label_attribute_source import ProductLabelAttributeSource
from ..enums.reorder_point_source import ReorderPointSource
from ..enums.reservation_status import ReservationStatus
from ..enums.price_on_request_reason import PriceOnRequestReason
from ..enums.price_tax_basis import PriceTaxBasis
from ..enums.price_tax_basis_source import PriceTaxBasisSource
from ..enums.role_catalog_response_source import RoleCatalogResponseSource
from ..enums.segment_rule_operator import SegmentRuleOperator
from ..enums.segment_rule_preview_request_rule_match import SegmentRulePreviewRequestRuleMatch
from ..enums.segment_rule_preview_request_target import SegmentRulePreviewRequestTarget
from ..enums.segment_rule_preview_response_rule_match import SegmentRulePreviewResponseRuleMatch
from ..enums.segment_rule_preview_response_target import SegmentRulePreviewResponseTarget
from ..enums.segment_rules_target import SegmentRulesTarget
from ..enums.shipping_carrier_source import ShippingCarrierSource
from ..enums.shipping_rate_pricing_type import ShippingRatePricingType
from ..enums.shipping_tax_source import ShippingTaxSource
from ..enums.shipping_free_above_basis import ShippingFreeAboveBasis
from ..enums.shipping_rates_basis_matrix_basis_default import ShippingRatesBasisMatrixBasisDefault
from ..enums.shipping_service_level_create_request_tone import ShippingServiceLevelCreateRequestTone
from ..enums.shipping_service_level_row_tone import ShippingServiceLevelRowTone
from ..enums.shipping_service_level_update_request_tone import ShippingServiceLevelUpdateRequestTone
from ..enums.shipping_tax_unresolved_reason import ShippingTaxUnresolvedReason
from ..enums.shipping_tax_market_source import ShippingTaxMarketSource
from ..enums.shipping_tax_context_via import ShippingTaxContextVia
from ..enums.shipping_tracking_carrier_status import ShippingTrackingCarrierStatus
from ..enums.shipping_vocabulary_default_tone import ShippingVocabularyDefaultTone
from ..enums.shipping_vocabulary_source import ShippingVocabularySource
from ..enums.shipping_vocabulary_tone import ShippingVocabularyTone
from ..enums.shipping_weight_unit_create_request_tone import ShippingWeightUnitCreateRequestTone
from ..enums.shipping_weight_unit_row_tone import ShippingWeightUnitRowTone
from ..enums.shipping_weight_unit_update_request_tone import ShippingWeightUnitUpdateRequestTone
from ..enums.stock_movement_type import StockMovementType
from ..enums.store_asset_request_visibility import StoreAssetRequestVisibility
from ..enums.validation_failed_response_status import ValidationFailedResponseStatus
from ..enums.vocabulary_default_tone import VocabularyDefaultTone
from ..enums.vocabulary_source import VocabularySource
from ..enums.vocabulary_tone import VocabularyTone
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
from ..enums.message2_status import Message2Status

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

        if isinstance(o, AppsCreateVcsDeploymentType):
            return o.value

        if isinstance(o, AppsGetDeploymentDownloadType):
            return o.value

        if isinstance(o, Method):
            return o.value

        if isinstance(o, Code):
            return o.value

        if isinstance(o, AvatarsGetCreditCardCode):
            return o.value

        if isinstance(o, AvatarsGetFlagCode):
            return o.value

        if isinstance(o, Theme):
            return o.value

        if isinstance(o, Timezone):
            return o.value

        if isinstance(o, Permissions):
            return o.value

        if isinstance(o, Output):
            return o.value

        if isinstance(o, CartStatus):
            return o.value

        if isinstance(o, CartMergeStrategy):
            return o.value

        if isinstance(o, Name):
            return o.value

        if isinstance(o, CartIoDirection):
            return o.value

        if isinstance(o, CartIoEntity):
            return o.value

        if isinstance(o, CartIoFormat):
            return o.value

        if isinstance(o, CartIoApplyMode):
            return o.value

        if isinstance(o, CartExportFormat):
            return o.value

        if isinstance(o, CartItemType):
            return o.value

        if isinstance(o, ChannelStatus):
            return o.value

        if isinstance(o, ChannelUnassignedVisibility):
            return o.value

        if isinstance(o, ChannelTypeTone):
            return o.value

        if isinstance(o, ChannelsVocabulariesGetName):
            return o.value

        if isinstance(o, Tone):
            return o.value

        if isinstance(o, CustomersVocabulariesGetName):
            return o.value

        if isinstance(o, CustomersOrganizationsListStatus):
            return o.value

        if isinstance(o, OrganizationStatus):
            return o.value

        if isinstance(o, Status):
            return o.value

        if isinstance(o, RegistrationStatus):
            return o.value

        if isinstance(o, CustomersContactsCreateRegistrationStatus):
            return o.value

        if isinstance(o, ContactStatus):
            return o.value

        if isinstance(o, ContactActivityKind):
            return o.value

        if isinstance(o, Source):
            return o.value

        if isinstance(o, SegmentMemberSource):
            return o.value

        if isinstance(o, RuleMatch):
            return o.value

        if isinstance(o, SegmentRuleMatch):
            return o.value

        if isinstance(o, Target):
            return o.value

        if isinstance(o, FormStatus):
            return o.value

        if isinstance(o, FormSubmissionStatus):
            return o.value

        if isinstance(o, FormsSubmissionsPruneStatus):
            return o.value

        if isinstance(o, FormsVocabulariesGetName):
            return o.value

        if isinstance(o, InventoriesMovementsListType):
            return o.value

        if isinstance(o, InventoriesVocabulariesGetName):
            return o.value

        if isinstance(o, InventoriesReservationsListStatus):
            return o.value

        if isinstance(o, InventoriesLocationsListType):
            return o.value

        if isinstance(o, LocationType):
            return o.value

        if isinstance(o, Format):
            return o.value

        if isinstance(o, Mode):
            return o.value

        if isinstance(o, CreateImportTarget):
            return o.value

        if isinstance(o, Direction):
            return o.value

        if isinstance(o, ApplyMode):
            return o.value

        if isinstance(o, MarketsListStatus):
            return o.value

        if isinstance(o, MarketStatus):
            return o.value

        if isinstance(o, MarketsVocabularyName):
            return o.value

        if isinstance(o, ResourceType):
            return o.value

        if isinstance(o, Scope):
            return o.value

        if isinstance(o, Reason):
            return o.value

        if isinstance(o, MessageClass):
            return o.value

        if isinstance(o, WhatsappCategory):
            return o.value

        if isinstance(o, OrderListKindTone):
            return o.value

        if isinstance(o, OrderlistsVocabulariesGetName):
            return o.value

        if isinstance(o, OrderListCartMode):
            return o.value

        if isinstance(o, OrderStatus):
            return o.value

        if isinstance(o, OrderPaymentStatus):
            return o.value

        if isinstance(o, OrderFulfillmentStatus):
            return o.value

        if isinstance(o, OrdersVocabulariesGetName):
            return o.value

        if isinstance(o, OrderCommentVisibility):
            return o.value

        if isinstance(o, OrderReturnSettlement):
            return o.value

        if isinstance(o, OrderReturnRefusal):
            return o.value

        if isinstance(o, PageEditStateStatus):
            return o.value

        if isinstance(o, PageStatus):
            return o.value

        if isinstance(o, PagesVocabulariesGetName):
            return o.value

        if isinstance(o, PaymentStatus):
            return o.value

        if isinstance(o, PaymentMethodKind):
            return o.value

        if isinstance(o, PaymentDunningStage):
            return o.value

        if isinstance(o, PaymentsVocabulariesGetName):
            return o.value

        if isinstance(o, PaymentFeeType):
            return o.value

        if isinstance(o, PriceListStatus):
            return o.value

        if isinstance(o, PriceListTaxBasis):
            return o.value

        if isinstance(o, PriceEntryType):
            return o.value

        if isinstance(o, PriceEndingRule):
            return o.value

        if isinstance(o, PriceEntriesBulkMode):
            return o.value

        if isinstance(o, PricesVocabulariesGetName):
            return o.value

        if isinstance(o, Kind):
            return o.value

        if isinstance(o, ProductsKind):
            return o.value

        if isinstance(o, EntityType):
            return o.value

        if isinstance(o, ProductsAssetsListSource):
            return o.value

        if isinstance(o, AssetsSource):
            return o.value

        if isinstance(o, CategoriesRuleMatch):
            return o.value

        if isinstance(o, CategoryRuleMatch):
            return o.value

        if isinstance(o, ProductCategoriesSource):
            return o.value

        if isinstance(o, Collection):
            return o.value

        if isinstance(o, ShippingCarriersListStatus):
            return o.value

        if isinstance(o, ShippingCarrierStatus):
            return o.value

        if isinstance(o, PricingType):
            return o.value

        if isinstance(o, ShippingMethodMatrixBasis):
            return o.value

        if isinstance(o, ShippingMethodPricingType):
            return o.value

        if isinstance(o, ShippingVocabulariesGetName):
            return o.value

        if isinstance(o, BuildRuntime):
            return o.value

        if isinstance(o, Framework):
            return o.value

        if isinstance(o, Adapter):
            return o.value

        if isinstance(o, SitesCreateTemplateDeploymentType):
            return o.value

        if isinstance(o, Visibility):
            return o.value

        if isinstance(o, AddressTypeRowTone):
            return o.value

        if isinstance(o, AddressTypeRowCreateRequestTone):
            return o.value

        if isinstance(o, AddressTypeRowUpdateRequestTone):
            return o.value

        if isinstance(o, AttributeValueBucket):
            return o.value

        if isinstance(o, AuthMailSource):
            return o.value

        if isinstance(o, RecoveryMailSource):
            return o.value

        if isinstance(o, CartPriceSnapshotMode):
            return o.value

        if isinstance(o, CartVocabularyTone):
            return o.value

        if isinstance(o, CartVocabularyName):
            return o.value

        if isinstance(o, CartVocabularySource):
            return o.value

        if isinstance(o, CartVocabularyRefName):
            return o.value

        if isinstance(o, CategoryRuleOperator):
            return o.value

        if isinstance(o, ChannelUnresolvedReason):
            return o.value

        if isinstance(o, ChannelContextSource):
            return o.value

        if isinstance(o, ChannelInactiveBehavior):
            return o.value

        if isinstance(o, ChannelPolicySource):
            return o.value

        if isinstance(o, ChannelPolicyTenantDefault):
            return o.value

        if isinstance(o, ChannelUnassignedPolicy):
            return o.value

        if isinstance(o, ChannelVisibilityReason):
            return o.value

        if isinstance(o, ChannelVocabularyTone):
            return o.value

        if isinstance(o, ChannelVocabularyName):
            return o.value

        if isinstance(o, ChannelVocabularySource):
            return o.value

        if isinstance(o, ChannelVocabularyRefName):
            return o.value

        if isinstance(o, ContactRegistrationStatus):
            return o.value

        if isinstance(o, ContactCreateRequestRegistrationStatus):
            return o.value

        if isinstance(o, ContactEventKindTone):
            return o.value

        if isinstance(o, ContactEventKindCreateRequestTone):
            return o.value

        if isinstance(o, ContactEventKindUpdateRequestTone):
            return o.value

        if isinstance(o, ContactPermissionsPermissions):
            return o.value

        if isinstance(o, ContactUpdateRequestRegistrationStatus):
            return o.value

        if isinstance(o, FormNotifySource):
            return o.value

        if isinstance(o, FormSubmissionPruneRequestStatus):
            return o.value

        if isinstance(o, FormsVocabularyTone):
            return o.value

        if isinstance(o, FormsVocabularyName):
            return o.value

        if isinstance(o, FormsVocabularySummaryName):
            return o.value

        if isinstance(o, InventoryVocabularyDefaultTone):
            return o.value

        if isinstance(o, InventoryVocabularySource):
            return o.value

        if isinstance(o, IoProfileResourceApplyMode):
            return o.value

        if isinstance(o, IoProfileResourceDirection):
            return o.value

        if isinstance(o, LifecycleStageTone):
            return o.value

        if isinstance(o, LifecycleStageCreateRequestTone):
            return o.value

        if isinstance(o, LifecycleStageUpdateRequestTone):
            return o.value

        if isinstance(o, MarketDefaultLocaleSource):
            return o.value

        if isinstance(o, MarketLocaleFallback):
            return o.value

        if isinstance(o, MarketLocaleGranularity):
            return o.value

        if isinstance(o, MarketPricingSource):
            return o.value

        if isinstance(o, MarketTaxBasis):
            return o.value

        if isinstance(o, MarketReadinessBlocking):
            return o.value

        if isinstance(o, MarketReadinessWarnings):
            return o.value

        if isinstance(o, MarketReadinessCheckId):
            return o.value

        if isinstance(o, MarketReadinessSeverity):
            return o.value

        if isinstance(o, MarketReadinessReportBlocking):
            return o.value

        if isinstance(o, MarketReadinessReportWarnings):
            return o.value

        if isinstance(o, MarketsVocabularyTone):
            return o.value

        if isinstance(o, MarketsVocabularySource):
            return o.value

        if isinstance(o, MarketsVocabularySummaryName):
            return o.value

        if isinstance(o, OrderCancellationScope):
            return o.value

        if isinstance(o, OrderCustomerRollupRequestStatuses):
            return o.value

        if isinstance(o, OrderCustomerRollupResponseStatuses):
            return o.value

        if isinstance(o, OrderItemType):
            return o.value

        if isinstance(o, OrderListKindRowTone):
            return o.value

        if isinstance(o, OrderListVocabularyDefaultTone):
            return o.value

        if isinstance(o, OrderListVocabularyName):
            return o.value

        if isinstance(o, OrderListVocabularySource):
            return o.value

        if isinstance(o, OrderListVocabularyTone):
            return o.value

        if isinstance(o, OrderReturnStatus):
            return o.value

        if isinstance(o, OrderVocabularyTone):
            return o.value

        if isinstance(o, OrderVocabularyName):
            return o.value

        if isinstance(o, OrderVocabularySource):
            return o.value

        if isinstance(o, OrderVocabularySummaryName):
            return o.value

        if isinstance(o, OrderResolutionStage):
            return o.value

        if isinstance(o, PagesVocabularyApp):
            return o.value

        if isinstance(o, PagesVocabularyTone):
            return o.value

        if isinstance(o, PagesVocabularyName):
            return o.value

        if isinstance(o, PagesVocabularySource):
            return o.value

        if isinstance(o, PagesVocabularyIndexApp):
            return o.value

        if isinstance(o, PaymentFailureCode):
            return o.value

        if isinstance(o, PaymentTermTone):
            return o.value

        if isinstance(o, PaymentTermCreateRequestTone):
            return o.value

        if isinstance(o, PaymentTermUpdateRequestTone):
            return o.value

        if isinstance(o, PaymentVocabularyTone):
            return o.value

        if isinstance(o, PriceEntriesAdjustResponseRounding):
            return o.value

        if isinstance(o, PriceEntriesAdjustResponseRoundingMode):
            return o.value

        if isinstance(o, PriceRoundingMode):
            return o.value

        if isinstance(o, PriceCurrencySource):
            return o.value

        if isinstance(o, PriceListTiebreak):
            return o.value

        if isinstance(o, PriceTaxInclusiveDefault):
            return o.value

        if isinstance(o, PriceTaxUnresolvedReason):
            return o.value

        if isinstance(o, PriceTaxMarketSource):
            return o.value

        if isinstance(o, PriceVocabularyTone):
            return o.value

        if isinstance(o, PriceVocabularyName):
            return o.value

        if isinstance(o, PriceVocabularySource):
            return o.value

        if isinstance(o, PriceVocabularyRefName):
            return o.value

        if isinstance(o, ProductGridColumnSource):
            return o.value

        if isinstance(o, ProductLabelSource):
            return o.value

        if isinstance(o, ProductLabelAttributeSource):
            return o.value

        if isinstance(o, ReorderPointSource):
            return o.value

        if isinstance(o, ReservationStatus):
            return o.value

        if isinstance(o, PriceOnRequestReason):
            return o.value

        if isinstance(o, PriceTaxBasis):
            return o.value

        if isinstance(o, PriceTaxBasisSource):
            return o.value

        if isinstance(o, RoleCatalogResponseSource):
            return o.value

        if isinstance(o, SegmentRuleOperator):
            return o.value

        if isinstance(o, SegmentRulePreviewRequestRuleMatch):
            return o.value

        if isinstance(o, SegmentRulePreviewRequestTarget):
            return o.value

        if isinstance(o, SegmentRulePreviewResponseRuleMatch):
            return o.value

        if isinstance(o, SegmentRulePreviewResponseTarget):
            return o.value

        if isinstance(o, SegmentRulesTarget):
            return o.value

        if isinstance(o, ShippingCarrierSource):
            return o.value

        if isinstance(o, ShippingRatePricingType):
            return o.value

        if isinstance(o, ShippingTaxSource):
            return o.value

        if isinstance(o, ShippingFreeAboveBasis):
            return o.value

        if isinstance(o, ShippingRatesBasisMatrixBasisDefault):
            return o.value

        if isinstance(o, ShippingServiceLevelCreateRequestTone):
            return o.value

        if isinstance(o, ShippingServiceLevelRowTone):
            return o.value

        if isinstance(o, ShippingServiceLevelUpdateRequestTone):
            return o.value

        if isinstance(o, ShippingTaxUnresolvedReason):
            return o.value

        if isinstance(o, ShippingTaxMarketSource):
            return o.value

        if isinstance(o, ShippingTaxContextVia):
            return o.value

        if isinstance(o, ShippingTrackingCarrierStatus):
            return o.value

        if isinstance(o, ShippingVocabularyDefaultTone):
            return o.value

        if isinstance(o, ShippingVocabularySource):
            return o.value

        if isinstance(o, ShippingVocabularyTone):
            return o.value

        if isinstance(o, ShippingWeightUnitCreateRequestTone):
            return o.value

        if isinstance(o, ShippingWeightUnitRowTone):
            return o.value

        if isinstance(o, ShippingWeightUnitUpdateRequestTone):
            return o.value

        if isinstance(o, StockMovementType):
            return o.value

        if isinstance(o, StoreAssetRequestVisibility):
            return o.value

        if isinstance(o, ValidationFailedResponseStatus):
            return o.value

        if isinstance(o, VocabularyDefaultTone):
            return o.value

        if isinstance(o, VocabularySource):
            return o.value

        if isinstance(o, VocabularyTone):
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

        if isinstance(o, Message2Status):
            return o.value

        return super().default(o)
