odoo.define('owl_pos.CustomTopButtons', function(require) {
'use strict';

   const { Gui } = require('point_of_sale.Gui');
   const PosComponent = require('point_of_sale.PosComponent');
   const Registries = require('point_of_sale.Registries');

   class CustomTopButtons extends PosComponent {
        onClick() {
            Gui.showPopup("ErrorPopup", {
               title: this.env._t('Custom Top Button Clicked'),
               body: this.env._t('Welcome to OWL, From top button'),
           });
        }
    }
   CustomTopButtons.template = 'CustomTopButtons';
   Registries.Component.add(CustomTopButtons);
   
});