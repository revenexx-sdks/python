from .base_model import AppwriteModel
from .address import Address
from .address_create_request import AddressCreateRequest
from .address_type_row import AddressTypeRow
from .address_type_row_create_request import AddressTypeRowCreateRequest
from .address_type_row_update_request import AddressTypeRowUpdateRequest
from .address_update_request import AddressUpdateRequest
from .asset_families import AssetFamilies
from .asset_families_create_request import AssetFamiliesCreateRequest
from .asset_families_filter import AssetFamiliesFilter
from .asset_families_update_request import AssetFamiliesUpdateRequest
from .asset_resource import AssetResource
from .assets import Assets
from .assets_create_request import AssetsCreateRequest
from .assets_filter import AssetsFilter
from .assets_update_request import AssetsUpdateRequest
from .association_types import AssociationTypes
from .association_types_create_request import AssociationTypesCreateRequest
from .association_types_filter import AssociationTypesFilter
from .association_types_update_request import AssociationTypesUpdateRequest
from .attribute_field import AttributeField
from .attribute_field_option import AttributeFieldOption
from .attribute_field_storage import AttributeFieldStorage
from .attribute_field_validation import AttributeFieldValidation
from .attribute_groups import AttributeGroups
from .attribute_groups_create_request import AttributeGroupsCreateRequest
from .attribute_groups_filter import AttributeGroupsFilter
from .attribute_groups_update_request import AttributeGroupsUpdateRequest
from .attribute_options import AttributeOptions
from .attribute_options_create_request import AttributeOptionsCreateRequest
from .attribute_options_filter import AttributeOptionsFilter
from .attribute_options_update_request import AttributeOptionsUpdateRequest
from .attribute_schema_family import AttributeSchemaFamily
from .attribute_schema_group import AttributeSchemaGroup
from .attributes import Attributes
from .attributes_create_request import AttributesCreateRequest
from .attributes_filter import AttributesFilter
from .attributes_update_request import AttributesUpdateRequest
from .audit_entry import AuditEntry
from .auth_login_request import AuthLoginRequest
from .auth_login_response import AuthLoginResponse
from .auth_logout_request import AuthLogoutRequest
from .auth_magic_link_confirm_request import AuthMagicLinkConfirmRequest
from .auth_magic_link_confirm_response import AuthMagicLinkConfirmResponse
from .auth_magic_link_request import AuthMagicLinkRequest
from .auth_magic_link_response import AuthMagicLinkResponse
from .auth_me_request import AuthMeRequest
from .auth_me_response import AuthMeResponse
from .auth_mfa_challenge_confirm_request import AuthMfaChallengeConfirmRequest
from .auth_mfa_challenge_confirm_response import AuthMfaChallengeConfirmResponse
from .auth_mfa_challenge_request import AuthMfaChallengeRequest
from .auth_mfa_challenge_response import AuthMfaChallengeResponse
from .auth_otp_confirm_request import AuthOtpConfirmRequest
from .auth_otp_confirm_response import AuthOtpConfirmResponse
from .auth_otp_request import AuthOtpRequest
from .auth_otp_response import AuthOtpResponse
from .auth_recovery_confirm_request import AuthRecoveryConfirmRequest
from .auth_recovery_confirm_response import AuthRecoveryConfirmResponse
from .auth_recovery_request import AuthRecoveryRequest
from .auth_recovery_response import AuthRecoveryResponse
from .auth_register_request import AuthRegisterRequest
from .auth_register_response import AuthRegisterResponse
from .auth_session import AuthSession
from .auth_verification_confirm_request import AuthVerificationConfirmRequest
from .auth_verification_confirm_response import AuthVerificationConfirmResponse
from .auth_verification_request import AuthVerificationRequest
from .auth_verification_response import AuthVerificationResponse
from .binding import Binding
from .bulk_job import BulkJob
from .bulk_job_status import BulkJobStatus
from .bulk_job_type import BulkJobType
from .cart import Cart
from .cart_abandon_sweep import CartAbandonSweep
from .cart_claim_request import CartClaimRequest
from .cart_conversion import CartConversion
from .cart_conversion_pricing import CartConversionPricing
from .cart_conversion_reservation import CartConversionReservation
from .cart_create_request import CartCreateRequest
from .cart_export import CartExport
from .cart_export_request import CartExportRequest
from .cart_import import CartImport
from .cart_import_request import CartImportRequest
from .cart_io_mapping import CartIoMapping
from .cart_io_mapping_column import CartIoMappingColumn
from .cart_item import CartItem
from .cart_item_create_request import CartItemCreateRequest
from .cart_item_snapshot import CartItemSnapshot
from .cart_item_update_request import CartItemUpdateRequest
from .cart_items_replace_request import CartItemsReplaceRequest
from .cart_maintenance_request import CartMaintenanceRequest
from .cart_maintenance_result import CartMaintenanceResult
from .cart_merge_into_request import CartMergeIntoRequest
from .cart_merge_request import CartMergeRequest
from .cart_merge_result import CartMergeResult
from .cart_order_request import CartOrderRequest
from .cart_purge_sweep import CartPurgeSweep
from .cart_update_request import CartUpdateRequest
from .cart_vocabulary import CartVocabulary
from .cart_vocabulary_index import CartVocabularyIndex
from .cart_vocabulary_ref import CartVocabularyRef
from .cart_vocabulary_value import CartVocabularyValue
from .categories import Categories
from .categories_create_request import CategoriesCreateRequest
from .categories_filter import CategoriesFilter
from .categories_update_request import CategoriesUpdateRequest
from .category_recompute_all_request import CategoryRecomputeAllRequest
from .category_recompute_request import CategoryRecomputeRequest
from .category_recompute_result import CategoryRecomputeResult
from .category_recompute_summary import CategoryRecomputeSummary
from .category_rule_condition import CategoryRuleCondition
from .category_rule_sample import CategoryRuleSample
from .category_rules_request import CategoryRulesRequest
from .channel import Channel
from .channel_context import ChannelContext
from .channel_create_request import ChannelCreateRequest
from .channel_defaults import ChannelDefaults
from .channel_policy import ChannelPolicy
from .channel_type_create_request import ChannelTypeCreateRequest
from .channel_type_defaults import ChannelTypeDefaults
from .channel_type_row import ChannelTypeRow
from .channel_type_update_request import ChannelTypeUpdateRequest
from .channel_update_request import ChannelUpdateRequest
from .channel_visibility import ChannelVisibility
from .channel_visibility_counts import ChannelVisibilityCounts
from .channel_visibility_decision import ChannelVisibilityDecision
from .channel_visibility_item import ChannelVisibilityItem
from .channel_visibility_request import ChannelVisibilityRequest
from .channel_vocabulary import ChannelVocabulary
from .channel_vocabulary_index import ChannelVocabularyIndex
from .channel_vocabulary_ref import ChannelVocabularyRef
from .channel_vocabulary_value import ChannelVocabularyValue
from .collection import Collection
from .collection_field import CollectionField
from .collection_list import CollectionList
from .contact import Contact
from .contact_activity_request import ContactActivityRequest
from .contact_create_request import ContactCreateRequest
from .contact_event import ContactEvent
from .contact_event_kind import ContactEventKind
from .contact_event_kind_create_request import ContactEventKindCreateRequest
from .contact_event_kind_update_request import ContactEventKindUpdateRequest
from .contact_invite_request import ContactInviteRequest
from .contact_invite_response import ContactInviteResponse
from .contact_permissions import ContactPermissions
from .contact_update_request import ContactUpdateRequest
from .customers_defaults_request import CustomersDefaultsRequest
from .customers_defaults_response import CustomersDefaultsResponse
from .delivery_block import DeliveryBlock
from .delivery_menu import DeliveryMenu
from .delivery_page import DeliveryPage
from .delivery_page_ref import DeliveryPageRef
from .editor_state import EditorState
from .eligible_payment_method import EligiblePaymentMethod
from .error import Error
from .facet_count import FacetCount
from .families import Families
from .families_create_request import FamiliesCreateRequest
from .families_filter import FamiliesFilter
from .families_update_request import FamiliesUpdateRequest
from .family_attributes import FamilyAttributes
from .family_attributes_create_request import FamilyAttributesCreateRequest
from .family_attributes_filter import FamilyAttributesFilter
from .family_attributes_update_request import FamilyAttributesUpdateRequest
from .family_variants import FamilyVariants
from .family_variants_create_request import FamilyVariantsCreateRequest
from .family_variants_filter import FamilyVariantsFilter
from .family_variants_update_request import FamilyVariantsUpdateRequest
from .folder_resource import FolderResource
from .form import Form
from .form_action_mapping import FormActionMapping
from .form_create_request import FormCreateRequest
from .form_defaults_result import FormDefaultsResult
from .form_delete_result import FormDeleteResult
from .form_kit_node import FormKitNode
from .form_kit_step_marker import FormKitStepMarker
from .form_list_filter import FormListFilter
from .form_post_submit_action import FormPostSubmitAction
from .form_settings import FormSettings
from .form_submission import FormSubmission
from .form_submission_create_request import FormSubmissionCreateRequest
from .form_submission_delete_result import FormSubmissionDeleteResult
from .form_submission_list_filter import FormSubmissionListFilter
from .form_submission_metadata import FormSubmissionMetadata
from .form_submission_prune_request import FormSubmissionPruneRequest
from .form_submission_prune_result import FormSubmissionPruneResult
from .form_submission_prune_sample import FormSubmissionPruneSample
from .form_submission_update_request import FormSubmissionUpdateRequest
from .form_update_request import FormUpdateRequest
from .forms_page import FormsPage
from .forms_vocabulary import FormsVocabulary
from .forms_vocabulary_index import FormsVocabularyIndex
from .forms_vocabulary_summary import FormsVocabularySummary
from .forms_vocabulary_value import FormsVocabularyValue
from .inventory_adjust_item import InventoryAdjustItem
from .inventory_adjust_request import InventoryAdjustRequest
from .inventory_availability_item import InventoryAvailabilityItem
from .inventory_availability_request import InventoryAvailabilityRequest
from .inventory_commit_request import InventoryCommitRequest
from .inventory_receive_request import InventoryReceiveRequest
from .inventory_release_request import InventoryReleaseRequest
from .inventory_reserve_request import InventoryReserveRequest
from .inventory_restock_request import InventoryRestockRequest
from .inventory_ship_to import InventoryShipTo
from .inventory_stock_item import InventoryStockItem
from .inventory_vocabulary import InventoryVocabulary
from .inventory_vocabulary_index import InventoryVocabularyIndex
from .io_entity import IoEntity
from .io_profile import IoProfile
from .io_profile_create_request import IoProfileCreateRequest
from .io_profile_format import IoProfileFormat
from .io_profile_resource import IoProfileResource
from .io_profile_update_request import IoProfileUpdateRequest
from .item_availability import ItemAvailability
from .layout import Layout
from .library_item import LibraryItem
from .library_template import LibraryTemplate
from .lifecycle_stage import LifecycleStage
from .lifecycle_stage_create_request import LifecycleStageCreateRequest
from .lifecycle_stage_update_request import LifecycleStageUpdateRequest
from .location import Location
from .location_availability import LocationAvailability
from .location_create_request import LocationCreateRequest
from .location_update_request import LocationUpdateRequest
from .locations_filter import LocationsFilter
from .market import Market
from .market_backfill_added import MarketBackfillAdded
from .market_backfill_kept import MarketBackfillKept
from .market_backfill_request import MarketBackfillRequest
from .market_backfill_result import MarketBackfillResult
from .market_backfill_seeded import MarketBackfillSeeded
from .market_clone_copied import MarketCloneCopied
from .market_clone_request import MarketCloneRequest
from .market_clone_result import MarketCloneResult
from .market_clone_seeded import MarketCloneSeeded
from .market_context import MarketContext
from .market_create_request import MarketCreateRequest
from .market_currency import MarketCurrency
from .market_currency_create_request import MarketCurrencyCreateRequest
from .market_currency_deleted import MarketCurrencyDeleted
from .market_currency_filter import MarketCurrencyFilter
from .market_currency_list import MarketCurrencyList
from .market_currency_update_request import MarketCurrencyUpdateRequest
from .market_default_locale import MarketDefaultLocale
from .market_deleted import MarketDeleted
from .market_filter import MarketFilter
from .market_list import MarketList
from .market_locale import MarketLocale
from .market_locale_create_request import MarketLocaleCreateRequest
from .market_locale_deleted import MarketLocaleDeleted
from .market_locale_filter import MarketLocaleFilter
from .market_locale_keys import MarketLocaleKeys
from .market_locale_list import MarketLocaleList
from .market_locale_policy import MarketLocalePolicy
from .market_locale_update_request import MarketLocaleUpdateRequest
from .market_make_default_request import MarketMakeDefaultRequest
from .market_make_default_response import MarketMakeDefaultResponse
from .market_pricing import MarketPricing
from .market_readiness import MarketReadiness
from .market_readiness_check import MarketReadinessCheck
from .market_readiness_counts import MarketReadinessCounts
from .market_readiness_report import MarketReadinessReport
from .market_readiness_subject import MarketReadinessSubject
from .market_ref import MarketRef
from .market_tax_class import MarketTaxClass
from .market_tax_class_create_request import MarketTaxClassCreateRequest
from .market_tax_class_deleted import MarketTaxClassDeleted
from .market_tax_class_filter import MarketTaxClassFilter
from .market_tax_class_list import MarketTaxClassList
from .market_tax_class_update_request import MarketTaxClassUpdateRequest
from .market_update_request import MarketUpdateRequest
from .markets_page import MarketsPage
from .markets_vocabulary import MarketsVocabulary
from .markets_vocabulary_index import MarketsVocabularyIndex
from .markets_vocabulary_summary import MarketsVocabularySummary
from .markets_vocabulary_value import MarketsVocabularyValue
from .measurement_families import MeasurementFamilies
from .measurement_families_create_request import MeasurementFamiliesCreateRequest
from .measurement_families_filter import MeasurementFamiliesFilter
from .measurement_families_update_request import MeasurementFamiliesUpdateRequest
from .menu import Menu
from .menu_update_request import MenuUpdateRequest
from .menu_upsert_request import MenuUpsertRequest
from .message import Message
from .multi_search_entry import MultiSearchEntry
from .multi_search_request import MultiSearchRequest
from .multi_search_result import MultiSearchResult
from .mutation_request import MutationRequest
from .mutation_response import MutationResponse
from .number_range import NumberRange
from .order import Order
from .order_acknowledge_request import OrderAcknowledgeRequest
from .order_cancel_position import OrderCancelPosition
from .order_cancel_request import OrderCancelRequest
from .order_cancellation import OrderCancellation
from .order_cancellation_position import OrderCancellationPosition
from .order_comment import OrderComment
from .order_comment_create_request import OrderCommentCreateRequest
from .order_complete_request import OrderCompleteRequest
from .order_customer_rollup import OrderCustomerRollup
from .order_customer_rollup_request import OrderCustomerRollupRequest
from .order_customer_rollup_response import OrderCustomerRollupResponse
from .order_deleted import OrderDeleted
from .order_detail import OrderDetail
from .order_event import OrderEvent
from .order_hold_request import OrderHoldRequest
from .order_item import OrderItem
from .order_item_create_request import OrderItemCreateRequest
from .order_items_cancel_request import OrderItemsCancelRequest
from .order_list_create_request import OrderListCreateRequest
from .order_list_item import OrderListItem
from .order_list_item_input import OrderListItemInput
from .order_list_item_update_request import OrderListItemUpdateRequest
from .order_list_items_replace_request import OrderListItemsReplaceRequest
from .order_list_kind_create_request import OrderListKindCreateRequest
from .order_list_kind_make_default_request import OrderListKindMakeDefaultRequest
from .order_list_kind_row import OrderListKindRow
from .order_list_kind_update_request import OrderListKindUpdateRequest
from .order_list_skipped_position import OrderListSkippedPosition
from .order_list_summary import OrderListSummary
from .order_list_to_cart_request import OrderListToCartRequest
from .order_list_to_cart_result import OrderListToCartResult
from .order_list_to_order_request import OrderListToOrderRequest
from .order_list_to_order_result import OrderListToOrderResult
from .order_list_update_request import OrderListUpdateRequest
from .order_list_vocabulary import OrderListVocabulary
from .order_list_vocabulary_index import OrderListVocabularyIndex
from .order_list_vocabulary_value import OrderListVocabularyValue
from .order_list_with_items import OrderListWithItems
from .order_number_range_create_request import OrderNumberRangeCreateRequest
from .order_number_range_update_request import OrderNumberRangeUpdateRequest
from .order_number_ranges_seeded import OrderNumberRangesSeeded
from .order_page import OrderPage
from .order_payment_status_update_request import OrderPaymentStatusUpdateRequest
from .order_place_request import OrderPlaceRequest
from .order_placed import OrderPlaced
from .order_restock_position import OrderRestockPosition
from .order_return import OrderReturn
from .order_return_complete_request import OrderReturnCompleteRequest
from .order_return_completed import OrderReturnCompleted
from .order_return_create_request import OrderReturnCreateRequest
from .order_return_position import OrderReturnPosition
from .order_return_receive_request import OrderReturnReceiveRequest
from .order_return_reject_request import OrderReturnRejectRequest
from .order_returned_position import OrderReturnedPosition
from .order_shipment import OrderShipment
from .order_shipment_create_request import OrderShipmentCreateRequest
from .order_shipment_created import OrderShipmentCreated
from .order_shipment_item import OrderShipmentItem
from .order_shipment_position import OrderShipmentPosition
from .order_shippable import OrderShippable
from .order_shippable_order import OrderShippableOrder
from .order_shippable_position import OrderShippablePosition
from .order_unhold_request import OrderUnholdRequest
from .order_update_request import OrderUpdateRequest
from .order_vocabulary import OrderVocabulary
from .order_vocabulary_index import OrderVocabularyIndex
from .order_vocabulary_summary import OrderVocabularySummary
from .order_vocabulary_value import OrderVocabularyValue
from .organization import Organization
from .organization_activity_request import OrganizationActivityRequest
from .organization_create_request import OrganizationCreateRequest
from .organization_metrics import OrganizationMetrics
from .organization_metrics_freshness import OrganizationMetricsFreshness
from .organization_metrics_refresh_request import OrganizationMetricsRefreshRequest
from .organization_metrics_refresh_response import OrganizationMetricsRefreshResponse
from .organization_update_request import OrganizationUpdateRequest
from .page import Page
from .page_block_tree import PageBlockTree
from .page_comment_create_request import PageCommentCreateRequest
from .page_comment_item import PageCommentItem
from .page_comment_list import PageCommentList
from .page_comment_task_request import PageCommentTaskRequest
from .page_comment_update_request import PageCommentUpdateRequest
from .page_create_request import PageCreateRequest
from .page_history_request import PageHistoryRequest
from .page_library_item_update_request import PageLibraryItemUpdateRequest
from .page_menu_item import PageMenuItem
from .page_mutation_status_request import PageMutationStatusRequest
from .page_preview_grant_request import PagePreviewGrantRequest
from .page_publish_request import PagePublishRequest
from .page_revision_ref import PageRevisionRef
from .page_schedule_request import PageScheduleRequest
from .page_template_create_request import PageTemplateCreateRequest
from .page_template_update_request import PageTemplateUpdateRequest
from .page_translate_request import PageTranslateRequest
from .page_update_request import PageUpdateRequest
from .page_user_settings_request import PageUserSettingsRequest
from .pages_vocabulary import PagesVocabulary
from .pages_vocabulary_index import PagesVocabularyIndex
from .pages_vocabulary_ref import PagesVocabularyRef
from .pages_vocabulary_value import PagesVocabularyValue
from .payment import Payment
from .payment_create_request import PaymentCreateRequest
from .payment_eligibility_request import PaymentEligibilityRequest
from .payment_error_redact_request import PaymentErrorRedactRequest
from .payment_method import PaymentMethod
from .payment_method_create_request import PaymentMethodCreateRequest
from .payment_method_update_request import PaymentMethodUpdateRequest
from .payment_provider import PaymentProvider
from .payment_provider_create_request import PaymentProviderCreateRequest
from .payment_provider_update_request import PaymentProviderUpdateRequest
from .payment_term import PaymentTerm
from .payment_term_create_request import PaymentTermCreateRequest
from .payment_term_update_request import PaymentTermUpdateRequest
from .payment_transition_request import PaymentTransitionRequest
from .payment_vocabulary import PaymentVocabulary
from .payment_vocabulary_value import PaymentVocabularyValue
from .payment_webhook_ingest_request import PaymentWebhookIngestRequest
from .price_adjust_preview_row import PriceAdjustPreviewRow
from .price_deleted import PriceDeleted
from .price_entries_adjust_request import PriceEntriesAdjustRequest
from .price_entries_adjust_response import PriceEntriesAdjustResponse
from .price_entries_bulk_request import PriceEntriesBulkRequest
from .price_entries_bulk_response import PriceEntriesBulkResponse
from .price_entries_ladder_request import PriceEntriesLadderRequest
from .price_entries_ladder_response import PriceEntriesLadderResponse
from .price_entries_replace_request import PriceEntriesReplaceRequest
from .price_entries_replace_response import PriceEntriesReplaceResponse
from .price_entry import PriceEntry
from .price_entry_create_request import PriceEntryCreateRequest
from .price_entry_replace_item import PriceEntryReplaceItem
from .price_entry_update_request import PriceEntryUpdateRequest
from .price_list import PriceList
from .price_list_create_request import PriceListCreateRequest
from .price_list_defaults_response import PriceListDefaultsResponse
from .price_list_make_default_request import PriceListMakeDefaultRequest
from .price_list_make_default_response import PriceListMakeDefaultResponse
from .price_list_ref import PriceListRef
from .price_list_update_request import PriceListUpdateRequest
from .price_page import PricePage
from .price_resolve_basis import PriceResolveBasis
from .price_resolve_item import PriceResolveItem
from .price_resolve_request import PriceResolveRequest
from .price_resolve_response import PriceResolveResponse
from .price_tax_context import PriceTaxContext
from .price_tier import PriceTier
from .price_vocabulary import PriceVocabulary
from .price_vocabulary_index import PriceVocabularyIndex
from .price_vocabulary_ref import PriceVocabularyRef
from .price_vocabulary_value import PriceVocabularyValue
from .principal_resolve_request import PrincipalResolveRequest
from .product_associations import ProductAssociations
from .product_associations_create_request import ProductAssociationsCreateRequest
from .product_associations_filter import ProductAssociationsFilter
from .product_associations_update_request import ProductAssociationsUpdateRequest
from .product_categories import ProductCategories
from .product_categories_create_request import ProductCategoriesCreateRequest
from .product_categories_filter import ProductCategoriesFilter
from .product_categories_update_request import ProductCategoriesUpdateRequest
from .product_category_assign_request import ProductCategoryAssignRequest
from .product_completeness import ProductCompleteness
from .product_completeness_request import ProductCompletenessRequest
from .product_family_assign_request import ProductFamilyAssignRequest
from .product_grid_column import ProductGridColumn
from .product_grid_filter import ProductGridFilter
from .product_grid_row import ProductGridRow
from .product_label import ProductLabel
from .product_labels_request import ProductLabelsRequest
from .product_tax_ref import ProductTaxRef
from .products import Products
from .products_batch_request import ProductsBatchRequest
from .products_create_request import ProductsCreateRequest
from .products_filter import ProductsFilter
from .products_update_request import ProductsUpdateRequest
from .push_subscription import PushSubscription
from .reference_entities import ReferenceEntities
from .reference_entities_create_request import ReferenceEntitiesCreateRequest
from .reference_entities_filter import ReferenceEntitiesFilter
from .reference_entities_update_request import ReferenceEntitiesUpdateRequest
from .reference_entity_records import ReferenceEntityRecords
from .reference_entity_records_create_request import ReferenceEntityRecordsCreateRequest
from .reference_entity_records_filter import ReferenceEntityRecordsFilter
from .reference_entity_records_update_request import ReferenceEntityRecordsUpdateRequest
from .registration_approve_request import RegistrationApproveRequest
from .registration_reject_request import RegistrationRejectRequest
from .reorder_alert import ReorderAlert
from .reorder_alerts import ReorderAlerts
from .reorder_scan import ReorderScan
from .reorder_scan_emit import ReorderScanEmit
from .reorder_scan_request import ReorderScanRequest
from .reservation import Reservation
from .reservation_sweep_request import ReservationSweepRequest
from .reservation_sweep_result import ReservationSweepResult
from .reservations_filter import ReservationsFilter
from .resolved_price import ResolvedPrice
from .role_catalog_response import RoleCatalogResponse
from .role_permissions_request import RolePermissionsRequest
from .role_permissions_response import RolePermissionsResponse
from .roles_defaults_request import RolesDefaultsRequest
from .roles_defaults_response import RolesDefaultsResponse
from .search_hit import SearchHit
from .search_parameters import SearchParameters
from .search_result import SearchResult
from .seed_request import SeedRequest
from .seed_result import SeedResult
from .segment import Segment
from .segment_create_request import SegmentCreateRequest
from .segment_member import SegmentMember
from .segment_member_create_request import SegmentMemberCreateRequest
from .segment_member_update_request import SegmentMemberUpdateRequest
from .segment_rule_condition import SegmentRuleCondition
from .segment_rule_preview_request import SegmentRulePreviewRequest
from .segment_rule_preview_response import SegmentRulePreviewResponse
from .segment_rule_recompute_all_request import SegmentRuleRecomputeAllRequest
from .segment_rule_recompute_all_response import SegmentRuleRecomputeAllResponse
from .segment_rule_recompute_request import SegmentRuleRecomputeRequest
from .segment_rule_recompute_response import SegmentRuleRecomputeResponse
from .segment_rules import SegmentRules
from .segment_update_request import SegmentUpdateRequest
from .shipping_carrier import ShippingCarrier
from .shipping_carrier_catalog_entry import ShippingCarrierCatalogEntry
from .shipping_carrier_create_request import ShippingCarrierCreateRequest
from .shipping_carrier_update_request import ShippingCarrierUpdateRequest
from .shipping_delivery_estimate import ShippingDeliveryEstimate
from .shipping_method import ShippingMethod
from .shipping_method_create_request import ShippingMethodCreateRequest
from .shipping_method_update_request import ShippingMethodUpdateRequest
from .shipping_rate import ShippingRate
from .shipping_rate_tier import ShippingRateTier
from .shipping_rate_tier_create_request import ShippingRateTierCreateRequest
from .shipping_rate_tier_replace_item import ShippingRateTierReplaceItem
from .shipping_rate_tier_update_request import ShippingRateTierUpdateRequest
from .shipping_rate_tiers_ladder_request import ShippingRateTiersLadderRequest
from .shipping_rate_tiers_replace_request import ShippingRateTiersReplaceRequest
from .shipping_rates_basis import ShippingRatesBasis
from .shipping_rates_request import ShippingRatesRequest
from .shipping_service_level_create_request import ShippingServiceLevelCreateRequest
from .shipping_service_level_make_default_request import ShippingServiceLevelMakeDefaultRequest
from .shipping_service_level_row import ShippingServiceLevelRow
from .shipping_service_level_update_request import ShippingServiceLevelUpdateRequest
from .shipping_tax_class_usage import ShippingTaxClassUsage
from .shipping_tax_context import ShippingTaxContext
from .shipping_tracking_carrier import ShippingTrackingCarrier
from .shipping_tracking_request import ShippingTrackingRequest
from .shipping_vocabulary import ShippingVocabulary
from .shipping_vocabulary_index import ShippingVocabularyIndex
from .shipping_vocabulary_index_entry import ShippingVocabularyIndexEntry
from .shipping_vocabulary_value import ShippingVocabularyValue
from .shipping_weight_unit_create_request import ShippingWeightUnitCreateRequest
from .shipping_weight_unit_make_default_request import ShippingWeightUnitMakeDefaultRequest
from .shipping_weight_unit_row import ShippingWeightUnitRow
from .shipping_weight_unit_update_request import ShippingWeightUnitUpdateRequest
from .stock_level import StockLevel
from .stock_level_adjust_request import StockLevelAdjustRequest
from .stock_level_create_request import StockLevelCreateRequest
from .stock_level_update_request import StockLevelUpdateRequest
from .stock_levels_filter import StockLevelsFilter
from .stock_movement import StockMovement
from .stock_movements_filter import StockMovementsFilter
from .store_asset_request import StoreAssetRequest
from .suppression import Suppression
from .sync_history import SyncHistory
from .sync_rule_resource import SyncRuleResource
from .template import Template
from .tenant_config import TenantConfig
from .tenant_locale_keys import TenantLocaleKeys
from .tenant_locale_policy import TenantLocalePolicy
from .unauthenticated_response import UnauthenticatedResponse
from .validation_failed_response import ValidationFailedResponse
from .vocabulary import Vocabulary
from .vocabulary_index import VocabularyIndex
from .vocabulary_ref import VocabularyRef
from .vocabulary_value import VocabularyValue
from .algo_argon2 import AlgoArgon2
from .algo_bcrypt import AlgoBcrypt
from .algo_md5 import AlgoMd5
from .algo_phpass import AlgoPhpass
from .algo_scrypt import AlgoScrypt
from .algo_scrypt_modified import AlgoScryptModified
from .algo_sha import AlgoSha
from .attribute_boolean import AttributeBoolean
from .attribute_datetime import AttributeDatetime
from .attribute_email import AttributeEmail
from .attribute_enum import AttributeEnum
from .attribute_float import AttributeFloat
from .attribute_integer import AttributeInteger
from .attribute_ip import AttributeIp
from .attribute_line import AttributeLine
from .attribute_list import AttributeList
from .attribute_longtext import AttributeLongtext
from .attribute_mediumtext import AttributeMediumtext
from .attribute_point import AttributePoint
from .attribute_polygon import AttributePolygon
from .attribute_relationship import AttributeRelationship
from .attribute_string import AttributeString
from .attribute_text import AttributeText
from .attribute_url import AttributeUrl
from .attribute_varchar import AttributeVarchar
from .bucket import Bucket
from .collection2 import Collection2
from .collection_list2 import CollectionList2
from .column_boolean import ColumnBoolean
from .column_datetime import ColumnDatetime
from .column_email import ColumnEmail
from .column_enum import ColumnEnum
from .column_float import ColumnFloat
from .column_index import ColumnIndex
from .column_index_list import ColumnIndexList
from .column_integer import ColumnInteger
from .column_ip import ColumnIp
from .column_line import ColumnLine
from .column_list import ColumnList
from .column_longtext import ColumnLongtext
from .column_mediumtext import ColumnMediumtext
from .column_point import ColumnPoint
from .column_polygon import ColumnPolygon
from .column_relationship import ColumnRelationship
from .column_string import ColumnString
from .column_text import ColumnText
from .column_url import ColumnUrl
from .column_varchar import ColumnVarchar
from .continent import Continent
from .continent_list import ContinentList
from .country import Country
from .country_list import CountryList
from .currency import Currency
from .currency_list import CurrencyList
from .database import Database
from .database_list import DatabaseList
from .deployment import Deployment
from .deployment_list import DeploymentList
from .document import Document
from .document_list import DocumentList
from .execution import Execution
from .execution_list import ExecutionList
from .file import File
from .file_list import FileList
from .framework import Framework
from .framework_adapter import FrameworkAdapter
from .framework_list import FrameworkList
from .function import Function
from .function_list import FunctionList
from .headers import Headers
from .health_antivirus import HealthAntivirus
from .health_certificate import HealthCertificate
from .health_queue import HealthQueue
from .health_status import HealthStatus
from .health_status_list import HealthStatusList
from .health_time import HealthTime
from .identity import Identity
from .identity_list import IdentityList
from .index import Index
from .index_list import IndexList
from .jwt import Jwt
from .language import Language
from .language_list import LanguageList
from .locale import Locale
from .locale_code import LocaleCode
from .locale_code_list import LocaleCodeList
from .log import Log
from .log_list import LogList
from .membership import Membership
from .membership_list import MembershipList
from .message2 import Message2
from .message_list import MessageList
from .metric import Metric
from .mfa_challenge import MfaChallenge
from .mfa_factors import MfaFactors
from .mfa_recovery_codes import MfaRecoveryCodes
from .mfa_type import MfaType
from .phone import Phone
from .phone_list import PhoneList
from .preferences import Preferences
from .provider import Provider
from .provider_list import ProviderList
from .row import Row
from .row_list import RowList
from .runtime import Runtime
from .runtime_list import RuntimeList
from .session import Session
from .session_list import SessionList
from .site import Site
from .site_list import SiteList
from .specification import Specification
from .specification_list import SpecificationList
from .subscriber import Subscriber
from .subscriber_list import SubscriberList
from .table import Table
from .table_list import TableList
from .target import Target
from .target_list import TargetList
from .team import Team
from .team_list import TeamList
from .template_function import TemplateFunction
from .template_function_list import TemplateFunctionList
from .template_runtime import TemplateRuntime
from .template_variable import TemplateVariable
from .topic import Topic
from .topic_list import TopicList
from .transaction import Transaction
from .transaction_list import TransactionList
from .usage_function import UsageFunction
from .usage_functions import UsageFunctions
from .user import User
from .user_list import UserList
from .variable import Variable
from .variable_list import VariableList

