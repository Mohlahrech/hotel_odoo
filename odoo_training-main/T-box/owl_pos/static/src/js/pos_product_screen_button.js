odoo.define('owl_pos.RewardButton', function(require) {
'use strict';
   const { Gui } = require('point_of_sale.Gui');
   const PosComponent = require('point_of_sale.PosComponent');
   const ProductScreen = require('point_of_sale.ProductScreen');
   const { useListener } = require('web.custom_hooks');
   const Registries = require('point_of_sale.Registries');

   class CustomRewardButtons extends PosComponent {
       constructor() {
           super(...arguments);
           useListener('click', this.onClick);
       }
      
       onClick() {
            Gui.showPopup("ErrorPopup", {
               title: this.env._t('Button reward Custom Button Clicked'),
               body: this.env.pos.get_cashier().user_id[1],
           });
        }
   }

   CustomRewardButtons.template = 'CustomRewardButtons';

   ProductScreen.addControlButton({
       component: CustomRewardButtons,
       condition: function() {
           return this.env.pos;
       },
   });
   Registries.Component.add(CustomRewardButtons);

});