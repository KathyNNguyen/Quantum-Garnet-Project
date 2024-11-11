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
    { id: 66, top: 500, left: 350, name: "Slot Machine 66", type: "x Slot", minBet: "$2" },
    { id: 67, top: 500, left: 350, name: "Slot Machine 67", type: "x Slot", minBet: "$2" },
    { id: 68, top: 500, left: 350, name: "Slot Machine 68", type: "x Slot", minBet: "$2" },
    { id: 69, top: 500, left: 350, name: "Slot Machine 69", type: "x Slot", minBet: "$2" },
    { id: 70, top: 500, left: 350, name: "Slot Machine 70", type: "x Slot", minBet: "$2" },
    { id: 71, top: 500, left: 350, name: "Slot Machine 71", type: "x Slot", minBet: "$2" },
    { id: 72, top: 500, left: 350, name: "Slot Machine 72", type: "x Slot", minBet: "$2" },
    { id: 73, top: 500, left: 350, name: "Slot Machine 73", type: "x Slot", minBet: "$2" },
    { id: 74, top: 500, left: 350, name: "Slot Machine 74", type: "x Slot", minBet: "$2" },
    { id: 75, top: 500, left: 350, name: "Slot Machine 75", type: "x Slot", minBet: "$2" },
    { id: 76, top: 500, left: 350, name: "Slot Machine 76", type: "x Slot", minBet: "$2" },
    { id: 77, top: 500, left: 350, name: "Slot Machine 77", type: "x Slot", minBet: "$2" },
    { id: 78, top: 500, left: 350, name: "Slot Machine 78", type: "x Slot", minBet: "$2" },
    { id: 79, top: 500, left: 350, name: "Slot Machine 79", type: "x Slot", minBet: "$2" },
    { id: 80, top: 500, left: 350, name: "Slot Machine 80", type: "x Slot", minBet: "$2" },


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
