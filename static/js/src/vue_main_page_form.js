import Vue from 'vue';
import IMask from 'imask';

if (document.querySelectorAll('#vue_main_page_form').length) {
	var vue_main_page_form = new Vue({
		name: 'vue_main_page_form',
		el: '#vue_main_page_form',
		components: {},
		data: {
			name: 'i am vue main page form callbacker',
			fio: null,
			phone: null,
			email: null,
			comment: null,
			pdnAccept: false,
			formErrorMessage: null,
			showInValid: false,
			urls: {
				sendForm: '/part_form/',
			},
		},
		mounted() {
			this.tst();
			this.mask_number();
			//this.applyCaptchaStyle();
		},
		methods: {
			tst: function () {
				console.log('i am masker callback method');
			},
			applyCaptchaStyle: function () {
				let element = document.querySelectorAll('input[name=captcha_1]');
				element[0].classList.add('form-control');
				let captcha_image_element = document.querySelectorAll('.captcha');
				captcha_image_element[0].classList.add('float-right');
			},
			mask_number: function () {
				var element = document.getElementById('masked_phone_number');
				var maskOptions = {
					mask: '+{7} 000 000-00-00',
				};
				var mask = IMask(element, maskOptions);
				//console.log('mask', mask);
			},
			checkForm: function () {
				this.showInValid = false;
				if (!this.formCanBeSend) {
					this.formErrorMessage = 'Исправьте ошибки формы...';
					this.showInValid = true;
				}
				return;
			},
			sendForm: function () {
				if (this.formCanBeSend) {
					var payload = {
						fio: this.fio,
						phone: this.phone,
						email: this.email,
						comment: this.comment,
						pdn_accept: this.pdnAccept,
						captcha_1: document.getElementById('id_captcha_1').value,
						captcha_0: document.getElementById('id_captcha_0').value,
					};
					this.$http
						.post(this.urls.sendForm, payload)
						.then((response) => {
							if (response.data.errors) {
								console.log(response.data.errors);
								if (response.data.errors.captcha) {
									//this.formErrorMessage = `${response.data.errors.captcha[0]}`;
									this.formErrorMessage =
										'Вы ввели неверные символы с картинки...';
								}
							} else {
								console.log('success', response.data);
							}
						})
						.catch((err) => {
							console.log(err.data);
						});
				}
			},
		},
		computed: {
			formCanBeSend: function () {
				var email_validation =
					/^((?!\.)[\w-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$/;
				if (
					this.fio &&
					this.phone &&
					this.email &&
					this.pdnAccept &&
					email_validation.test(this.email)
				) {
					return true;
				}
				return false;
			},
		},
	});
}
