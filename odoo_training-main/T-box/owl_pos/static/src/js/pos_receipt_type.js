odoo.define('owl_pos.point_of_sale.ReceiptType', function (require) {
    "use strict";    
    
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

class  ReceiptType extends PosComponent {
    constructor() {
            super(...arguments);    
          
       }
    mounted() {
           

        }

    set_default(){
        alert("Test");

         
      };
    set_A4(){
       

      };
    set_A5(){
      

      };
    set_A1(){
        
      };

    
};

   ReceiptType.template = 'ReceiptType';

    Registries.Component.add(ReceiptType);



    }); 

