const express = require('express');
const fs = require('fs').promises;

function countStudents(path) {
  let result = '';
  return fs.readFile(path, 'utf8')
    .then((data) => {
      // split the data into rows and remove empty lines
      const rows = data.split('\n').filter((row) => row);

      // find index of field and firstName in csv
      const headers = rows.shift().split(',');
      const fieldIndex = headers.indexOf('field');
      const firstNameIndex = headers.indexOf('firstname');

      // retrieve only the fields, without repeats
      const fields = [...new Set(rows.map((row) => row.split(',')[fieldIndex]))];

      result += `Number of students: ${rows.length}\n`;

      fields.forEach((field) => {
        // split rows and retrieve field; if this matches current field, store
        // in students
        const students = rows.filter((row) => row.split(',')[fieldIndex] === field);
        // retrieve names and print them comma-separated
        result += `Number of students in ${field}: ${students.length}. List: ${students.map((student) => student.split(',')[firstNameIndex]).join(', ')}\n`;
      });
      return result;
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(process.argv[2])
    .then((data) => {
      res.send(`This is the list of our students\n${data}`);
    })
    .catch((err) => {
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(port, () => {
  console.log(`Listening on port ${port}.`);
});

module.exports = app;