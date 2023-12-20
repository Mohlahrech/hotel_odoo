odoo.define('owl_pos.form_edit', function (require) {
"use strict";

var FormController = require('web.FormController')

FormController.include({

    getSelectedIds: function () {
        var menu = this.$el.find(".o_form_button_edit");
       
            var button = this.$buttons.find(".o_form_button_edit").show();
            if (this.modelName == 'stock.picking') {
                var currentRecord = this.model.get(this.handle).data;
               
                if (currentRecord.state === 'done' ) {
                    this.$buttons.find(".o_form_button_edit").hide();
                }
            }
        

        return this._super.apply(this, arguments);
    }

});

});