from __future__ import annotations

import json
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class InvoiceAddress(BaseModel):
    """
    A class representing an address in an invoice.

    Attributes:
        street: Street address
        city: City, e.g. New York
        state: State, e.g. NY
        postal_code: Postal code, e.g. 10001
        country: Country, e.g. USA
        phone: Phone number, e.g. +1-123-456-7890
    """

    Attention: Optional[str] = Field(description="Name, e.g. John Doe")
    street: Optional[str] = Field(description="Street address, e.g. 123 Main St.")
    city: Optional[str] = Field(description="City, e.g. New York")
    state: Optional[str] = Field(description="State, e.g. NY")
    postal_code: Optional[str] = Field(description="Postal code, e.g. 10001")
    phone: Optional[str] = Field(description="Phone number, e.g. +1-123-456-7890.")

    @staticmethod
    def example():
        """
        Creates an empty example InvoiceAddress object.

        Returns:
            InvoiceAddress: An empty InvoiceAddress object.
        """

        return InvoiceAddress(street="", city="", state="", postal_code="", Attention="")

    def to_dict(self):
        """
        Converts the InvoiceAddress object to a dictionary.

        Returns:
            dict: The InvoiceAddress object as a dictionary.
        """

        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "postal_code": self.postal_code,
            "attention": self.Attention,
            "phone": self.phone,
        }


class InvoiceSignature(BaseModel):
    """
    A class representing a signature for the subcontractor.

    Attributes:
        signatory: Name of the person from the subcontractor who signed the contract.
        is_signed: Indicates if the contract is signed.
    """

    signatory: Optional[str] = Field(
        description="Name of the person who signed the contract"
    )
    is_signed: Optional[bool] = Field(description="Indicates if the contract is signed by the subcontractor")

    @staticmethod
    def example():
        """
        Creates an empty example InvoiceSignature object.

        Returns:
            InvoiceSignature: An empty InvoiceSignature object
        """

        return InvoiceSignature(signatory="", is_signed=False)

    def to_dict(self):
        """
        Converts the InvoiceSignature object to a dictionary.

        Returns:
            dict: The InvoiceSignature object as a dictionary.
        """

        return {"signatory": self.signatory, "is_signed": self.is_signed}


class InvoiceItem(BaseModel):
    """
    A class representing a details of the contract.

    Attributes:
        subcontractor: name of the company listed as subcontractor.
        subcontract: category assigned to the scope of the project.
        project: name assigned to the project.
        project_num: full project number as listed in the contract.
        project_num_prefix: portion of project number before '-', not including the '-'.
        project_num_Suffix: portion of project number after '-', not including the '-'.
        architect: architect named in the contract.
        total_contract_value: value of contract in dollars and cents.
    """

    subcontractor: Optional[str] = Field(
        description="name of the company listed as subcontractor, e.g. Iron Woman Construction & Environmental Services LLC",
    )
    subcontract: Optional[str] = Field(
        description="category assigned to the scope of the project, e.g.  Site Utilities",
    )
    project: Optional[str] = Field(
        description="name assigned to the project, e.g. Pena Station Filing 2 and DIBC Filing 7 Phase 2",
    )
    project_num: Optional[str] = Field(
        description="full project number as listed in the contract, e.g. 3019221 - 0250000",
    )
    project_num_prefix: Optional[str] = Field(
        description="portion of project number before '-', not including the '-', e.g. 3019221",
    )
    project_num_Suffix: Optional[str] = Field(
        description="portion of project number after '-', not including the '-', e.g. 0250000",
    )
    architect: Optional[str] = Field(
        description="architect named in the contract.",
    )
    total_contract_value: Optional[str] = Field(
        description="value of contract in dollars., e.g. $ 7,515,472",
    )

    @staticmethod
    def example():
        """
        Creates an empty example InvoiceItem object.

        Returns:
            InvoiceItem: An empty InvoiceItem object.
        """
        return InvoiceItem(
            subcontractor="",
            subcontract="",
            project="",
            project_num="",
            project_num_prefix="",
            project_num_Suffix="",
            architect="",
            total_contract_value="",
        )

    def to_dict(self):
        """
        Converts the InvoiceItem object to a dictionary.

        Returns:
            dict: The InvoiceItem object as a dictionary.
        """

        return {
            "subcontractor": self.subcontractor,
            "subcontract": self.subcontract,
            "project": self.project,
            "project_num": self.project_num,
            "project_num_prefix": self.project_num_prefix,
            "project_num_Suffix": self.project_num_Suffix,
            "architect": self.architect,
            "total_contract_value": self.total_contract_value,
        }


