

var indieApp = angular.module('indieApp', []);

indieApp.controller('imageAddCrtl', function($scope, $http) {
	$http.get('js/imageInfo.json').success(function(data) {
		$scope.imageInfo = data;
	});
});












// {
// 		"productId": 2,
// 		"type":"",
// 		"imageUrl": "img/test2.jpg"
// 	},
// 	{
// 		"productId": 3,
// 		"type":"",
// 		"imageUrl": "img/test3.jpg"
// 	},
// 	{
// 		"productId": 4,
// 		"type":"",
// 		"imageUrl": "img/test4.jpg"
// 	},
// 	{
// 		"productId": 5,
// 		"type":"",
// 		"imageUrl": "img/test5.jpg"
// 	},
// 	{
// 		"productId": 6,
// 		"type":"",
// 		"imageUrl": "img/test6.jpg"
// 	},
// 	{
// 		"productId": 7,
// 		"type":"",
// 		"imageUrl": "img/test7.jpg"
// 	},
// 	{
// 		"productId": 8,
// 		"type":"",
// 		"imageUrl": "img/test8.jpg"
// 	},
// 	{
// 		"productId": 9,
// 		"type":"",
// 		"imageUrl": "img/test9.jpg"
// 	},
// 	{
// 		"productId": 10,
// 		"type":"",
// 		"imageUrl": "img/test10.jpg"
// 	},
// 	{
// 		"productId": 11,
// 		"type":"",
// 		"imageUrl": "img/test11.jpg"
// 	},
// 	{
// 		"productId": 12,
// 		"type":"",
// 		"imageUrl": "img/test12.jpg"
// 	},
// 	{
// 		"productId": 13,
// 		"type":"",
// 		"imageUrl": "img/test13.jpg"
// 	},
// 	{
// 		"productId": 14,
// 		"type":"",
// 		"imageUrl": "img/test14.jpg"
// 	},
// 	{
// 		"productId": 15,
// 		"type":"",
// 		"imageUrl": "img/test15.jpg"
// 	},
// 	{
// 		"productId": 16,
// 		"type":"",
// 		"imageUrl": "img/test16.jpg"
// 	},
// 	{
// 		"productId": 17,
// 		"type":"",
// 		"imageUrl": "img/test17.jpg"
// 	},
// 	{
// 		"productId": 18,
// 		"type":"",
// 		"imageUrl": "img/test18.jpg"
// 	},
// 	{
// 		"productId": 19,
// 		"type":"",
// 		"imageUrl": "img/test19.jpg"
// 	},
// 	{
// 		"productId": 20,
// 		"type":"",
// 		"imageUrl": "img/test20.jpg"
// 	},
// 	{
// 		"productId": 21,
// 		"type":"",
// 		"imageUrl": "img/test21.jpg"
// 	},
// 	{
// 		"productId": 22,
// 		"type":"",
// 		"imageUrl": "img/test23.jpg"
// 	},
// 	{
// 		"productId": 24,
// 		"type":"",
// 		"imageUrl": "img/test24.jpg"
// 	},
// 	{
// 		"productId": 25,
// 		"type":"",
// 		"imageUrl": "img/test25.jpg"
// 	},
// 	{
// 		"productId": 26,
// 		"type":"",
// 		"imageUrl": "img/test26.jpg"
// 	}




	



