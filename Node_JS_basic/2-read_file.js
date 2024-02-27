// Defines function `countStudents`
const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    // split the data into rows and remove empty lines
    const rows = data.split('\n').filter((row) => row);

    // find index of field and firstName in csv
    const headers = rows.shift().split(',');
    const fieldIndex = headers.indexOf('field');
    const firstNameIndex = headers.indexOf('firstname');

    // retrieve only the fields, without repeats
    const fields = [...new Set(rows.map((row) => row.split(',')[fieldIndex]))];

    console.log(`Number of students: ${rows.length}`);

    fields.forEach((field) => {
      // split rows and retrieve field; if this matches current field, store
      // in students
      const students = rows.filter((row) => row.split(',')[fieldIndex] === field);
      // retrieve names and print them comma-separated
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.map((student) => student.split(',')[firstNameIndex]).join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;