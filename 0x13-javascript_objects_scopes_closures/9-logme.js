global.num = 0;
exports.logMe = function (item) {
  console.log(global.num++ + ': ' + item);
};
