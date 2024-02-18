// Script for the second calculator (Semester Calculator)

function addGradeSlot2() {
    const gradeTable = document.querySelector('#semesterCalculator table');
    const newRow = gradeTable.insertRow(-1);

    newRow.innerHTML = `
        <td><input type="text" class="gradeType" placeholder="Assignment, Quiz, Exam"></td>
        <td><input type="number" class="grade" min="0" max="100" step="0.01"></td>
        <td><button type="button" onclick="removeGradeSlot2(this)">Remove</button></td>
    `;
}

function removeGradeSlot2(button) {
    const gradeTable = document.querySelector('#semesterCalculator table');
    const rowIndex = button.parentNode.parentNode.rowIndex;
    gradeTable.deleteRow(rowIndex);
}

function calculateGrade2() {
    const gradeRows = document.querySelectorAll('#semesterCalculator .grade-input');
    let totalScore = 0;

    gradeRows.forEach(row => {
        const grade = parseFloat(row.querySelector('.grade').value);

        if (!isNaN(grade)) {
            totalScore += grade;
        }
    });

    const finalGrade = gradeRows.length > 0 ? totalScore / gradeRows.length : 0;

    const warningElement = document.getElementById('warning2');
    const finalGradeElement = document.getElementById('finalGrade2');

    warningElement.textContent = ""; // Remove any existing warnings

    finalGradeElement.textContent = `Your final percentage grade for the semester is: ${finalGrade.toFixed(2)}%`;
}
