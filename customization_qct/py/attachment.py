from __future__ import unicode_literals

import frappe
import os, base64
from frappe import _, throw
from frappe.utils import flt
from frappe.utils.file_manager import save_url, save_file, get_file_name, remove_all, remove_file
from frappe.utils import get_site_path, get_files_path, random_string, encode
import json

@frappe.whitelist()
def attach_all_docs(document, method=None):
	"""This function attaches drawings to the purchase order based on the items being ordered"""
	document = json.loads(document)
	current_attachments = []
	print(document["items"])
	print(len(document["items"]))
	item_list=document["items"][0]
	print(item_list["item_code"])
	for file_url in frappe.db.sql("""select file_url,name,is_private from `tabFile` where attached_to_name = '{0}'""".format(item_list["item_code"]), as_dict=True ):
		print("$#$#$#")
		print(file_url)
		current_attachments.append(file_url.file_url)
		count=0
		for item_doc in document["items"]:
			#frappe.msgprint(item_doc)
			# Check to see if the quantity is = 1
			item = frappe.get_doc("Item",item_doc["item_code"])
			attachments = []
			# Get the path for the attachments
			if item.drawing_attachment:
				attachments.append(item.drawing_attachment)
			if item.stp_attachment:
				attachments.append(item.stp_attachment)
			if item.dxf_attachment:
				attachments.append(item.dxf_attachment)
			if item.x_t_attachment:
				attachments.append(item.x_t_attachment)
		
			for attach in attachments:
				# Check to see if this file is attached to the one we are looking for
				if not attach in current_attachments:
					count = count + 1
					print("@#----------------rge-----------ef-#")
					save_url(file_url.file_url,file_url.file_url,"Quotation",document["name"], "Home/Attachments",file_url.is_private)
			frappe.msgprint("Attached {0} files".format(count))