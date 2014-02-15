var indieApp = angular.module('indieApp', []);

indieApp.controller('imageAddCrtl', function($scope, $http) {
	$http.get('js/imageInfo.json')
		.then(function(res) {
			$scope.imageInfo = res.data;
		});
});




	



