var messageApp = angular.module('messageApp', ['ngRoute']);

	messageApp.config(function($routeProvider) {
	$routeProvider
		.when('/messageComp',
		  {
		  	templateUrl:'partials/messageComposition.html'
		});		

	});
