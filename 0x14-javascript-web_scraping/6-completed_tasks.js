#!/usr/bin/node
// Computes the number of tasks completed by user id.

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const done = {};
    todos.forEach((todo) => {
      if (done[todo.userId] === undefined && todo.completed) {
        done[todo.userId] = 1;
      } else if (todo.completed) {
        done[todo.userId] += 1;
      }
    });
    console.log(done);
  }
});
