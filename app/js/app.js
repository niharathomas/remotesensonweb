'use strict';
// Declare app level module which depends on filters, and services
var app= angular.module('myApp', ['ngRoute']);
app.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', { templateUrl: 'partials/landing.html', controller: 'landingCtrl' });
  $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'loginCtrl'});
  $routeProvider.when('/home', {templateUrl: 'partials/home.html', controller: 'homeCtrl'});
  $routeProvider.when('/register', {templateUrl: 'partials/register.html', controller: 'registerCtrl'});
  $routeProvider.when('/sensors', {templateUrl: 'partials/sensor.html', controller: 'sensorCtrl'});
  $routeProvider.otherwise({redirectTo: '/login'});
}]);


app.run(function($rootScope, $location, loginService){
	var routespermission=['/home'];  //route that require login
	$rootScope.$on('$routeChangeStart', function(){
		if( routespermission.indexOf($location.path()) !=-1)
		{
			var connected=loginService.islogged();
			connected.then(function(msg){
				if(!msg.data) $location.path('/login');
			});
		}
	});
});