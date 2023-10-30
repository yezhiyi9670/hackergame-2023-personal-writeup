const fs = require('fs')

let dumpContent = fs.readFileSync('dump.txt').toString()
const stripContent = fs.readFileSync('strip.txt').toString()

while(true) {
  let next = dumpContent.replace(stripContent.trim(), '')
  if(next == dumpContent) {
    break
  }
  dumpContent = next
}

console.log(dumpContent)
