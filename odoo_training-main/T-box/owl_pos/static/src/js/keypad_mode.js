/** @odoo-module **/

const ProductScreen = require('point_of_sale.ProductScreen');
const NumberBuffer = require('point_of_sale.NumberBuffer');
const {useState,onMounted} = owl.hooks;
const Registery = require('point_of_sale.Registries');



const MyProductScreen = ProductScreen => 
	class extends ProductScreen{

		constructor(){
			super(...arguments);

			onMounted(() => NumberBuffer.reset());

			this.state = useState({
				numpadMode: 'price'
			});

		}


	};

	Registery.Component.extend(ProductScreen,MyProductScreen);

	return MyProductScreen;


