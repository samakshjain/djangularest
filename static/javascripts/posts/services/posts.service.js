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


    function create(content, pic) {
      //var fd = new FormData();
      // fd.append("content", content);
      // fd.append("pic", pic);
      return $http({
       method: 'POST',
       url: '/api/v1/posts/',
       headers: {
         'Content-Type': undefined  
       },
       transformRequest: function (data) {
           var formData = new FormData();
           //need to convert our json object to a string version of json otherwise
           // the browser will do a 'toString()' on the object which will result 
           // in the value '[Object object]' on the server.
           formData.append("content", angular.toJson(data.content));
           formData.append("pic", data.pic);
           return formData;
       },
       data: { content: content,
       pic: pic }
      });
    }


    function get(username) {
      return $http.get('/api/v1/accounts/' + username + '/posts/');
    }
  }
})();