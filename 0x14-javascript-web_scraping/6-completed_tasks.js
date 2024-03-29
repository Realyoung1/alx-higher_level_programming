#!/usr/bin/node
/*
    scripted comput number of tasks completed by userID
    when the first ARG is the API URL
    i printed only user with the completed task
    modue request used
*/

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    const dictCompletTodoUser = {};
    for (const todo of jsonBody) {
      if (todo.completed) {
        if (dictCompletTodoUser[todo.userId]) {
          dictCompletTodoUser[todo.userId] += 1;
        } else {
          dictCompletTodoUser[todo.userId] = 1;
        }
      }
    }
    console.log(dictCompletTodoUser);
  }
});
