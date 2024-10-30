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
    { id: 19, top: 500, left: 350, name: "Slot Machine 19", type: "x Slot", minBet: "$2" },
    { id: 20, top: 500, left: 350, name: "Slot Machine 20", type: "x Slot", minBet: "$2" },
    { id: 21, top: 100, left: 150, name: "Slot Machine 21", type: "x Slot", minBet: "$1" },
    { id: 22, top: 300, left: 250, name: "Slot Machine 22", type: "x Slot", minBet: "$5" },
    { id: 23, top: 100, left: 100, name: "Slot Machine 23", type: "x Slot", minBet: "$2" },
    { id: 24, top: 500, left: 350, name: "Slot Machine 24", type: "x Slot", minBet: "$2" },
    { id: 25, top: 500, left: 350, name: "Slot Machine 25", type: "x Slot", minBet: "$2" },
    { id: 26, top: 500, left: 350, name: "Slot Machine 26", type: "x Slot", minBet: "$2" },
    { id: 27, top: 500, left: 350, name: "Slot Machine 27", type: "x Slot", minBet: "$2" },
    { id: 28, top: 500, left: 350, name: "Slot Machine 28", type: "x Slot", minBet: "$2" },
    { id: 29, top: 500, left: 350, name: "Slot Machine 29", type: "x Slot", minBet: "$2" },
    { id: 30, top: 500, left: 350, name: "Slot Machine 30", type: "x Slot", minBet: "$2" },
    { id: 31, top: 100, left: 150, name: "Slot Machine 31", type: "x Slot", minBet: "$1" },
    { id: 32, top: 300, left: 250, name: "Slot Machine 32", type: "x Slot", minBet: "$5" },
    { id: 33, top: 100, left: 100, name: "Slot Machine 33", type: "x Slot", minBet: "$2" },
    { id: 34, top: 500, left: 350, name: "Slot Machine 34", type: "x Slot", minBet: "$2" },
    { id: 35, top: 500, left: 350, name: "Slot Machine 35", type: "x Slot", minBet: "$2" },
    { id: 36, top: 500, left: 350, name: "Slot Machine 36", type: "x Slot", minBet: "$2" },
    { id: 37, top: 500, left: 350, name: "Slot Machine 37", type: "x Slot", minBet: "$2" },
    { id: 38, top: 500, left: 350, name: "Slot Machine 38", type: "x Slot", minBet: "$2" },
    { id: 39, top: 500, left: 350, name: "Slot Machine 39", type: "x Slot", minBet: "$2" },
    { id: 40, top: 500, left: 350, name: "Slot Machine 40", type: "x Slot", minBet: "$2" },
    { id: 41, top: 100, left: 150, name: "Slot Machine 41", type: "x Slot", minBet: "$1" },
    { id: 42, top: 300, left: 250, name: "Slot Machine 42", type: "x Slot", minBet: "$5" },
    { id: 43, top: 100, left: 100, name: "Slot Machine 43", type: "x Slot", minBet: "$2" },
    { id: 44, top: 500, left: 350, name: "Slot Machine 44", type: "x Slot", minBet: "$2" },
    { id: 45, top: 500, left: 350, name: "Slot Machine 45", type: "x Slot", minBet: "$2" },
    { id: 46, top: 500, left: 350, name: "Slot Machine 46", type: "x Slot", minBet: "$2" },
    { id: 47, top: 500, left: 350, name: "Slot Machine 47", type: "x Slot", minBet: "$2" },
    { id: 48, top: 500, left: 350, name: "Slot Machine 48", type: "x Slot", minBet: "$2" },
    { id: 49, top: 500, left: 350, name: "Slot Machine 49", type: "x Slot", minBet: "$2" },
    { id: 50, top: 500, left: 350, name: "Slot Machine 50", type: "x Slot", minBet: "$2" }

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
