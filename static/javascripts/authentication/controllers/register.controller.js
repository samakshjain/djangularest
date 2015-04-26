(function () {
  'use strict';

  angular
    .module('thinkster.authentication.controllers')
    .controller('RegisterController', RegisterController)
    .directive('fileModel', ['$parse', function ($parse) {
        return {
            restrict: 'A',
            link: function(scope, element, attrs) {
                var model = $parse(attrs.fileModel);
                var modelSetter = model.assign;

                element.bind('change', function(){
                    scope.$apply(function(){
                        modelSetter(scope, element[0].files[0]);
                    });
                });
            }
        };
  }]);
  RegisterController.$inject = ['$location', '$scope', 'Authentication'];


  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;
    activate();


    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }


    function register() {
      Authentication.register(vm.email, vm.password, vm.username);
    }
  }
})();