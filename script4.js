// script4.js

function calculatePercentage(gpa) {
    if (isNaN(gpa) || gpa < 0 || gpa > 4) {
        return "Invalid input. Please enter a valid GPA between 0.00 and 4.00.";
    }

    const percentageMapping = [
        { minGPA: 3.90, maxGPA: 4.00, percentage: 95 },
        { minGPA: 3.70, maxGPA: 3.89,percentage: 85},
        { minGPA: 3.30, maxGPA: 3.69, percentage: 80 },
        { minGPA: 3.00, maxGPA: 3.29, percentage: 77 },
        { minGPA: 2.70, maxGPA: 2.99, percentage: 73 },
        { minGPA: 2.30, maxGPA: 2.69, percentage: 70 },
        { minGPA: 2.00, maxGPA: 2.29, percentage: 67 },
        { minGPA: 1.7, maxGPA: 1.99, percentage: 63 },
        { minGPA: 0.00, maxGPA: 1.69, percentage: 0.00},
    ];

    for (const mapping of percentageMapping) {
        if (gpa >= mapping.minGPA && gpa <= mapping.maxGPA) {
            return mapping.percentage;
        }
    }

    return "Error: Unable to calculate percentage.";
}

function calculateAndDisplayPercentage() {
    const gpaInput = document.getElementById('gpaInput');
    const resultElement = document.getElementById('percentageResult');

    const gpa = parseFloat(gpaInput.value);
    const percentage = calculatePercentage(gpa);

    resultElement.textContent = `For a GPA of ${gpa.toFixed(2)}, the corresponding percentage is ${percentage}%.`;
}

function calculateGPA(percentage) {
    if (isNaN(percentage) || percentage < 0 || percentage > 100) {
        return "Invalid input. Please enter a valid percentage between 0 and 100.";
    }

    const gpaMapping = [
        { minPercentage: 90, maxPercentage: 100,gpa: 4.00 },
        { minPercentage: 85, maxPercentage: 89, gpa: 3.80 },
        { minPercentage: 80, maxPercentage: 84, gpa: 3.70 },
        { minPercentage: 77, maxPercentage: 79, gpa: 3.30 },
        { minPercentage: 73, maxPercentage: 76, gpa: 3.00 },
        { minPercentage: 70, maxPercentage: 72, gpa: 2.70 },
        { minPercentage: 67, maxPercentage: 69, gpa: 2.30 },
        { minPercentage: 63, maxPercentage: 66, gpa: 2.00 },
        { minPercentage: 60, maxPercentage: 62, gpa: 1.70 },
        { minPercentage: 0, maxPercentage: 59, gpa: 0.00 },

    ];

    for (const mapping of gpaMapping) {
        if (percentage >= mapping.minPercentage && percentage <= mapping.maxPercentage) {
            return mapping.gpa.toFixed(2);
        }
    }

    return "Error: Unable to calculate GPA.";
}

function calculateAndDisplayGPA() {
    const percentageInput = document.getElementById('percentageInput');
    const resultElement = document.getElementById('gpaResult');

    const percentage = parseFloat(percentageInput.value);
    const gpa = calculateGPA(percentage);

    resultElement.textContent = `For a percentage of ${percentage}%, the corresponding GPA is ${gpa}.`;
}
