from enum import Enum

class ContactPermissionsPermissions(Enum):
    CATALOG_READ = "catalog.read"
    CARTS_MANAGE = "carts.manage"
    ORDERS_CREATE = "orders.create"
    ORDERS_REQUEST = "orders.request"
    ORDERS_APPROVE = "orders.approve"
    ORDERS_READ = "orders.read"
    ADDRESSES_MANAGE = "addresses.manage"
    CONTACTS_READ = "contacts.read"
    CONTACTS_MANAGE = "contacts.manage"
    ORGANIZATION_MANAGE = "organization.manage"
