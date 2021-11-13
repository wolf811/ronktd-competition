const { VueLoaderPlugin } = require("vue-loader");
var BundleTracker = require("webpack-bundle-tracker");
const path = require("path");
// const webpack = require('webpack')

module.exports = {
	// target: 'web',
	context: __dirname,
	mode: "development",
	entry: {
		main: "./static/js/src/main.js",
	},
	output: {
		filename: "app.js",
		path: require("path").resolve("./static/js/dist/"),
		// publicPath: '/static_root/webpackbundles/',
	},
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader",
				},
			},
			{
				test: /\.vue$/,
				loader: "vue-loader",
			},
			// {
			//   test: /\.css$/,
			//   use: [
			//     'style-loader',
			//     'css-loader',
			//     'vue-style-loader'
			//   ]
			// }
		],
	},
	devtool: "inline-source-map",
	plugins: [
		new VueLoaderPlugin(),
		new BundleTracker({
			path: __dirname,
			filename: "./assets/webpack-stats.json",
		}),
		// new webpack.HotModuleReplacementPlugin(),
		// new webpack.NamedModulesPlugin(),
	],
	resolve: {
		alias: {
			vue$: "vue/dist/vue.common.js",
		},
		extensions: ["*", ".js", ".vue", ".json"],
	},
	devServer: {
		// disableHostCheck: true,
		// contentBase: require('path').resolve('./static_root/webpackbundles/'),
		// hot: true,
		// logLevel: 'warn',
		// reload: true,
		// stats: 'errors-only',
		//inline: true,
		hot: false,
		client: false,
		devMiddleware: {
			writeToDisk: true,
		},
		//writeToDisk: true THIS WOULD CAUSE AND ERROR!!!
		// proxy: {
		//   '!/static_root/webpackbundles/**': {
		//     target: 'http://127.0.0.1:8000', //points to django server
		//     changeOrigin: true,
		//   },
		// },
	},
	// "jest": {
	//     "moduleFileExtensions": [
	//         "js",
	//         "json",
	//         "vue"
	//     ],
	//     "transform": {
	//         "^.+\\.js$": "<rootDir>/node_modules/babel-jest",
	//         ".*\\.(vue)$": "<rootDir>/node_modules/vue-jest"
	//     }
	// }
};
