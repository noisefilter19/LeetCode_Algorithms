let multi = 2;
let str = "Little lamb";
let multiStr = "";

while(multi > 0){
  multiStr += str
  multiStr += " ";
  multi--;
}

multiStr = multiStr.trimEnd();
console.log(multiStr); // "Little lamb Little lamb"