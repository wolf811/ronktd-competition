import Vue from 'vue';

export let vueRegisterSeminarApp;

if (document.querySelectorAll('#vue_register_seminar_app').length) {
	vueRegisterSeminarApp = new Vue({
		el: '#vue_register_seminar_app',
		name: 'vueRegisterSeminarApp',
		data: {
			myName: 'i am here',
			errors: null,
			successMessage: null,
		},
		mounted() {
			console.log(this.myName);
			$('#refresh_captcha').on('click', function (e) {
				e.preventDefault();
				//console.log('refresh clicked...');
				$.getJSON('/captcha/refresh/', function (result) {
					$('.captcha').attr('src', result['image_url']);
					$('#id_captcha_0').val(result['key']);
				});
			});
		},
		methods: {
			sendFormData: function () {
				this.errors = null;
				let formData = new FormData(document.forms.register_participant_form);
				this.$http
					.post('/seminar/register/', formData)
					.then((response) => {
						console.log(response.data);
						if (response.data.errors) {
							this.errors = response.data.errors;
						}
						if (response.data.success) {
							console.log('successRegistration', response.data.success);
							this.successMessage = response.data.success;
							window.location.replace('/seminar/#block_04');
						}
					})
					.catch((err) => {
						console.log('error', err.data);
					});
			},
			getErrorText(err) {
				return this.errors[err][0];
			},
		},
	});
}
