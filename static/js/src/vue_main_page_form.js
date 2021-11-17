import Vue from 'vue';
import IMask from 'imask';

var vue_main_page_form = new Vue({
	name: 'vue_main_page_form',
	el: '#vue_main_page_form',
	components: {},
	data: {
		name: 'i am vue main page form callbacker',
	},
	mounted() {
		this.tst();
		this.mask_number();
	},
	methods: {
		tst: function () {
			console.log('i am masker callback method');
		},
		mask_number: function () {
			var element = document.getElementById('masked_phone_number');
			var maskOptions = {
				mask: '+{7}(000)000-00-00',
			};
			var mask = IMask(element, maskOptions);
			//console.log('mask', mask);
		},
	},
});
