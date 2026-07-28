#!/usr/bin/node

document.getElementById('update_header').addEventListener('click', () => {
  document.querySelector('header').textContent = 'New Header!!!';
});