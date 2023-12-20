odoo.define('owl_pos.ExtraExtends', function(require) {
'use strict';
   const ProductScreen = require('point_of_sale.ProductScreen');
   const DiscountButton = require('pos_discount.DiscountButton');


   ProductScreen.addControlButton({

    component: DiscountButton,

    condition: function() {

        var cashier = this.env.pos.get('cashier') || this.env.pos.get_cashier();
        let has_discount = true;

        if (cashier.user_id[0] != 2){
          has_discount = false;

        }
            

        return this.env.pos.config.module_pos_discount && this.env.pos.config.discount_product_id && has_discount;

    },

    position: ['replace', 'DiscountButton'],

});

});