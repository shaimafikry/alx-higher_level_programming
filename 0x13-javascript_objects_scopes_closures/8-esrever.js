exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1, m = 0; i >= 0; m++, i--) {
    newList[m] = list[i];
  }
  return newList;
};
