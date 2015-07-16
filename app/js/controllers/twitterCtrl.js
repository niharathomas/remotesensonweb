	'use strict';

	app.controller('loginCtrl', ['$scope','loginService', function ($scope,loginService) {
		$scope.twitterSignIn=function(data){
			OAuth.popup('twitter', function(error, success){
	  // See the result below
				});	
	}}]);