__all__ = [
    'AppwriteModel',
    'Address',
    'AddressCreateRequest',
    'AddressTypeRow',
    'AddressTypeRowCreateRequest',
    'AddressTypeRowUpdateRequest',
    'AddressUpdateRequest',
    'AssetFamilies',
    'AssetFamiliesCreateRequest',
    'AssetFamiliesFilter',
    'AssetFamiliesUpdateRequest',
    'AssetResource',
    'Assets',
    'AssetsCreateRequest',
    'AssetsFilter',
    'AssetsUpdateRequest',
    'AssociationTypes',
    'AssociationTypesCreateRequest',
    'AssociationTypesFilter',
    'AssociationTypesUpdateRequest',
    'AttributeField',
    'AttributeFieldOption',
    'AttributeFieldStorage',
    'AttributeFieldValidation',
    'AttributeGroups',
    'AttributeGroupsCreateRequest',
    'AttributeGroupsFilter',
    'AttributeGroupsUpdateRequest',
    'AttributeOptions',
    'AttributeOptionsCreateRequest',
    'AttributeOptionsFilter',
    'AttributeOptionsUpdateRequest',
    'AttributeSchemaFamily',
    'AttributeSchemaGroup',
    'Attributes',
    'AttributesCreateRequest',
    'AttributesFilter',
    'AttributesUpdateRequest',
    'AuditEntry',
    'AuthLoginRequest',
    'AuthLoginResponse',
    'AuthLogoutRequest',
    'AuthMagicLinkConfirmRequest',
    'AuthMagicLinkConfirmResponse',
    'AuthMagicLinkRequest',
    'AuthMagicLinkResponse',
    'AuthMeRequest',
    'AuthMeResponse',
    'AuthMfaChallengeConfirmRequest',
    'AuthMfaChallengeConfirmResponse',
    'AuthMfaChallengeRequest',
    'AuthMfaChallengeResponse',
    'AuthOtpConfirmRequest',
    'AuthOtpConfirmResponse',
    'AuthOtpRequest',
    'AuthOtpResponse',
    'AuthRecoveryConfirmRequest',
    'AuthRecoveryConfirmResponse',
    'AuthRecoveryRequest',
    'AuthRecoveryResponse',
    'AuthRegisterRequest',
    'AuthRegisterResponse',
    'AuthSession',
    'AuthVerificationConfirmRequest',
    'AuthVerificationConfirmResponse',
    'AuthVerificationRequest',
    'AuthVerificationResponse',
    'Binding',
    'BulkJob',
    'BulkJobStatus',
    'BulkJobType',
    'Cart',
    'CartAbandonSweep',
    'CartClaimRequest',
    'CartConversion',
    'CartConversionPricing',
    'CartConversionReservation',
    'CartCreateRequest',
    'CartExport',
    'CartExportRequest',
    'CartImport',
    'CartImportRequest',
    'CartIoMapping',
    'CartIoMappingColumn',
    'CartItem',
    'CartItemCreateRequest',
    'CartItemSnapshot',
    'CartItemUpdateRequest',
    'CartItemsReplaceRequest',
    'CartMaintenanceRequest',
    'CartMaintenanceResult',
    'CartMergeIntoRequest',
    'CartMergeRequest',
    'CartMergeResult',
    'CartOrderRequest',
    'CartPurgeSweep',
    'CartUpdateRequest',
    'CartVocabulary',
    'CartVocabularyIndex',
    'CartVocabularyRef',
    'CartVocabularyValue',
    'Categories',
    'CategoriesCreateRequest',
    'CategoriesFilter',
    'CategoriesUpdateRequest',
    'CategoryRecomputeAllRequest',
    'CategoryRecomputeRequest',
    'CategoryRecomputeResult',
    'CategoryRecomputeSummary',
    'CategoryRuleCondition',
    'CategoryRuleSample',
    'CategoryRulesRequest',
    'Channel',
    'ChannelContext',
    'ChannelCreateRequest',
    'ChannelDefaults',
    'ChannelPolicy',
    'ChannelTypeCreateRequest',
    'ChannelTypeDefaults',
    'ChannelTypeRow',
    'ChannelTypeUpdateRequest',
    'ChannelUpdateRequest',
    'ChannelVisibility',
    'ChannelVisibilityCounts',
    'ChannelVisibilityDecision',
    'ChannelVisibilityItem',
    'ChannelVisibilityRequest',
    'ChannelVocabulary',
    'ChannelVocabularyIndex',
    'ChannelVocabularyRef',
    'ChannelVocabularyValue',
    'Collection',
    'CollectionField',
    'CollectionList',
    'Contact',
    'ContactActivityRequest',
    'ContactCreateRequest',
    'ContactEvent',
    'ContactEventKind',
    'ContactEventKindCreateRequest',
    'ContactEventKindUpdateRequest',
    'ContactInviteRequest',
    'ContactInviteResponse',
    'ContactPermissions',
    'ContactUpdateRequest',
    'CustomersDefaultsRequest',
    'CustomersDefaultsResponse',
    'DeliveryBlock',
    'DeliveryMenu',
    'DeliveryPage',
    'DeliveryPageRef',
    'EditorState',
    'EligiblePaymentMethod',
    'Error',
    'FacetCount',
    'Families',
    'FamiliesCreateRequest',
    'FamiliesFilter',
    'FamiliesUpdateRequest',
    'FamilyAttributes',
    'FamilyAttributesCreateRequest',
    'FamilyAttributesFilter',
    'FamilyAttributesUpdateRequest',
    'FamilyVariants',
    'FamilyVariantsCreateRequest',
    'FamilyVariantsFilter',
    'FamilyVariantsUpdateRequest',
    'FolderResource',
    'Form',
    'FormActionMapping',
    'FormCreateRequest',
    'FormDefaultsResult',
    'FormDeleteResult',
    'FormKitNode',
    'FormKitStepMarker',
    'FormListFilter',
    'FormPostSubmitAction',
    'FormSettings',
    'FormSubmission',
    'FormSubmissionCreateRequest',
    'FormSubmissionDeleteResult',
    'FormSubmissionListFilter',
    'FormSubmissionMetadata',
    'FormSubmissionPruneRequest',
    'FormSubmissionPruneResult',
    'FormSubmissionPruneSample',
    'FormSubmissionUpdateRequest',
    'FormUpdateRequest',
    'FormsPage',
    'FormsVocabulary',
    'FormsVocabularyIndex',
    'FormsVocabularySummary',
    'FormsVocabularyValue',
    'InventoryAdjustItem',
    'InventoryAdjustRequest',
    'InventoryAvailabilityItem',
    'InventoryAvailabilityRequest',
    'InventoryCommitRequest',
    'InventoryReceiveRequest',
    'InventoryReleaseRequest',
    'InventoryReserveRequest',
    'InventoryRestockRequest',
    'InventoryShipTo',
    'InventoryStockItem',
    'InventoryVocabulary',
    'InventoryVocabularyIndex',
    'IoEntity',
    'IoProfile',
    'IoProfileCreateRequest',
    'IoProfileFormat',
    'IoProfileResource',
    'IoProfileUpdateRequest',
    'ItemAvailability',
    'Layout',
    'LibraryItem',
    'LibraryTemplate',
    'LifecycleStage',
    'LifecycleStageCreateRequest',
    'LifecycleStageUpdateRequest',
    'Location',
    'LocationAvailability',
    'LocationCreateRequest',
    'LocationUpdateRequest',
    'LocationsFilter',
    'Market',
    'MarketBackfillAdded',
    'MarketBackfillKept',
    'MarketBackfillRequest',
    'MarketBackfillResult',
    'MarketBackfillSeeded',
    'MarketCloneCopied',
    'MarketCloneRequest',
    'MarketCloneResult',
    'MarketCloneSeeded',
    'MarketContext',
    'MarketCreateRequest',
    'MarketCurrency',
    'MarketCurrencyCreateRequest',
    'MarketCurrencyDeleted',
    'MarketCurrencyFilter',
    'MarketCurrencyList',
    'MarketCurrencyUpdateRequest',
    'MarketDefaultLocale',
    'MarketDeleted',
    'MarketFilter',
    'MarketList',
    'MarketLocale',
    'MarketLocaleCreateRequest',
    'MarketLocaleDeleted',
    'MarketLocaleFilter',
    'MarketLocaleKeys',
    'MarketLocaleList',
    'MarketLocalePolicy',
    'MarketLocaleUpdateRequest',
    'MarketMakeDefaultRequest',
    'MarketMakeDefaultResponse',
    'MarketPricing',
    'MarketReadiness',
    'MarketReadinessCheck',
    'MarketReadinessCounts',
    'MarketReadinessReport',
    'MarketReadinessSubject',
    'MarketRef',
    'MarketTaxClass',
    'MarketTaxClassCreateRequest',
    'MarketTaxClassDeleted',
    'MarketTaxClassFilter',
    'MarketTaxClassList',
    'MarketTaxClassUpdateRequest',
    'MarketUpdateRequest',
    'MarketsPage',
    'MarketsVocabulary',
    'MarketsVocabularyIndex',
    'MarketsVocabularySummary',
    'MarketsVocabularyValue',
    'MeasurementFamilies',
    'MeasurementFamiliesCreateRequest',
    'MeasurementFamiliesFilter',
    'MeasurementFamiliesUpdateRequest',
    'Menu',
    'MenuUpdateRequest',
    'MenuUpsertRequest',
    'Message',
    'MultiSearchEntry',
    'MultiSearchRequest',
    'MultiSearchResult',
    'MutationRequest',
    'MutationResponse',
    'NumberRange',
    'Order',
    'OrderAcknowledgeRequest',
    'OrderCancelPosition',
    'OrderCancelRequest',
    'OrderCancellation',
    'OrderCancellationPosition',
    'OrderComment',
    'OrderCommentCreateRequest',
    'OrderCompleteRequest',
    'OrderCustomerRollup',
    'OrderCustomerRollupRequest',
    'OrderCustomerRollupResponse',
    'OrderDeleted',
    'OrderDetail',
    'OrderEvent',
    'OrderHoldRequest',
    'OrderItem',
    'OrderItemCreateRequest',
    'OrderItemsCancelRequest',
    'OrderListCreateRequest',
    'OrderListItem',
    'OrderListItemInput',
    'OrderListItemUpdateRequest',
    'OrderListItemsReplaceRequest',
    'OrderListKindCreateRequest',
    'OrderListKindMakeDefaultRequest',
    'OrderListKindRow',
    'OrderListKindUpdateRequest',
    'OrderListSkippedPosition',
    'OrderListSummary',
    'OrderListToCartRequest',
    'OrderListToCartResult',
    'OrderListToOrderRequest',
    'OrderListToOrderResult',
    'OrderListUpdateRequest',
    'OrderListVocabulary',
    'OrderListVocabularyIndex',
    'OrderListVocabularyValue',
    'OrderListWithItems',
    'OrderNumberRangeCreateRequest',
    'OrderNumberRangeUpdateRequest',
    'OrderNumberRangesSeeded',
    'OrderPage',
    'OrderPaymentStatusUpdateRequest',
    'OrderPlaceRequest',
    'OrderPlaced',
    'OrderRestockPosition',
    'OrderReturn',
    'OrderReturnCompleteRequest',
    'OrderReturnCompleted',
    'OrderReturnCreateRequest',
    'OrderReturnPosition',
    'OrderReturnReceiveRequest',
    'OrderReturnRejectRequest',
    'OrderReturnedPosition',
    'OrderShipment',
    'OrderShipmentCreateRequest',
    'OrderShipmentCreated',
    'OrderShipmentItem',
    'OrderShipmentPosition',
    'OrderShippable',
    'OrderShippableOrder',
    'OrderShippablePosition',
    'OrderUnholdRequest',
    'OrderUpdateRequest',
    'OrderVocabulary',
    'OrderVocabularyIndex',
    'OrderVocabularySummary',
    'OrderVocabularyValue',
    'Organization',
    'OrganizationActivityRequest',
    'OrganizationCreateRequest',
    'OrganizationMetrics',
    'OrganizationMetricsFreshness',
    'OrganizationMetricsRefreshRequest',
    'OrganizationMetricsRefreshResponse',
    'OrganizationUpdateRequest',
    'Page',
    'PageBlockTree',
    'PageCommentCreateRequest',
    'PageCommentItem',
    'PageCommentList',
    'PageCommentTaskRequest',
    'PageCommentUpdateRequest',
    'PageCreateRequest',
    'PageHistoryRequest',
    'PageLibraryItemUpdateRequest',
    'PageMenuItem',
    'PageMutationStatusRequest',
    'PagePreviewGrantRequest',
    'PagePublishRequest',
    'PageRevisionRef',
    'PageScheduleRequest',
    'PageTemplateCreateRequest',
    'PageTemplateUpdateRequest',
    'PageTranslateRequest',
    'PageUpdateRequest',
    'PageUserSettingsRequest',
    'PagesVocabulary',
    'PagesVocabularyIndex',
    'PagesVocabularyRef',
    'PagesVocabularyValue',
    'Payment',
    'PaymentCreateRequest',
    'PaymentEligibilityRequest',
    'PaymentErrorRedactRequest',
    'PaymentMethod',
    'PaymentMethodCreateRequest',
    'PaymentMethodUpdateRequest',
    'PaymentProvider',
    'PaymentProviderCreateRequest',
    'PaymentProviderUpdateRequest',
    'PaymentTerm',
    'PaymentTermCreateRequest',
    'PaymentTermUpdateRequest',
    'PaymentTransitionRequest',
    'PaymentVocabulary',
    'PaymentVocabularyValue',
    'PaymentWebhookIngestRequest',
    'PriceAdjustPreviewRow',
    'PriceDeleted',
    'PriceEntriesAdjustRequest',
    'PriceEntriesAdjustResponse',
    'PriceEntriesBulkRequest',
    'PriceEntriesBulkResponse',
    'PriceEntriesLadderRequest',
    'PriceEntriesLadderResponse',
    'PriceEntriesReplaceRequest',
    'PriceEntriesReplaceResponse',
    'PriceEntry',
    'PriceEntryCreateRequest',
    'PriceEntryReplaceItem',
    'PriceEntryUpdateRequest',
    'PriceList',
    'PriceListCreateRequest',
    'PriceListDefaultsResponse',
    'PriceListMakeDefaultRequest',
    'PriceListMakeDefaultResponse',
    'PriceListRef',
    'PriceListUpdateRequest',
    'PricePage',
    'PriceResolveBasis',
    'PriceResolveItem',
    'PriceResolveRequest',
    'PriceResolveResponse',
    'PriceTaxContext',
    'PriceTier',
    'PriceVocabulary',
    'PriceVocabularyIndex',
    'PriceVocabularyRef',
    'PriceVocabularyValue',
    'PrincipalResolveRequest',
    'ProductAssociations',
    'ProductAssociationsCreateRequest',
    'ProductAssociationsFilter',
    'ProductAssociationsUpdateRequest',
    'ProductCategories',
    'ProductCategoriesCreateRequest',
    'ProductCategoriesFilter',
    'ProductCategoriesUpdateRequest',
    'ProductCategoryAssignRequest',
    'ProductCompleteness',
    'ProductCompletenessRequest',
    'ProductFamilyAssignRequest',
    'ProductGridColumn',
    'ProductGridFilter',
    'ProductGridRow',
    'ProductLabel',
    'ProductLabelsRequest',
    'ProductTaxRef',
    'Products',
    'ProductsBatchRequest',
    'ProductsCreateRequest',
    'ProductsFilter',
    'ProductsUpdateRequest',
    'PushSubscription',
    'ReferenceEntities',
    'ReferenceEntitiesCreateRequest',
    'ReferenceEntitiesFilter',
    'ReferenceEntitiesUpdateRequest',
    'ReferenceEntityRecords',
    'ReferenceEntityRecordsCreateRequest',
    'ReferenceEntityRecordsFilter',
    'ReferenceEntityRecordsUpdateRequest',
    'RegistrationApproveRequest',
    'RegistrationRejectRequest',
    'ReorderAlert',
    'ReorderAlerts',
    'ReorderScan',
    'ReorderScanEmit',
    'ReorderScanRequest',
    'Reservation',
    'ReservationSweepRequest',
    'ReservationSweepResult',
    'ReservationsFilter',
    'ResolvedPrice',
    'RoleCatalogResponse',
    'RolePermissionsRequest',
    'RolePermissionsResponse',
    'RolesDefaultsRequest',
    'RolesDefaultsResponse',
    'SearchHit',
    'SearchParameters',
    'SearchResult',
    'SeedRequest',
    'SeedResult',
    'Segment',
    'SegmentCreateRequest',
    'SegmentMember',
    'SegmentMemberCreateRequest',
    'SegmentMemberUpdateRequest',
    'SegmentRuleCondition',
    'SegmentRulePreviewRequest',
    'SegmentRulePreviewResponse',
    'SegmentRuleRecomputeAllRequest',
    'SegmentRuleRecomputeAllResponse',
    'SegmentRuleRecomputeRequest',
    'SegmentRuleRecomputeResponse',
    'SegmentRules',
    'SegmentUpdateRequest',
    'ShippingCarrier',
    'ShippingCarrierCatalogEntry',
    'ShippingCarrierCreateRequest',
    'ShippingCarrierUpdateRequest',
    'ShippingDeliveryEstimate',
    'ShippingMethod',
    'ShippingMethodCreateRequest',
    'ShippingMethodUpdateRequest',
    'ShippingRate',
    'ShippingRateTier',
    'ShippingRateTierCreateRequest',
    'ShippingRateTierReplaceItem',
    'ShippingRateTierUpdateRequest',
    'ShippingRateTiersLadderRequest',
    'ShippingRateTiersReplaceRequest',
    'ShippingRatesBasis',
    'ShippingRatesRequest',
    'ShippingServiceLevelCreateRequest',
    'ShippingServiceLevelMakeDefaultRequest',
    'ShippingServiceLevelRow',
    'ShippingServiceLevelUpdateRequest',
    'ShippingTaxClassUsage',
    'ShippingTaxContext',
    'ShippingTrackingCarrier',
    'ShippingTrackingRequest',
    'ShippingVocabulary',
    'ShippingVocabularyIndex',
    'ShippingVocabularyIndexEntry',
    'ShippingVocabularyValue',
    'ShippingWeightUnitCreateRequest',
    'ShippingWeightUnitMakeDefaultRequest',
    'ShippingWeightUnitRow',
    'ShippingWeightUnitUpdateRequest',
    'StockLevel',
    'StockLevelAdjustRequest',
    'StockLevelCreateRequest',
    'StockLevelUpdateRequest',
    'StockLevelsFilter',
    'StockMovement',
    'StockMovementsFilter',
    'StoreAssetRequest',
    'Suppression',
    'SyncHistory',
    'SyncRuleResource',
    'Template',
    'TenantConfig',
    'TenantLocaleKeys',
    'TenantLocalePolicy',
    'UnauthenticatedResponse',
    'ValidationFailedResponse',
    'Vocabulary',
    'VocabularyIndex',
    'VocabularyRef',
    'VocabularyValue',
    'AlgoArgon2',
    'AlgoBcrypt',
    'AlgoMd5',
    'AlgoPhpass',
    'AlgoScrypt',
    'AlgoScryptModified',
    'AlgoSha',
    'AttributeBoolean',
    'AttributeDatetime',
    'AttributeEmail',
    'AttributeEnum',
    'AttributeFloat',
    'AttributeInteger',
    'AttributeIp',
    'AttributeLine',
    'AttributeList',
    'AttributeLongtext',
    'AttributeMediumtext',
    'AttributePoint',
    'AttributePolygon',
    'AttributeRelationship',
    'AttributeString',
    'AttributeText',
    'AttributeUrl',
    'AttributeVarchar',
    'Bucket',
    'Collection2',
    'CollectionList2',
    'ColumnBoolean',
    'ColumnDatetime',
    'ColumnEmail',
    'ColumnEnum',
    'ColumnFloat',
    'ColumnIndex',
    'ColumnIndexList',
    'ColumnInteger',
    'ColumnIp',
    'ColumnLine',
    'ColumnList',
    'ColumnLongtext',
    'ColumnMediumtext',
    'ColumnPoint',
    'ColumnPolygon',
    'ColumnRelationship',
    'ColumnString',
    'ColumnText',
    'ColumnUrl',
    'ColumnVarchar',
    'Continent',
    'ContinentList',
    'Country',
    'CountryList',
    'Currency',
    'CurrencyList',
    'Database',
    'DatabaseList',
    'Deployment',
    'DeploymentList',
    'Document',
    'DocumentList',
    'Execution',
    'ExecutionList',
    'File',
    'FileList',
    'Framework',
    'FrameworkAdapter',
    'FrameworkList',
    'Function',
    'FunctionList',
    'Headers',
    'HealthAntivirus',
    'HealthCertificate',
    'HealthQueue',
    'HealthStatus',
    'HealthStatusList',
    'HealthTime',
    'Identity',
    'IdentityList',
    'Index',
    'IndexList',
    'Jwt',
    'Language',
    'LanguageList',
    'Locale',
    'LocaleCode',
    'LocaleCodeList',
    'Log',
    'LogList',
    'Membership',
    'MembershipList',
    'Message2',
    'MessageList',
    'Metric',
    'MfaChallenge',
    'MfaFactors',
    'MfaRecoveryCodes',
    'MfaType',
    'Phone',
    'PhoneList',
    'Preferences',
    'Provider',
    'ProviderList',
    'Row',
    'RowList',
    'Runtime',
    'RuntimeList',
    'Session',
    'SessionList',
    'Site',
    'SiteList',
    'Specification',
    'SpecificationList',
    'Subscriber',
    'SubscriberList',
    'Table',
    'TableList',
    'Target',
    'TargetList',
    'Team',
    'TeamList',
    'TemplateFunction',
    'TemplateFunctionList',
    'TemplateRuntime',
    'TemplateVariable',
    'Topic',
    'TopicList',
    'Transaction',
    'TransactionList',
    'UsageFunction',
    'UsageFunctions',
    'User',
    'UserList',
    'Variable',
    'VariableList',
]
