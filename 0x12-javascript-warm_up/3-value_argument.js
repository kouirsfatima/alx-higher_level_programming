#!/usr/bin/node

const Args = process.argv.length;

if (Args === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
