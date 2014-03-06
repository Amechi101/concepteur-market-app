var indieApp = angular.module('indieApp', []);

indieApp.controller('imageAddCrtl', function($scope, $http) {
	$http.get('js/imageInfo.json').success(function(data) {
		$scope.imageInfo = data;
	});
});




