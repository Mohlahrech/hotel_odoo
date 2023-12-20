odoo.define('owl_pos.PaymentScreenButton', function(require) {
'use strict';
   const { Gui } = require('point_of_sale.Gui');
   const Registries = require('point_of_sale.Registries');
   const PaymentScreen = require('point_of_sale.PaymentScreen');

    const CustomButtonPaymentScreen = (PaymentScreen) =>
       class extends PaymentScreen {
         
           IsCustomButton() {
             
                Gui.showPopup("ErrorPopup", {
                       title: this.env._t('Payment Screen Custom Button Clicked'),
                       body: this.env._t('Welcome to OWL Payment custom button'),
                   });
           }
       };
   Registries.Component.extend(PaymentScreen, CustomButtonPaymentScreen);
   return CustomButtonPaymentScreen;
});