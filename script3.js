// Script for the third calculator (Total Grade Calculator)

function addGradeSlot3() {
    const gradeTable = document.querySelector('#totalGradeCalculator table');
    const newRow = gradeTable.insertRow(-1);

    newRow.innerHTML = `
        <td><input type="text" class="gradeType" placeholder="Assignment, Quiz, Exam"></td>
        <td><input type="number" class="gradeWeight" min="0" max="100" step="0.01"></td>
        <td><input type="number" class="grade" min="0" max="100" step="0.01"></td>
        <td><button type="button" onclick="removeGradeSlot3(this)">Remove</button></td>
    `;
}

function removeGradeSlot3(button) {
    const gradeTable = document.querySelector('#totalGradeCalculator table');
    const rowIndex = button.parentNode.parentNode.rowIndex;
    gradeTable.deleteRow(rowIndex);
}

function calculateGrade3() {
    const gradeRows = document.querySelectorAll('#totalGradeCalculator .grade-input');
    let totalWeight = 0;
    let totalScore = 0;

    gradeRows.forEach(row => {
        const gradeWeight = parseFloat(row.querySelector('.gradeWeight').value);
        const grade = parseFloat(row.querySelector('.grade').value);

        if (!isNaN(gradeWeight) && !isNaN(grade)) {
            totalWeight += gradeWeight;
            totalScore += (gradeWeight * grade) / 100;
        }
    });

    const finalGrade = totalWeight > 0 ? (totalScore / totalWeight) * 100 : 0;

    const warningElement = document.getElementById('warning3');
    const finalGradeElement = document.getElementById('finalGrade3');

    if (totalWeight !== 100) {
        warningElement.textContent = "Warning: The total percentage weight of all submissions is not 100%. Are you sure you didn't forget an assignment?";
        finalGradeElement.textContent = "";
    } else {
        warningElement.textContent = "";
        finalGradeElement.textContent = `Your final percentage grade is: ${finalGrade.toFixed(2)}%`;
    }
}
