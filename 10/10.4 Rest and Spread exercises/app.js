const filterOutOdds = (arr) => {
  return [...arr].filter((num) => { return num % 2 === 0 })
};

const findMin = (arr) => {
  return [...arr].reduce((acc, nextNum) => {
    return Math.min(acc, nextNum);
  });
};

const mergeObjects = (obj1, obj2) => {
  return { ...obj1, ...obj2 };
};

const doubleAndReturnArgs = (...args) => {
  let newArr = [];
  for (const item of args) {
    if (typeof (item) == "object") {
      newArr.push(...item)
    } else {
      newArr.push(item);
    }
  };

  return newArr.reduce((acc, next) => {
    return [...acc, next * 2]
  }, [])

}

const removeRandom = (items) => {
  let newItems = [...items];
  newItems.splice(Math.floor(Math.random() * newItems.length), 1);
  return newItems;
};

const extend = (...args) => {
  const mergeArr = [];
  return [...args].reduce((acc, next) => {
    let accArr = [...acc];
    if (typeof (next) == "object") {
      for (const item of next) {
        accArr.push(item);
      }
    } else {
      accArr.push(next);
    }
    return accArr;
  }, []);
}

const testObj = { first: "Daniel", last: "McNathaniel" };

const addKeyVal = (obj, key, val) => {
  return { ...obj, [`${key}`]: val };
};

const removeKey = (obj, key) => {
  let newObj = { ...obj };
  delete newObj[key];
  return newObj;
}

const combine = (obj1, obj2) => {
  return { ...obj1, ...obj2 };
};

const update = (obj, key, val) => {
  const updatedObj = { ...obj }
  updatedObj[`${key}`] = val;
  return updatedObj;
}