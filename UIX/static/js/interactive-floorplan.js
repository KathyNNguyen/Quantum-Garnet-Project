const container = document.getElementById('floorplan-container');

// array of slot machines with coordinates, names, and info
const machines = [
    { id: 1, top: 17.97, left: 11.66, name: "Slot Machine 1", type: "x Slot", minBet: "$1" },
    { id: 2, top: 28.05, left: 8.26, name: "Slot Machine 2", type: "x Slot", minBet: "$5" },
    { id: 3, top: 28.05, left: 15.69, name: "Slot Machine 3", type: "x Slot", minBet: "$2" },
    { id: 4, top: 11.84, left: 32.55, name: "Slot Machine 4", type: "x Slot", minBet: "$2" },
    { id: 5, top: 11.84, left: 35.32, name: "Slot Machine 5", type: "x Slot", minBet: "$2" },
    { id: 6, top: 11.84, left: 37.84, name: "Slot Machine 6", type: "x Slot", minBet: "$2" },
    { id: 7, top: 11.84, left: 40.35, name: "Slot Machine 7", type: "x Slot", minBet: "$2" },
    { id: 8, top: 11.84, left: 42.87, name: "Slot Machine 8", type: "x Slot", minBet: "$2" },
    { id: 9, top: 11.84, left: 45.26, name: "Slot Machine 9", type: "x Slot", minBet: "$2" },
    { id: 10, top: 11.84, left: 47.65, name: "Slot Machine 10", type: "x Slot", minBet: "$2" },
    { id: 11, top: 11.84, left: 50.17, name: "Slot Machine 11", type: "x Slot", minBet: "$2" },
    { id: 12, top: 11.84, left: 52.68, name: "Slot Machine 12", type: "x Slot", minBet: "$2" },
    { id: 13, top: 11.84, left: 55.08, name: "Slot Machine 13", type: "x Slot", minBet: "$2" },
    { id: 14, top: 11.84, left: 57.47, name: "Slot Machine 14", type: "x Slot", minBet: "$2" },
    { id: 15, top: 11.84, left: 59.98, name: "Slot Machine 15", type: "x Slot", minBet: "$2" },
    { id: 16, top: 11.84, left: 62.63, name: "Slot Machine 16", type: "x Slot", minBet: "$2" },
    { id: 17, top: 11.84, left: 65.14, name: "Slot Machine 17", type: "x Slot", minBet: "$2" },
    { id: 18, top: 11.84, left: 67.41, name: "Slot Machine 18", type: "x Slot", minBet: "$2" },
    { id: 19, top: 23.67, left: 37.58, name: "Slot Machine 19", type: "x Slot", minBet: "$2" },
    { id: 20, top: 23.67, left: 39.97, name: "Slot Machine 20", type: "x Slot", minBet: "$2" },
    { id: 21, top: 23.67, left: 62.37, name: "Slot Machine 21", type: "x Slot", minBet: "$1" },
    { id: 22, top: 23.67, left: 64.89, name: "Slot Machine 22", type: "x Slot", minBet: "$5" },
    { id: 23, top: 30.68, left: 37.58, name: "Slot Machine 23", type: "x Slot", minBet: "$2" },
    { id: 24, top: 30.68, left: 39.97, name: "Slot Machine 24", type: "x Slot", minBet: "$2" },
    { id: 25, top: 30.68, left: 62.37, name: "Slot Machine 25", type: "x Slot", minBet: "$2" },
    { id: 26, top: 30.68, left: 64.89, name: "Slot Machine 26", type: "x Slot", minBet: "$2" },
    { id: 27, top: 26.96, left: 35.07, name: "Slot Machine 27", type: "x Slot", minBet: "$2" },
    { id: 28, top: 26.96, left: 42.37, name: "Slot Machine 28", type: "x Slot", minBet: "$2" },
    { id: 29, top: 26.96, left: 59.98, name: "Slot Machine 29", type: "x Slot", minBet: "$2" },
    { id: 30, top: 26.96, left: 67.28, name: "Slot Machine 30", type: "x Slot", minBet: "$2" },
    { id: 31, top: 23.67, left: 49.29, name: "Slot Machine 31", type: "x Slot", minBet: "$1" },
    { id: 32, top: 23.67, left: 52.68, name: "Slot Machine 32", type: "x Slot", minBet: "$5" },
    { id: 33, top: 29.81, left: 49.29, name: "Slot Machine 33", type: "x Slot", minBet: "$2" },
    { id: 34, top: 29.81, left: 52.68, name: "Slot Machine 34", type: "x Slot", minBet: "$2" },
    { id: 35, top: 30.03, left: 74.08, name: "Slot Machine 35", type: "x Slot", minBet: "$2" },
    { id: 36, top: 30.03, left: 76.59, name: "Slot Machine 36", type: "x Slot", minBet: "$2" },
    { id: 37, top: 30.03, left: 79.24, name: "Slot Machine 37", type: "x Slot", minBet: "$2" },
    { id: 38, top: 30.03, left: 81.63, name: "Slot Machine 38", type: "x Slot", minBet: "$2" },
    { id: 39, top: 30.03, left: 84.14, name: "Slot Machine 39", type: "x Slot", minBet: "$2" },
    { id: 40, top: 30.03, left: 86.66, name: "Slot Machine 40", type: "x Slot", minBet: "$2" },
    { id: 41, top: 30.03, left: 89.05, name: "Slot Machine 41", type: "x Slot", minBet: "$2" },
    { id: 42, top: 44.27, left: 2.6, name: "Slot Machine 42", type: "x Slot", minBet: "$5" },
    { id: 43, top: 48.44, left: 2.6, name: "Slot Machine 43", type: "x Slot", minBet: "$2" },
    { id: 44, top: 53.04, left: 2.6, name: "Slot Machine 44", type: "x Slot", minBet: "$2" },
    { id: 45, top: 57.42, left: 2.6, name: "Slot Machine 45", type: "x Slot", minBet: "$2" },
    { id: 46, top: 61.81, left: 2.6, name: "Slot Machine 46", type: "x Slot", minBet: "$2" },
    { id: 47, top: 65.75, left: 2.6, name: "Slot Machine 47", type: "x Slot", minBet: "$2" },
    { id: 48, top: 47.78, left: 11.54, name: "Slot Machine 48", type: "x Slot", minBet: "$2" },
    { id: 49, top: 60.27, left: 11.54, name: "Slot Machine 49", type: "x Slot", minBet: "$2" },
    { id: 50, top: 51.72, left: 9.65, name: "Slot Machine 50", type: "x Slot", minBet: "$2" },
    { id: 51, top: 55.89, left: 9.65, name: "Slot Machine 51", type: "x Slot", minBet: "$2" },
    { id: 52, top: 51.72, left: 13.42, name: "Slot Machine 52", type: "x Slot", minBet: "$2" },
    { id: 53, top: 55.89, left: 13.42, name: "Slot Machine 53", type: "x Slot", minBet: "$2" },
    { id: 54, top: 44.27, left: 21.48, name: "Slot Machine 54", type: "x Slot", minBet: "$2" },
    { id: 55, top: 48.44, left: 21.48, name: "Slot Machine 55", type: "x Slot", minBet: "$2" },
    { id: 56, top: 52.60, left: 21.48, name: "Slot Machine 56", type: "x Slot", minBet: "$2" },
    { id: 57, top: 56.98, left: 21.48, name: "Slot Machine 57", type: "x Slot", minBet: "$2" },
    { id: 58, top: 61.37, left: 21.48, name: "Slot Machine 58", type: "x Slot", minBet: "$2" },
    { id: 59, top: 73.86, left: 6.38, name: "Slot Machine 59", type: "x Slot", minBet: "$2" },
    { id: 60, top: 73.86, left: 8.89, name: "Slot Machine 60", type: "x Slot", minBet: "$2" },
    { id: 61, top: 73.86, left: 11.28, name: "Slot Machine 61", type: "x Slot", minBet: "$2" },
    { id: 62, top: 73.86, left: 13.80, name: "Slot Machine 62", type: "x Slot", minBet: "$2" },
    { id: 63, top: 73.86, left: 16.19, name: "Slot Machine 63", type: "x Slot", minBet: "$2" },
    { id: 64, top: 73.86, left: 18.71, name: "Slot Machine 64", type: "x Slot", minBet: "$2" },
    { id: 65, top: 73.86, left: 21.22, name: "Slot Machine 65", type: "x Slot", minBet: "$2" },
    { id: 66, top: 44.27, left: 33.05, name: "Slot Machine 66", type: "x Slot", minBet: "$2" },
    { id: 67, top: 48.66, left: 33.05, name: "Slot Machine 67", type: "x Slot", minBet: "$2" },
    { id: 68, top: 52.60, left: 33.05, name: "Slot Machine 68", type: "x Slot", minBet: "$2" },
    { id: 69, top: 57.20, left: 33.05, name: "Slot Machine 69", type: "x Slot", minBet: "$2" },
    { id: 70, top: 61.59, left: 33.05, name: "Slot Machine 70", type: "x Slot", minBet: "$2" },
    { id: 71, top: 65.53, left: 33.05, name: "Slot Machine 71", type: "x Slot", minBet: "$2" },
    { id: 72, top: 70.57, left: 33.05, name: "Slot Machine 72", type: "x Slot", minBet: "$2" },
    { id: 73, top: 74.74, left: 33.05, name: "Slot Machine 73", type: "x Slot", minBet: "$2" },
    { id: 74, top: 47.12, left: 47.02, name: "Slot Machine 74", type: "x Slot", minBet: "$2" },
    { id: 75, top: 72.77, left: 47.02, name: "Slot Machine 75", type: "x Slot", minBet: "$2" },
    { id: 76, top: 51.29, left: 45.13, name: "Slot Machine 76", type: "x Slot", minBet: "$2" },
    { id: 77, top: 55.67, left: 45.13, name: "Slot Machine 77", type: "x Slot", minBet: "$2" },
    { id: 78, top: 60.05, left: 45.13, name: "Slot Machine 78", type: "x Slot", minBet: "$2" },
    { id: 79, top: 64.00, left: 45.13, name: "Slot Machine 79", type: "x Slot", minBet: "$2" },
    { id: 80, top: 68.38, left: 45.13, name: "Slot Machine 80", type: "x Slot", minBet: "$2" },
    { id: 81, top: 51.29, left: 49.04, name: "Slot Machine 81", type: "x Slot", minBet: "$2" },
    { id: 82, top: 55.67, left: 49.04, name: "Slot Machine 82", type: "x Slot", minBet: "$2" },
    { id: 83, top: 60.05, left: 49.04, name: "Slot Machine 83", type: "x Slot", minBet: "$2" },
    { id: 84, top: 64.00, left: 49.04, name: "Slot Machine 84", type: "x Slot", minBet: "$2" },
    { id: 85, top: 68.38, left: 49.04, name: "Slot Machine 85", type: "x Slot", minBet: "$2" },
    { id: 86, top: 52.82, left: 62.00, name: "Slot Machine 86", type: "x Slot", minBet: "$2" },
    { id: 87, top: 59.40, left: 62.00, name: "Slot Machine 87", type: "x Slot", minBet: "$2" },
    { id: 88, top: 52.82, left: 71.18, name: "Slot Machine 88", type: "x Slot", minBet: "$2" },
    { id: 89, top: 59.18, left: 71.18, name: "Slot Machine 89", type: "x Slot", minBet: "$2" },
    { id: 90, top: 52.60, left: 80.49, name: "Slot Machine 90", type: "x Slot", minBet: "$2" },
    { id: 91, top: 59.18, left: 80.49, name: "Slot Machine 91", type: "x Slot", minBet: "$2" },
    { id: 92, top: 52.16, left: 89.43, name: "Slot Machine 92", type: "x Slot", minBet: "$2" },
    { id: 93, top: 59.00, left: 89.65, name: "Slot Machine 93", type: "x Slot", minBet: "$2" },
    { id: 94, top: 75.18, left: 64.01, name: "Slot Machine 94", type: "x Slot", minBet: "$2" },
    { id: 95, top: 81.53, left: 64.01, name: "Slot Machine 95", type: "x Slot", minBet: "$2" },
    { id: 96, top: 75.18, left: 67.53, name: "Slot Machine 96", type: "x Slot", minBet: "$2" },
    { id: 97, top: 81.09, left: 67.53, name: "Slot Machine 97", type: "x Slot", minBet: "$2" },
    { id: 98, top: 73.64, left: 76.34, name: "Slot Machine 98", type: "x Slot", minBet: "$2" },
    { id: 99, top: 82.63, left: 76.34, name: "Slot Machine 99", type: "x Slot", minBet: "$2" },
    { id: 100, top: 78.24, left: 74.08, name: "Slot Machine 100", type: "x Slot", minBet: "$2" },
    { id: 101, top: 78.03, left: 78.86, name: "Slot Machine 101", type: "x Slot", minBet: "$2" },
    { id: 102, top: 74.52, left: 84.90, name: "Slot Machine 102", type: "x Slot", minBet: "$2" },
    { id: 103, top: 80.66, left: 84.90, name: "Slot Machine 103", type: "x Slot", minBet: "$2" },
    { id: 104, top: 74.74, left: 88.42, name: "Slot Machine 104", type: "x Slot", minBet: "$2" },
    { id: 105, top: 80.66, left: 88.55, name: "Slot Machine 105", type: "x Slot", minBet: "$2" },
    { id: 106, top: 94.90, left: 60.23, name: "Slot Machine 106", type: "x Slot", minBet: "$2" },
    { id: 107, top: 94.90, left: 62.63, name: "Slot Machine 107", type: "x Slot", minBet: "$2" },
    { id: 108, top: 94.90, left: 65.27, name: "Slot Machine 108", type: "x Slot", minBet: "$2" },
    { id: 109, top: 94.90, left: 67.66, name: "Slot Machine 109", type: "x Slot", minBet: "$2" },
    { id: 110, top: 94.90, left: 70.18, name: "Slot Machine 110", type: "x Slot", minBet: "$2" },
    { id: 111, top: 94.90, left: 72.57, name: "Slot Machine 111", type: "x Slot", minBet: "$2" },
    { id: 112, top: 94.90, left: 74.96, name: "Slot Machine 112", type: "x Slot", minBet: "$2" },
    { id: 113, top: 94.90, left: 77.60, name: "Slot Machine 113", type: "x Slot", minBet: "$2" },
    { id: 114, top: 94.90, left: 79.87, name: "Slot Machine 114", type: "x Slot", minBet: "$2" },
    { id: 115, top: 94.90, left: 82.38, name: "Slot Machine 115", type: "x Slot", minBet: "$2" },
    { id: 116, top: 94.90, left: 84.90, name: "Slot Machine 116", type: "x Slot", minBet: "$2" },
    { id: 117, top: 94.90, left: 87.42, name: "Slot Machine 117", type: "x Slot", minBet: "$2" },
    { id: 118, top: 94.90, left: 89.93, name: "Slot Machine 118", type: "x Slot", minBet: "$2" },
    { id: 119, top: 94.90, left: 92.45, name: "Slot Machine 119", type: "x Slot", minBet: "$2" },

];

// function to create interactive stars and tooltips
function addInteractiveStars() {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.style.display = 'none';
    container.appendChild(tooltip);

    machines.forEach(machine => {
        // create the star element
        const star = document.createElement('div');
        star.className = 'interactive-star';
        star.style.left = `${machine.left}%`;
        star.style.top = `${machine.top}%`;       
        star.setAttribute('data-id', machine.id);

        // append both elements to the container
        container.appendChild(star);

        // displaying the tooltip
        star.addEventListener('mouseenter', () => {
            tooltip.style.display = 'block';
            tooltip.innerText = `${machine.name}\nType: ${machine.type}\nMin Bet: ${machine.minBet}`;
            tooltip.style.left = `${machine.left}px`;
            tooltip.style.top = `${machine.top - 30}px`;
        });

        // hiding the tooltip
        star.addEventListener('mouseleave', () => {
            tooltip.style.display = 'none';
        });
    });
}

// call the function to add stars when the page loads
window.onload = addInteractiveStars;
