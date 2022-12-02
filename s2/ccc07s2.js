function main() {

  let boxSizes = gets();

  const box = [];

  while(boxSizes--){
    const sizeArr = gets().split(' ');
    sizeArr.sort((a, b) => a - b);
    const [l, w, h] = sizeArr;
    box.push({l, w, h});
  }

  let numOfItems = gets();
  let output = '';
  while (numOfItems--){
    const itemSizesArr = gets().split(' ');
    itemSizesArr.sort((a, b) => a - b);
    const [itemL, itemW, itemH] = itemSizesArr;
    let canFit = 0;
    for (let i of box){
      if (itemL <= i.l && itemW <= i.w && itemH <= i.h){
        canFit = i.w * i.h * i.l;
        break;
      }
    }
    if (canFit) output += canFit + '\n';
    else output += "Item does not fit.\n";
  }
  print(output);
}

function gets() {return prompt()};
function print(x) {console.log(x)};
