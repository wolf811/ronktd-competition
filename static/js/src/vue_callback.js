import Vue from "vue";

var vue_callbacker = new Vue({
	name: "vue_callbacker",
	el: "#test_callback",
	components: {},
	data: {
		name: "i am vue callbacker",
	},
	mounted() {
		this.tst();
	},
	methods: {
		tst: function () {
			console.log("i am test method");
		},
	},
});
