(function () {
  'use strict';

  angular
    .module('thinkster.posts.services')
    .factory('Posts', Posts);

  Posts.$inject = ['$http'];


  function Posts($http) {
    var Posts = {
      all: all,
      create: create,
      get: get
    };

    return Posts;

    ////////////////////


    function all() {
      return $http.get('/api/v1/posts/');
    }

    var fd = new FormData();
    myKeys = Object.keys($scope.vm)
    for(i=0; i < mykeys.length ; i++) {
        fd.append(myKeys[i], vm[myKeys[i]]);
    });

    function create(author,content) {
      return $http.post('/api/v1/posts/', fd);
    }


    function get(username) {
      return $http.get('/api/v1/accounts/' + username + '/posts/');
    }
  }
})();