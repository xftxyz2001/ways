function groupBy(arr, keyGenerator) {
  if (typeof keyGenerator === "string") {
    keyGenerator = (item) => item[keyGenerator];
  }
  const result = {};
  for (const item of arr) {
    const key = keyGenerator(item);
    if (!result[key]) {
      result[key] = [];
    }
    result[key].push(item);
  }
  return result;
}
