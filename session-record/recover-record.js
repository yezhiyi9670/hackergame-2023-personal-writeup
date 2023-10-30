const fs = require('fs')

const content = fs.readFileSync('./asciinema_restore.rec').toString()

const lines = content.split('\n')

let result = ''

for(const line of lines) {
  if(line[0] == '[') {
    const obj = JSON.parse(line)
    if(obj[1] != 'o') {
      throw new Error(`Unknown action ${obj[1]}, line ${line}`)
    }
    result += obj[2]
  }
}

console.log(result)
