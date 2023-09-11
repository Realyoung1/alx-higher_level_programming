#!/usr/bin/node
/*
  print Found or not if exists input arguments
*/
#!/usr/bin/node
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
