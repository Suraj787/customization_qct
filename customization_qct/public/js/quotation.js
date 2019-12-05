frappe.ui.form.on('Quotation', {
	
	letter:function(frm){
		frappe.db.get_value("Cover Letter",frm.doc.letter,"cover_letter",(val) =>{
			console.log(val)
		frm.set_value("letter_content",val.cover_letter)
		});
	}
	
});

frappe.ui.form.on("Quotation", "business_lines", function(frm, cdt, cdn) {
    
    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Field of Scope",
            filters: {
                "bussiness_line": frm.doc.business_lines,
            },
            fields: ["fields"]
        },
        callback: function(r) {
            var scope_details = [];
            frm.clear_table("scope_details");
            for (var i = 0; i < r.message.length; i++) {
                var d = frm.add_child("scope_details");
                for (var key in r.message[i]) {
                    if (r.message[i].hasOwnProperty(key)) {
                       var a= d.name;
                       console.log(a);
                        frappe.model.set_value(d.doctype, d.name, key, r.message[i][key]);
                    }
                }
                frm.refresh_field("scope_details");
            }
            
        }
    })

});