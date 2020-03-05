from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Units"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description": _("Lease."),
					"route_options": {
							"item_group": "Garoud Community"
							}
				},
				{
					"type": "doctype",
					"name": "Lease Units",
					"description": _("Lease Units."),
				},
			]
		},

		{
			"label": _("Contracts"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Contracts."),
				},
				]
		},
		{
			"label": _("Billing"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"description": _("Invoice."),
				},

			]
		},
	]