class Invoice(BaseModel):
    """
    A class representing an invoice.

    Attributes:
        customer_name: Name of the customer being invoiced.
        customer_address: Full address of the customer.
        customer_tax_id: Government tax ID of the customer.
        shipping_address: Full address of the shipping location for the customer.
        purchase_order: Purchase order reference number.
        invoice_id: Reference ID for the invoice.
        invoice_date: Date the invoice was issued.
        payable_by: Date when the invoice should be paid.
        vendor_name: Name of the vendor who created the invoice.
        vendor_address: Full address of the vendor.
        vendor_tax_id: Government tax ID of the vendor.
        remittance_address: Full address where the payment should be sent.
        subtotal: Subtotal of the invoice.
        total_discount: Total discount applied to the invoice.
        total_tax: Total tax applied to the invoice.
        invoice_total: Total charges associated with the invoice.
        payment_terms: Payment terms for the invoice.
        items: List of line items in the invoice.
        total_item_quantity: Total quantity of items in the invoice.
        items_customer_signature: Signature of the customer for the items in the invoice.
        items_vendor_signature: Signature of the vendor for the items in the invoice.
        returns: List of line items returned in the invoice.
        total_return_quantity: Total quantity of items returned in the invoice.
        returns_customer_signature: Signature of the customer for the returned items in the invoice.
        returns_vendor_signature: Signature of the vendor for the returned items in the invoice.
    """

    customer_name: Optional[str] = Field(
        description="Name of the customer being invoiced, e.g. Company A"
    )
    customer_address: Optional[InvoiceAddress] = Field(
        description="Full address of the customer, e.g. 123 Main St., City, Country"
    )
    customer_tax_id: Optional[str] = Field(
        description="Government tax ID of the customer, e.g. 123456789"
    )
    shipping_address: Optional[InvoiceAddress] = Field(
        description="Full address of the shipping location for the customer (null if the same as customer address), e.g. 123 Main St., City, Country"
    )
    purchase_order: Optional[str] = Field(
        description="Purchase order reference number, e.g. PO-1234"
    )
    invoice_id: Optional[str] = Field(
        description="Reference ID for the invoice (often invoice number), e.g. INV-1234"
    )
    invoice_date: Optional[str] = Field(
        description="Date the invoice was issued or delivered, e.g., 2021-01-01"
    )
    payable_by: Optional[str] = Field(
        description="Date when the invoice should be paid, e.g., 2021-01-15"
    )
    vendor_name: Optional[str] = Field(
        description="Name of the vendor who created the invoice, e.g. Company B"
    )
    vendor_address: Optional[InvoiceAddress] = Field(
        description="Full address of the vendor, e.g. 321 Main St., City, Country"
    )
    vendor_tax_id: Optional[str] = Field(
        description="Government tax ID of the vendor, e.g. 123456789"
    )
    remittance_address: Optional[InvoiceAddress] = Field(
        description="Full address where the payment should be sent (null if the same as vendor address), e.g. 321 Main St., City, Country"
    )
    subtotal: Optional[float] = Field(
        description="Subtotal of the invoice, e.g. 100.00"
    )
    total_discount: Optional[float] = Field(
        description="Total discount applied to the invoice, e.g. 10.00"
    )
    total_tax: Optional[float] = Field(
        description="Total tax applied to the invoice, e.g. 5.00"
    )
    invoice_total: Optional[float] = Field(
        description="Total charges associated with the invoice, e.g. 95.00"
    )
    payment_terms: Optional[str] = Field(
        description="Payment terms for the invoice, e.g. Net 90"
    )
    items: Optional[list[InvoiceItem]] = Field(
        description="List of line items in the invoice"
    )
    total_item_quantity: Optional[float] = Field(
        description="Total quantity of items in the invoice"
    )
    items_customer_signature: Optional[InvoiceSignature] = Field(
        description="Signature of the customer for the items in the invoice"
    )
    items_vendor_signature: Optional[InvoiceSignature] = Field(
        description="Signature of the vendor for the items in the invoice"
    )
    returns: Optional[list[InvoiceItem]] = Field(
        description="List of line items returned in the invoice"
    )
    total_return_quantity: Optional[float] = Field(
        description="Total quantity of items returned in the invoice"
    )
    returns_customer_signature: Optional[InvoiceSignature] = Field(
        description="Signature of the customer for the returned items in the invoice"
    )
    returns_vendor_signature: Optional[InvoiceSignature] = Field(
        description="Signature of the vendor for the returned items in the invoice"
    )

    @staticmethod
    def example():
        """
        Creates an empty example Invoice object.

        Returns:
            Invoice: An empty Invoice object.
        """

        return Invoice(
            customer_name="",
            customer_address=InvoiceAddress.example(),
            customer_tax_id="",
            shipping_address=InvoiceAddress.example(),
            purchase_order="",
            invoice_id="",
            invoice_date=datetime.now().strftime("%Y-%m-%d"),
            payable_by=datetime.now().strftime("%Y-%m-%d"),
            vendor_name="",
            vendor_address=InvoiceAddress.example(),
            vendor_tax_id="",
            remittance_address=InvoiceAddress.example(),
            subtotal=0.0,
            total_discount=0.0,
            total_tax=0.0,
            invoice_total=0.0,
            payment_terms="",
            items=[InvoiceItem.example()],
            total_item_quantity=0.0,
            items_customer_signature=InvoiceSignature.example(),
            items_vendor_signature=InvoiceSignature.example(),
            returns=[InvoiceItem.example()],
            total_return_quantity=0.0,
            returns_customer_signature=InvoiceSignature.example(),
            returns_vendor_signature=InvoiceSignature.example(),
        )

    @staticmethod
    def from_json(json_str: str):
        """
        Creates an Invoice object from a JSON string.

        Args:
            json_str: The JSON string representing the Invoice object.

        Returns:
            Invoice: An Invoice object.
        """

        json_content = json.loads(json_str)

        def create_invoice_address(address):
            """
            Creates an InvoiceAddress object from a dictionary.

            Args:
                address: A dictionary representing an InvoiceAddress object.

            Returns:
                InvoiceAddress: An InvoiceAddress object.
            """

            if address is None:
                return None

            return InvoiceAddress(
                street=address.get("street", None),
                city=address.get("city", None),
                state=address.get("state", None),
                postal_code=address.get("postal_code", None),
                country=address.get("country", None),
            )

        def create_invoice_item(item):
            """
            Creates an InvoiceItem object from a dictionary.

            Args:
                product: A dictionary representing an InvoiceItem object.

            Returns:
                InvoiceItem: An InvoiceItem object.
            """

            if item is None:
                return None

            return InvoiceItem(
                product_code=item.get("product_code", None),
                description=item.get("description", None),
                quantity=item.get("quantity", None),
                tax=item.get("tax", None),
                tax_rate=item.get("tax_rate", None),
                unit_price=item.get("unit_price", None),
                total=item.get("total", None),
                reason=item.get("reason", None),
            )

        def create_invoice_signature(signature):
            """
            Creates an InvoiceSignature object from a dictionary.

            Args:
                signature: A dictionary representing an InvoiceSignature object.

            Returns:
                InvoiceSignature: An InvoiceSignature object.
            """

            if signature is None:
                return None

            return InvoiceSignature(
                signatory=signature.get("signatory", None),
                is_signed=signature.get("is_signed", None),
            )

        invoice_items = [
            create_invoice_item(item) for item in json_content.get("items", [])
        ]
        invoice_returns = [
            create_invoice_item(return_product)
            for return_product in json_content.get("returns", [])
        ]

        return Invoice(
            customer_name=json_content.get("customer_name", None),
            customer_address=create_invoice_address(
                json_content.get("customer_address", None)
            ),
            customer_tax_id=json_content.get("customer_tax_id", None),
            shipping_address=create_invoice_address(
                json_content.get("shipping_address", None)
            ),
            purchase_order=json_content.get("purchase_order", None),
            invoice_id=json_content.get("invoice_id", None),
            invoice_date=json_content.get("invoice_date", None),
            payable_by=json_content.get("payable_by", None),
            vendor_name=json_content.get("vendor_name", None),
            vendor_address=create_invoice_address(
                json_content.get("vendor_address", None)
            ),
            vendor_tax_id=json_content.get("vendor_tax_id", None),
            remittance_address=create_invoice_address(
                json_content.get("remittance_address", None)
            ),
            subtotal=json_content.get("subtotal", None),
            total_discount=json_content.get("total_discount", None),
            total_tax=json_content.get("total_tax", None),
            invoice_total=json_content.get("invoice_total", None),
            payment_terms=json_content.get("payment_terms", None),
            items=invoice_items,
            total_item_quantity=json_content.get("total_item_quantity", None),
            items_customer_signature=create_invoice_signature(
                json_content.get("items_customer_signature", None)
            ),
            items_vendor_signature=create_invoice_signature(
                json_content.get("items_vendor_signature", None)
            ),
            returns=invoice_returns,
            total_return_quantity=json_content.get("total_return_quantity", None),
            returns_customer_signature=create_invoice_signature(
                json_content.get("returns_customer_signature", None)
            ),
            returns_vendor_signature=create_invoice_signature(
                json_content.get("returns_vendor_signature", None)
            ),
        )

    def to_dict(self):
        """
        Converts the Invoice object to a dictionary.

        Returns:
            dict: The Invoice object as a dictionary.
        """

        def to_list(items, expected_type):
            return [item.to_dict() for item in items if isinstance(item, expected_type)]

        items = to_list(self.items or [], InvoiceItem)
        returns = to_list(self.returns or [], InvoiceItem)

        return {
            "customer_name": self.customer_name,
            "customer_address": self.customer_address.to_dict()
            if self.customer_address is not None
            else None,
            "customer_tax_id": self.customer_tax_id,
            "shipping_address": self.shipping_address.to_dict()
            if self.shipping_address is not None
            else None,
            "purchase_order": self.purchase_order,
            "invoice_id": self.invoice_id,
            "invoice_date": self.invoice_date,
            "payable_by": self.payable_by,
            "vendor_name": self.vendor_name,
            "vendor_address": self.vendor_address.to_dict()
            if self.vendor_address is not None
            else None,
            "vendor_tax_id": self.vendor_tax_id,
            "remittance_address": self.remittance_address.to_dict()
            if self.remittance_address is not None
            else None,
            "subtotal": f"{self.subtotal:.2f}" if self.subtotal is not None else None,
            "total_discount": f"{self.total_discount:.2f}"
            if self.total_discount is not None
            else None,
            "total_tax": f"{self.total_tax:.2f}"
            if self.total_tax is not None
            else None,
            "invoice_total": f"{self.invoice_total:.2f}"
            if self.invoice_total is not None
            else None,
            "payment_terms": self.payment_terms,
            "items": items,
            "total_item_quantity": self.total_item_quantity,
            "items_customer_signature": self.items_customer_signature.to_dict()
            if self.items_customer_signature is not None
            else None,
            "items_vendor_signature": self.items_vendor_signature.to_dict()
            if self.items_vendor_signature is not None
            else None,
            "returns": returns,
            "total_return_quantity": self.total_return_quantity,
            "returns_customer_signature": self.returns_customer_signature.to_dict()
            if self.returns_customer_signature is not None
            else None,
            "returns_vendor_signature": self.returns_vendor_signature.to_dict()
            if self.returns_vendor_signature is not None
            else None,
        }
