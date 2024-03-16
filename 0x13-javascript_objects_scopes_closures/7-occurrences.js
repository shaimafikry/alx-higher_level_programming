exports.nbOccurences = function (list, searchElement) {
  let m = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) { m++; }
  }
  return m;
};
