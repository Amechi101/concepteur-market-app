angular.module('messageApp', []).config(messageRouter);


function messageRouter ($routeProvider) {
	$routeProvider
		.when('/messageComp',
		{
 			templateURL:'partials/messageComposition.html'
		})
		.otherwise({redirectTO:'/'})
			
}