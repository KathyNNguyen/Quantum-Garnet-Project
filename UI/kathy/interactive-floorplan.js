// array of slot machines with coordinates, names, and info
const machines = [
    { id: 1, top: 100, left: 150, name: "Slot Machine 1", type: "Classic Slot", minBet: "$1" },
    { id: 2, top: 300, left: 250, name: "Slot Machine 2", type: "Progressive Slot", minBet: "$5" },
    { id: 3, top: 500, left: 350, name: "Slot Machine 3", type: "Video Slot", minBet: "$2" }
];

// function to create interactive stars and tooltips
function addInteractiveStars() {
    const container = document.querySelector('.floorplan-container');

    machines.forEach(machine => {
        // create the star element
        const star = document.createElement('div');
        star.className = 'interactive-star';
        star.style.top = `${machine.top}px`;
        star.style.left = `${machine.left}px`;

        // create the tooltip element
        const tooltip = document.createElement('div');
        tooltip.className = 'tooltip';
        tooltip.style.top = `${machine.top}px`;
        tooltip.style.left = `${machine.left + 40}px`; // Adjust tooltip offset
        tooltip.innerHTML = `${machine.name}: <br> Type: ${machine.type} <br> Min Bet: ${machine.minBet}`;

        // append both elements to the container
        container.appendChild(star);
        container.appendChild(tooltip);
    });
}

// call the function to add stars when the page loads
window.onload = addInteractiveStars;
