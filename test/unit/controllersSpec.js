'use strict';

/* jasmine specs for controllers go here */

describe('loginCtrl', function(){

  it('should login valid users', function() {
    var scope = {},
        ctrl = new loginCtrl(scope);

    expect(scope.phones.length).toBe(3);
  });

  it('should ....', inject(function() {
    //spec body
  }));
});
