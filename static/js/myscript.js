// =============== Enable Tooltips & Popovers ===============
//
//captcha django-simple-captcha
//
$('#refresh_captcha').on('click', function (e) {
	e.preventDefault();
	//console.log('refresh clicked...');
	$.getJSON('/captcha/refresh/', function (result) {
		$('.captcha').attr('src', result['image_url']);
		$('#id_captcha_0').val(result['key']);
	});
});
//
var tooltipTriggerList = [].slice.call(
	document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
	return new bootstrap.Tooltip(tooltipTriggerEl);
});
var popoverTriggerList = [].slice.call(
	document.querySelectorAll('[data-bs-toggle="popover"]')
);
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
	return new bootstrap.Popover(popoverTriggerEl);
});
// ===========================================================

// ====================== OwlCarousel =========================
$(document).ready(function () {
	$('.owl-carousel-spikers').owlCarousel({
		// nav: true,
		// navText: ['<i class="bi bi-arrow-left"></i>','<i class="bi bi-arrow-right"></i>'],
		loop: true,
		margin: 10,
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			600: {
				items: 3,
			},
			1000: {
				items: 4,
				loop: false,
			},
		},
	});

	$('.owl-carousel').owlCarousel({
		// nav: true,
		// navText: ['<i class="bi bi-arrow-left"></i>','<i class="bi bi-arrow-right"></i>'],
		loop: true,
		margin: 10,
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			600: {
				items: 3,
			},
			1000: {
				items: 5,
				loop: false,
			},
		},
	});

});
$(document).ready(function () {
	$('.owl-carousel-spikers').owlCarousel({
		// nav: true,
		// navText: ['<i class="bi bi-arrow-left"></i>','<i class="bi bi-arrow-right"></i>'],
		loop: true,
		margin: 10,
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			600: {
				items: 3,
			},
			1000: {
				items: 4,
				loop: false,
			},
		},
	});
});
// ============================================================

// ========================== DatePicker ======================
// $('.form-date').daterangepicker({
//     "singleDatePicker": true,
//     "showDropdowns": true,
//     "minYear": 1950,
//     "maxYear": 2050,
//     "autoApply": true,
//     "locale": {
//         format: 'DD.MM.YYYY',
//         "applyLabel": "Ок",
//         "cancelLabel": "Отмена",
//         // "fromLabel": "От",
//         // "toLabel": "До",
//         "customRangeLabel": "Произвольный",
//         "daysOfWeek": [
//             "Вс",
//             "Пн",
//             "Вт",
//             "Ср",
//             "Чт",
//             "Пт",
//             "Сб"
//         ],
//         "monthNames": [
//             "Январь",
//             "Февраль",
//             "Март",
//             "Апрель",
//             "Май",
//             "Июнь",
//             "Июль",
//             "Август",
//             "Сентябрь",
//             "Октябрь",
//             "Ноябрь",
//             "Декабрь"
//         ],
//         firstDay: 1
//     }
// })
// ===========================================================

// ====================== My scripts =========================

// $("#btnOrgInn").click(function() {
//     console.log("click");
//     $("#id_inn").attr("disabled", false);
// })
// $("#btnOrgName").click(function() {
//     $("#fieldNameOrg").show('fade');
//     $("#textNameOrg").hide();
// })

// $('#checkUsl1').click(function() {
//     if ($(this).is(':checked')) {
//         $('#btnPay').removeClass('disabled');
//     } else {
//         $('#btnPay').addClass('disabled');
//     }
// })

$('#checkSogl1').click(function () {
	if ($(this).is(':checked')) {
		$('#btnSend').removeClass('disabled');
	} else {
		$('#btnSend').addClass('disabled');
	}
});

$('#btn-move-to-reg').click(function () {
	$('#form-registration').show('fade');
	$('#form-signin').hide();
});
$('#btn-move-to-signin').click(function () {
	$('#form-registration').hide();
	$('#form-signin').show('fade');
});
$('#btn-move-to-recovery').click(function () {
	$('#form-recovery').show('fade');
	$('#form-signin').hide();
});
$('#btn-cancel-recovery').click(function () {
	$('#form-recovery').hide();
	$('#form-signin').show('fade');
});
// ===========================================================

// function copyToken() {
//   /* Получить текстовое поле */
//   var copyText = document.getElementById("tokenField");

//   /* Выделите текстовое поле */
//   copyText.select();
//   copyText.setSelectionRange(0, 99999); /* Для мобильных устройств */

//   /* Скопируйте текст внутри текстового поля */
//   document.execCommand("copy");

//   /* Оповещение скопированного текста */
//   // alert("Скопировал текст: " + copyText.value);
// }
// function copyJson() {
//   var copyJson = document.getElementById("jsonField");
//   copyJson.select();
//   copyJson.setSelectionRange(0, 99999);
//   document.execCommand("copy");
// }
// const newsCarousel = new Carousel(document.querySelector("#newsCarousel"), {
//         // preload: 2,
//     });

//     // Customize Fancybox
//     Fancybox.bind('[data-fancybox="gallery"]', {
//         Carousel: {
//             on: {
//                 change: (that) => {
//                     newsCarousel.slideTo(newsCarousel.findPageForSlide(that.page), {
//                         friction: 0,
//                     });
//                 },
//             },
//         },
//     });

const galleryCarousel = new Carousel(document.querySelector('.carousel'), {
	Dots: false,
});
// Thumbnails
if (document.querySelectorAll('.thumb').length) {
	const thumbCarousel = new Carousel(document.querySelector('.thumb'), {
		Sync: {
			target: galleryCarousel,
			friction: 0,
		},
		Dots: false,
		Navigation: false,
		center: true,
		slidesPerPage: 1,
		infinite: false,
	});
}
// Customize Fancybox
Fancybox.bind('[data-fancybox="gallery"]', {
	Carousel: {
		on: {
			change: (that) => {
				galleryCarousel.slideTo(galleryCarousel.findPageForSlide(that.page), {
					friction: 0,
				});
			},
		},
	},
});
