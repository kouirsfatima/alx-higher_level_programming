#!/usr/bin/node

const count = process.argv.length;

if (count[0] === undefined) {
    console.log('No argument');
  } else {
    console.log(count[0]);
  }
