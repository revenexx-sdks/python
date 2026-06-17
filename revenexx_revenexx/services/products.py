from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.products import Products as ProductsModel;
from ..models.asset_families import AssetFamilies;
from ..models.assets import Assets;
from ..models.association_types import AssociationTypes;
from ..models.attribute_groups import AttributeGroups;
from ..models.attribute_options import AttributeOptions;
from ..models.attributes import Attributes;
from ..models.categories import Categories;
from ..models.families import Families;
from ..models.family_attributes import FamilyAttributes;
from ..models.family_variants import FamilyVariants;
from ..models.measurement_families import MeasurementFamilies;
from ..models.product_associations import ProductAssociations;
from ..models.product_categories import ProductCategories;
from ..models.reference_entities import ReferenceEntities;
from ..models.reference_entity_records import ReferenceEntityRecords;

class Products(Service):

    def __init__(self, client) -> None:
        super(Products, self).__init__(client)

    def products_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_create(
        self,
        sku: str,
        attribute_values: Optional[Dict[str, Any]] = None,
        completeness: Optional[Dict[str, Any]] = None,
        deleted_at: Optional[str] = None,
        enabled: Optional[bool] = None,
        family_id: Optional[str] = None,
        family_variant_id: Optional[str] = None,
        kind: Optional[str] = None,
        parent_id: Optional[str] = None,
        quantified_associations: Optional[Dict[str, Any]] = None,
        tax_class: Optional[str] = None
    ) -> ProductsModel:
        """
        

        Parameters
        ----------
        sku : str
            
        attribute_values : Optional[Dict[str, Any]]
            
        completeness : Optional[Dict[str, Any]]
            
        deleted_at : Optional[str]
            
        enabled : Optional[bool]
            
        family_id : Optional[str]
            
        family_variant_id : Optional[str]
            
        kind : Optional[str]
            
        parent_id : Optional[str]
            
        quantified_associations : Optional[Dict[str, Any]]
            
        tax_class : Optional[str]
            
        
        Returns
        -------
        ProductsModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products'
        api_params = {}
        if sku is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "sku"')


        if attribute_values is not None:
            api_params['attribute_values'] = self._normalize_value(attribute_values)
        api_params['completeness'] = self._normalize_value(completeness)
        api_params['deleted_at'] = self._normalize_value(deleted_at)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['family_id'] = self._normalize_value(family_id)
        api_params['family_variant_id'] = self._normalize_value(family_variant_id)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        api_params['parent_id'] = self._normalize_value(parent_id)
        api_params['quantified_associations'] = self._normalize_value(quantified_associations)
        api_params['sku'] = self._normalize_value(sku)
        api_params['tax_class'] = self._normalize_value(tax_class)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProductsModel)


    def products_asset_families_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/asset_families'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_asset_families_create(
        self,
        code: str,
        labels: Optional[Dict[str, Any]] = None,
        naming_convention: Optional[Dict[str, Any]] = None
    ) -> AssetFamilies:
        """
        

        Parameters
        ----------
        code : str
            
        labels : Optional[Dict[str, Any]]
            
        naming_convention : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        AssetFamilies
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/asset_families'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        api_params['naming_convention'] = self._normalize_value(naming_convention)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AssetFamilies)


    def products_asset_families_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/asset_families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_asset_families_get(
        self,
        id: str
    ) -> AssetFamilies:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        AssetFamilies
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/asset_families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=AssetFamilies)


    def products_asset_families_update(
        self,
        id: str,
        code: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        naming_convention: Optional[Dict[str, Any]] = None
    ) -> AssetFamilies:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        naming_convention : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        AssetFamilies
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/asset_families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        api_params['naming_convention'] = self._normalize_value(naming_convention)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AssetFamilies)


    def products_assets_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/assets'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_assets_create(
        self,
        asset_family_id: str,
        code: str,
        attribute_values: Optional[Dict[str, Any]] = None,
        media_uuid: Optional[str] = None
    ) -> Assets:
        """
        

        Parameters
        ----------
        asset_family_id : str
            
        code : str
            
        attribute_values : Optional[Dict[str, Any]]
            
        media_uuid : Optional[str]
            
        
        Returns
        -------
        Assets
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/assets'
        api_params = {}
        if asset_family_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "asset_family_id"')

        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['asset_family_id'] = self._normalize_value(asset_family_id)
        if attribute_values is not None:
            api_params['attribute_values'] = self._normalize_value(attribute_values)
        api_params['code'] = self._normalize_value(code)
        api_params['media_uuid'] = self._normalize_value(media_uuid)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Assets)


    def products_assets_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/assets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_assets_get(
        self,
        id: str
    ) -> Assets:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Assets
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/assets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Assets)


    def products_assets_update(
        self,
        id: str,
        asset_family_id: Optional[str] = None,
        attribute_values: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        media_uuid: Optional[str] = None
    ) -> Assets:
        """
        

        Parameters
        ----------
        id : str
            
        asset_family_id : Optional[str]
            
        attribute_values : Optional[Dict[str, Any]]
            
        code : Optional[str]
            
        media_uuid : Optional[str]
            
        
        Returns
        -------
        Assets
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/assets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if asset_family_id is not None:
            api_params['asset_family_id'] = self._normalize_value(asset_family_id)
        if attribute_values is not None:
            api_params['attribute_values'] = self._normalize_value(attribute_values)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['media_uuid'] = self._normalize_value(media_uuid)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Assets)


    def products_association_types_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/association_types'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_association_types_create(
        self,
        code: str,
        is_quantified: Optional[bool] = None,
        is_two_way: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> AssociationTypes:
        """
        

        Parameters
        ----------
        code : str
            
        is_quantified : Optional[bool]
            
        is_two_way : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        AssociationTypes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/association_types'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['code'] = self._normalize_value(code)
        if is_quantified is not None:
            api_params['is_quantified'] = self._normalize_value(is_quantified)
        if is_two_way is not None:
            api_params['is_two_way'] = self._normalize_value(is_two_way)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AssociationTypes)


    def products_association_types_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/association_types/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_association_types_get(
        self,
        id: str
    ) -> AssociationTypes:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        AssociationTypes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/association_types/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=AssociationTypes)


    def products_association_types_update(
        self,
        id: str,
        code: Optional[str] = None,
        is_quantified: Optional[bool] = None,
        is_two_way: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> AssociationTypes:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        is_quantified : Optional[bool]
            
        is_two_way : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        AssociationTypes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/association_types/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if is_quantified is not None:
            api_params['is_quantified'] = self._normalize_value(is_quantified)
        if is_two_way is not None:
            api_params['is_two_way'] = self._normalize_value(is_two_way)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AssociationTypes)


    def products_attribute_groups_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_groups'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_attribute_groups_create(
        self,
        code: str,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None
    ) -> AttributeGroups:
        """
        

        Parameters
        ----------
        code : str
            
        labels : Optional[Dict[str, Any]]
            
        position : Optional[float]
            
        
        Returns
        -------
        AttributeGroups
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_groups'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeGroups)


    def products_attribute_groups_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_groups/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_attribute_groups_get(
        self,
        id: str
    ) -> AttributeGroups:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        AttributeGroups
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_groups/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=AttributeGroups)


    def products_attribute_groups_update(
        self,
        id: str,
        code: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None
    ) -> AttributeGroups:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        position : Optional[float]
            
        
        Returns
        -------
        AttributeGroups
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_groups/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeGroups)


    def products_attribute_options_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_options'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_attribute_options_create(
        self,
        attribute_id: str,
        code: str,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        swatch: Optional[Dict[str, Any]] = None
    ) -> AttributeOptions:
        """
        

        Parameters
        ----------
        attribute_id : str
            
        code : str
            
        labels : Optional[Dict[str, Any]]
            
        position : Optional[float]
            
        swatch : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        AttributeOptions
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_options'
        api_params = {}
        if attribute_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "attribute_id"')

        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['attribute_id'] = self._normalize_value(attribute_id)
        api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['swatch'] = self._normalize_value(swatch)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeOptions)


    def products_attribute_options_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_options/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_attribute_options_get(
        self,
        id: str
    ) -> AttributeOptions:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        AttributeOptions
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_options/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=AttributeOptions)


    def products_attribute_options_update(
        self,
        id: str,
        attribute_id: Optional[str] = None,
        code: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        swatch: Optional[Dict[str, Any]] = None
    ) -> AttributeOptions:
        """
        

        Parameters
        ----------
        id : str
            
        attribute_id : Optional[str]
            
        code : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        position : Optional[float]
            
        swatch : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        AttributeOptions
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attribute_options/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if attribute_id is not None:
            api_params['attribute_id'] = self._normalize_value(attribute_id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['swatch'] = self._normalize_value(swatch)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeOptions)


    def products_attributes_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attributes'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_attributes_create(
        self,
        code: str,
        type: str,
        config: Optional[Dict[str, Any]] = None,
        entity_ref: Optional[str] = None,
        entity_type: Optional[str] = None,
        group_id: Optional[str] = None,
        is_filterable: Optional[bool] = None,
        is_unique: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        localizable: Optional[bool] = None,
        position: Optional[float] = None,
        scopable: Optional[bool] = None,
        usable_in_grid: Optional[bool] = None,
        validation: Optional[Dict[str, Any]] = None
    ) -> Attributes:
        """
        

        Parameters
        ----------
        code : str
            
        type : str
            
        config : Optional[Dict[str, Any]]
            
        entity_ref : Optional[str]
            
        entity_type : Optional[str]
            
        group_id : Optional[str]
            
        is_filterable : Optional[bool]
            
        is_unique : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            
        localizable : Optional[bool]
            
        position : Optional[float]
            
        scopable : Optional[bool]
            
        usable_in_grid : Optional[bool]
            
        validation : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        Attributes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attributes'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if type is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "type"')


        api_params['code'] = self._normalize_value(code)
        api_params['config'] = self._normalize_value(config)
        api_params['entity_ref'] = self._normalize_value(entity_ref)
        if entity_type is not None:
            api_params['entity_type'] = self._normalize_value(entity_type)
        api_params['group_id'] = self._normalize_value(group_id)
        if is_filterable is not None:
            api_params['is_filterable'] = self._normalize_value(is_filterable)
        if is_unique is not None:
            api_params['is_unique'] = self._normalize_value(is_unique)
        api_params['labels'] = self._normalize_value(labels)
        if localizable is not None:
            api_params['localizable'] = self._normalize_value(localizable)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if scopable is not None:
            api_params['scopable'] = self._normalize_value(scopable)
        api_params['type'] = self._normalize_value(type)
        if usable_in_grid is not None:
            api_params['usable_in_grid'] = self._normalize_value(usable_in_grid)
        api_params['validation'] = self._normalize_value(validation)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Attributes)


    def products_attributes_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attributes/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_attributes_get(
        self,
        id: str
    ) -> Attributes:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Attributes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attributes/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Attributes)


    def products_attributes_update(
        self,
        id: str,
        code: Optional[str] = None,
        config: Optional[Dict[str, Any]] = None,
        entity_ref: Optional[str] = None,
        entity_type: Optional[str] = None,
        group_id: Optional[str] = None,
        is_filterable: Optional[bool] = None,
        is_unique: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        localizable: Optional[bool] = None,
        position: Optional[float] = None,
        scopable: Optional[bool] = None,
        type: Optional[str] = None,
        usable_in_grid: Optional[bool] = None,
        validation: Optional[Dict[str, Any]] = None
    ) -> Attributes:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        config : Optional[Dict[str, Any]]
            
        entity_ref : Optional[str]
            
        entity_type : Optional[str]
            
        group_id : Optional[str]
            
        is_filterable : Optional[bool]
            
        is_unique : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            
        localizable : Optional[bool]
            
        position : Optional[float]
            
        scopable : Optional[bool]
            
        type : Optional[str]
            
        usable_in_grid : Optional[bool]
            
        validation : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        Attributes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/attributes/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['config'] = self._normalize_value(config)
        api_params['entity_ref'] = self._normalize_value(entity_ref)
        if entity_type is not None:
            api_params['entity_type'] = self._normalize_value(entity_type)
        api_params['group_id'] = self._normalize_value(group_id)
        if is_filterable is not None:
            api_params['is_filterable'] = self._normalize_value(is_filterable)
        if is_unique is not None:
            api_params['is_unique'] = self._normalize_value(is_unique)
        api_params['labels'] = self._normalize_value(labels)
        if localizable is not None:
            api_params['localizable'] = self._normalize_value(localizable)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if scopable is not None:
            api_params['scopable'] = self._normalize_value(scopable)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if usable_in_grid is not None:
            api_params['usable_in_grid'] = self._normalize_value(usable_in_grid)
        api_params['validation'] = self._normalize_value(validation)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Attributes)


    def products_batch(
        self,
        ids: Optional[List[str]] = None,
        skus: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        ids : Optional[List[str]]
            
        skus : Optional[List[str]]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/batch'
        api_params = {}

        if ids is not None:
            api_params['ids'] = self._normalize_value(ids)
        if skus is not None:
            api_params['skus'] = self._normalize_value(skus)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def products_categories_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/categories'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_categories_create(
        self,
        code: str,
        labels: Optional[Dict[str, Any]] = None,
        parent_id: Optional[str] = None,
        path: Optional[str] = None,
        position: Optional[float] = None,
        values: Optional[Dict[str, Any]] = None
    ) -> Categories:
        """
        

        Parameters
        ----------
        code : str
            
        labels : Optional[Dict[str, Any]]
            
        parent_id : Optional[str]
            
        path : Optional[str]
            
        position : Optional[float]
            
        values : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        Categories
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/categories'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        api_params['parent_id'] = self._normalize_value(parent_id)
        api_params['path'] = self._normalize_value(path)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['values'] = self._normalize_value(values)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Categories)


    def products_categories_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/categories/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_categories_get(
        self,
        id: str
    ) -> Categories:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Categories
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/categories/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Categories)


    def products_categories_update(
        self,
        id: str,
        code: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        parent_id: Optional[str] = None,
        path: Optional[str] = None,
        position: Optional[float] = None,
        values: Optional[Dict[str, Any]] = None
    ) -> Categories:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        parent_id : Optional[str]
            
        path : Optional[str]
            
        position : Optional[float]
            
        values : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        Categories
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/categories/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        api_params['parent_id'] = self._normalize_value(parent_id)
        api_params['path'] = self._normalize_value(path)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['values'] = self._normalize_value(values)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Categories)


    def products_families_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/families'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_families_create(
        self,
        code: str,
        image_attribute: Optional[str] = None,
        label_attribute: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> Families:
        """
        

        Parameters
        ----------
        code : str
            
        image_attribute : Optional[str]
            
        label_attribute : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        Families
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/families'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['code'] = self._normalize_value(code)
        api_params['image_attribute'] = self._normalize_value(image_attribute)
        api_params['label_attribute'] = self._normalize_value(label_attribute)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Families)


    def products_families_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_families_get(
        self,
        id: str
    ) -> Families:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Families
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Families)


    def products_families_update(
        self,
        id: str,
        code: Optional[str] = None,
        image_attribute: Optional[str] = None,
        label_attribute: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> Families:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        image_attribute : Optional[str]
            
        label_attribute : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        Families
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['image_attribute'] = self._normalize_value(image_attribute)
        api_params['label_attribute'] = self._normalize_value(label_attribute)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Families)


    def products_family_attributes_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_attributes'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_family_attributes_create(
        self,
        attribute_id: str,
        family_id: str,
        is_required: Optional[bool] = None,
        position: Optional[float] = None,
        required_channels: Optional[Dict[str, Any]] = None
    ) -> FamilyAttributes:
        """
        

        Parameters
        ----------
        attribute_id : str
            
        family_id : str
            
        is_required : Optional[bool]
            
        position : Optional[float]
            
        required_channels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        FamilyAttributes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_attributes'
        api_params = {}
        if attribute_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "attribute_id"')

        if family_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "family_id"')


        api_params['attribute_id'] = self._normalize_value(attribute_id)
        api_params['family_id'] = self._normalize_value(family_id)
        if is_required is not None:
            api_params['is_required'] = self._normalize_value(is_required)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['required_channels'] = self._normalize_value(required_channels)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=FamilyAttributes)


    def products_family_attributes_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_attributes/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_family_attributes_get(
        self,
        id: str
    ) -> FamilyAttributes:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        FamilyAttributes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_attributes/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=FamilyAttributes)


    def products_family_attributes_update(
        self,
        id: str,
        attribute_id: Optional[str] = None,
        family_id: Optional[str] = None,
        is_required: Optional[bool] = None,
        position: Optional[float] = None,
        required_channels: Optional[Dict[str, Any]] = None
    ) -> FamilyAttributes:
        """
        

        Parameters
        ----------
        id : str
            
        attribute_id : Optional[str]
            
        family_id : Optional[str]
            
        is_required : Optional[bool]
            
        position : Optional[float]
            
        required_channels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        FamilyAttributes
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_attributes/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if attribute_id is not None:
            api_params['attribute_id'] = self._normalize_value(attribute_id)
        if family_id is not None:
            api_params['family_id'] = self._normalize_value(family_id)
        if is_required is not None:
            api_params['is_required'] = self._normalize_value(is_required)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['required_channels'] = self._normalize_value(required_channels)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=FamilyAttributes)


    def products_family_variants_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_variants'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_family_variants_create(
        self,
        code: str,
        family_id: str,
        axes: Optional[Dict[str, Any]] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> FamilyVariants:
        """
        

        Parameters
        ----------
        code : str
            
        family_id : str
            
        axes : Optional[Dict[str, Any]]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        FamilyVariants
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_variants'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if family_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "family_id"')


        api_params['axes'] = self._normalize_value(axes)
        api_params['code'] = self._normalize_value(code)
        api_params['family_id'] = self._normalize_value(family_id)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=FamilyVariants)


    def products_family_variants_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_variants/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_family_variants_get(
        self,
        id: str
    ) -> FamilyVariants:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        FamilyVariants
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_variants/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=FamilyVariants)


    def products_family_variants_update(
        self,
        id: str,
        axes: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        family_id: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> FamilyVariants:
        """
        

        Parameters
        ----------
        id : str
            
        axes : Optional[Dict[str, Any]]
            
        code : Optional[str]
            
        family_id : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        FamilyVariants
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/family_variants/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['axes'] = self._normalize_value(axes)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if family_id is not None:
            api_params['family_id'] = self._normalize_value(family_id)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=FamilyVariants)


    def products_measurement_families_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/measurement_families'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_measurement_families_create(
        self,
        code: str,
        standard_unit: str,
        labels: Optional[Dict[str, Any]] = None,
        units: Optional[Dict[str, Any]] = None
    ) -> MeasurementFamilies:
        """
        

        Parameters
        ----------
        code : str
            
        standard_unit : str
            
        labels : Optional[Dict[str, Any]]
            
        units : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        MeasurementFamilies
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/measurement_families'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if standard_unit is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "standard_unit"')


        api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        api_params['standard_unit'] = self._normalize_value(standard_unit)
        api_params['units'] = self._normalize_value(units)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MeasurementFamilies)


    def products_measurement_families_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/measurement_families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_measurement_families_get(
        self,
        id: str
    ) -> MeasurementFamilies:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        MeasurementFamilies
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/measurement_families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MeasurementFamilies)


    def products_measurement_families_update(
        self,
        id: str,
        code: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        standard_unit: Optional[str] = None,
        units: Optional[Dict[str, Any]] = None
    ) -> MeasurementFamilies:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        standard_unit : Optional[str]
            
        units : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        MeasurementFamilies
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/measurement_families/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if standard_unit is not None:
            api_params['standard_unit'] = self._normalize_value(standard_unit)
        api_params['units'] = self._normalize_value(units)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MeasurementFamilies)


    def products_product_associations_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_associations'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_product_associations_create(
        self,
        association_type_id: str,
        product_id: str,
        target_product_id: str,
        position: Optional[float] = None,
        quantity: Optional[float] = None
    ) -> ProductAssociations:
        """
        

        Parameters
        ----------
        association_type_id : str
            
        product_id : str
            
        target_product_id : str
            
        position : Optional[float]
            
        quantity : Optional[float]
            
        
        Returns
        -------
        ProductAssociations
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_associations'
        api_params = {}
        if association_type_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "association_type_id"')

        if product_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "product_id"')

        if target_product_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "target_product_id"')


        api_params['association_type_id'] = self._normalize_value(association_type_id)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['target_product_id'] = self._normalize_value(target_product_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProductAssociations)


    def products_product_associations_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_associations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_product_associations_get(
        self,
        id: str
    ) -> ProductAssociations:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ProductAssociations
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_associations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ProductAssociations)


    def products_product_associations_update(
        self,
        id: str,
        association_type_id: Optional[str] = None,
        position: Optional[float] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        target_product_id: Optional[str] = None
    ) -> ProductAssociations:
        """
        

        Parameters
        ----------
        id : str
            
        association_type_id : Optional[str]
            
        position : Optional[float]
            
        product_id : Optional[str]
            
        quantity : Optional[float]
            
        target_product_id : Optional[str]
            
        
        Returns
        -------
        ProductAssociations
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_associations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if association_type_id is not None:
            api_params['association_type_id'] = self._normalize_value(association_type_id)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if product_id is not None:
            api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        if target_product_id is not None:
            api_params['target_product_id'] = self._normalize_value(target_product_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProductAssociations)


    def products_product_categories_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_categories'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_product_categories_create(
        self,
        category_id: str,
        product_id: str,
        position: Optional[float] = None
    ) -> ProductCategories:
        """
        

        Parameters
        ----------
        category_id : str
            
        product_id : str
            
        position : Optional[float]
            
        
        Returns
        -------
        ProductCategories
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_categories'
        api_params = {}
        if category_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "category_id"')

        if product_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "product_id"')


        api_params['category_id'] = self._normalize_value(category_id)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['product_id'] = self._normalize_value(product_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProductCategories)


    def products_product_categories_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_categories/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_product_categories_get(
        self,
        id: str
    ) -> ProductCategories:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ProductCategories
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_categories/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ProductCategories)


    def products_product_categories_update(
        self,
        id: str,
        category_id: Optional[str] = None,
        position: Optional[float] = None,
        product_id: Optional[str] = None
    ) -> ProductCategories:
        """
        

        Parameters
        ----------
        id : str
            
        category_id : Optional[str]
            
        position : Optional[float]
            
        product_id : Optional[str]
            
        
        Returns
        -------
        ProductCategories
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/product_categories/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if category_id is not None:
            api_params['category_id'] = self._normalize_value(category_id)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if product_id is not None:
            api_params['product_id'] = self._normalize_value(product_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProductCategories)


    def products_reference_entities_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entities'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_reference_entities_create(
        self,
        code: str,
        image: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> ReferenceEntities:
        """
        

        Parameters
        ----------
        code : str
            
        image : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        ReferenceEntities
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entities'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        api_params['code'] = self._normalize_value(code)
        api_params['image'] = self._normalize_value(image)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ReferenceEntities)


    def products_reference_entities_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entities/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_reference_entities_get(
        self,
        id: str
    ) -> ReferenceEntities:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ReferenceEntities
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entities/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ReferenceEntities)


    def products_reference_entities_update(
        self,
        id: str,
        code: Optional[str] = None,
        image: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> ReferenceEntities:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            
        image : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        ReferenceEntities
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entities/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['image'] = self._normalize_value(image)
        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ReferenceEntities)


    def products_reference_entity_records_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entity_records'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def products_reference_entity_records_create(
        self,
        code: str,
        reference_entity_id: str,
        attribute_values: Optional[Dict[str, Any]] = None,
        labels: Optional[Dict[str, Any]] = None
    ) -> ReferenceEntityRecords:
        """
        

        Parameters
        ----------
        code : str
            
        reference_entity_id : str
            
        attribute_values : Optional[Dict[str, Any]]
            
        labels : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        ReferenceEntityRecords
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entity_records'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if reference_entity_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "reference_entity_id"')


        if attribute_values is not None:
            api_params['attribute_values'] = self._normalize_value(attribute_values)
        api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        api_params['reference_entity_id'] = self._normalize_value(reference_entity_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ReferenceEntityRecords)


    def products_reference_entity_records_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entity_records/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_reference_entity_records_get(
        self,
        id: str
    ) -> ReferenceEntityRecords:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ReferenceEntityRecords
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entity_records/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ReferenceEntityRecords)


    def products_reference_entity_records_update(
        self,
        id: str,
        attribute_values: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        reference_entity_id: Optional[str] = None
    ) -> ReferenceEntityRecords:
        """
        

        Parameters
        ----------
        id : str
            
        attribute_values : Optional[Dict[str, Any]]
            
        code : Optional[str]
            
        labels : Optional[Dict[str, Any]]
            
        reference_entity_id : Optional[str]
            
        
        Returns
        -------
        ReferenceEntityRecords
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/reference_entity_records/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if attribute_values is not None:
            api_params['attribute_values'] = self._normalize_value(attribute_values)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if reference_entity_id is not None:
            api_params['reference_entity_id'] = self._normalize_value(reference_entity_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ReferenceEntityRecords)


    def products_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def products_get(
        self,
        id: str
    ) -> ProductsModel:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ProductsModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ProductsModel)


    def products_update(
        self,
        id: str,
        attribute_values: Optional[Dict[str, Any]] = None,
        completeness: Optional[Dict[str, Any]] = None,
        deleted_at: Optional[str] = None,
        enabled: Optional[bool] = None,
        family_id: Optional[str] = None,
        family_variant_id: Optional[str] = None,
        kind: Optional[str] = None,
        parent_id: Optional[str] = None,
        quantified_associations: Optional[Dict[str, Any]] = None,
        sku: Optional[str] = None,
        tax_class: Optional[str] = None
    ) -> ProductsModel:
        """
        

        Parameters
        ----------
        id : str
            
        attribute_values : Optional[Dict[str, Any]]
            
        completeness : Optional[Dict[str, Any]]
            
        deleted_at : Optional[str]
            
        enabled : Optional[bool]
            
        family_id : Optional[str]
            
        family_variant_id : Optional[str]
            
        kind : Optional[str]
            
        parent_id : Optional[str]
            
        quantified_associations : Optional[Dict[str, Any]]
            
        sku : Optional[str]
            
        tax_class : Optional[str]
            
        
        Returns
        -------
        ProductsModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/products/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if attribute_values is not None:
            api_params['attribute_values'] = self._normalize_value(attribute_values)
        api_params['completeness'] = self._normalize_value(completeness)
        api_params['deleted_at'] = self._normalize_value(deleted_at)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['family_id'] = self._normalize_value(family_id)
        api_params['family_variant_id'] = self._normalize_value(family_variant_id)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        api_params['parent_id'] = self._normalize_value(parent_id)
        api_params['quantified_associations'] = self._normalize_value(quantified_associations)
        if sku is not None:
            api_params['sku'] = self._normalize_value(sku)
        api_params['tax_class'] = self._normalize_value(tax_class)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProductsModel)

