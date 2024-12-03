const container = document.getElementById("floorplan-container");

// function to add interactive stars dynamically from API data
function addInteractiveStars() {
  // fetch slot machine data from the server
  fetch("/api/slot-machines")
    .then((response) => response.json())
    .then((data) => {
      // loop through each slot machine and create the interactive star.
      data.forEach((machine) => {
        const star = document.createElement("div");
        star.className = "interactive-star";
        star.style.left = `${machine.left}%`;
        star.style.top = `${machine.top}%`;
        star.setAttribute("data-id", machine.machine_id);
        star.setAttribute("data-name", machine.name.toLowerCase());

        const tooltip = document.createElement("div");
        tooltip.className = "tooltip";
        tooltip.style.display = "none";

        // displaying the tooltip.
        star.addEventListener("mouseenter", () => {
          tooltip.style.display = "block";
          tooltip.innerHTML = `
                        <strong>${machine.name}</strong><br>
                        Type: ${machine.game_type}<br>
                        Min Bet: $${machine.minimum_bet}
                    `;
          tooltip.style.left = `${parseFloat(machine.left)}%`;
          tooltip.style.top = `${parseFloat(machine.top) - 5}%`;
        });

        // hiding the tooltip.
        star.addEventListener("mouseleave", () => {
          tooltip.style.display = "none";
        });

        // append both elements to the container.
        container.appendChild(star);
        container.appendChild(tooltip);
      });
    })
    .catch((error) => console.error("Error fetching slot machines:", error));
}

//Search bar querying the data.
const searchMachineTemplate = document.querySelector("[data-machine-template]");
const searchMachineContainer = document.querySelector(
  "[data-machine-display-container]"
);
const searchInput = document.querySelector("[data-search]");

let machinesS = [];
let interactiveStars = [];

searchInput.addEventListener("input", (e) => {
  const value = e.target.value.toLowerCase();

  // Filter machines in the search list.
  machinesS.forEach((machine) => {
    const isVisible = machine.name.toLowerCase().includes(value);
    machine.element.classList.toggle("hide", !isVisible);
  });

  // Filter interactive stars on the map.
  interactiveStars.forEach((star) => {
    const isVisible = star.dataset.name.includes(value);
    star.classList.toggle("hide", !isVisible);
  });
});

fetch("/api/slot-machines")
  .then((res) => res.json())
  .then((data) => {
    machinesS = data.map((machine) => {
      const searchDisplay =
        searchMachineTemplate.content.cloneNode(true).children[0];
      const header = searchDisplay.querySelector("[machine-header]");
      const body = searchDisplay.querySelector("[machine-body]");
      header.textContent = machine.name;
      body.textContent =
        "min: " + machine.minimum_bet + "  max: " + machine.maximum_bet;
      searchMachineContainer.append(searchDisplay);
      return {
        name: machine.name,
        minimum_bet: machine.minimum_bet,
        maximum_bet: machine.maximum_bet,
        element: searchDisplay,
      };
    });
  });

function addInteractiveStars() {
  fetch("/api/slot-machines")
    .then((response) => response.json())
    .then((data) => {
      data.forEach((machine) => {
        const star = document.createElement("div");
        star.className = "interactive-star";
        star.style.left = `${machine.left}%`;
        star.style.top = `${machine.top}%`;
        star.setAttribute("data-id", machine.machine_id);
        star.setAttribute("data-name", machine.name.toLowerCase());

        const tooltip = document.createElement("div");
        tooltip.className = "tooltip";
        tooltip.style.display = "none";

        star.addEventListener("mouseenter", () => {
          tooltip.style.display = "block";
          tooltip.innerHTML = `
                        <strong>${machine.name}</strong><br>
                        Type: ${machine.game_type}<br>
                        Min Bet: $${machine.minimum_bet}
                    `;
          tooltip.style.left = `${parseFloat(machine.left)}%`;
          tooltip.style.top = `${parseFloat(machine.top) - 5}%`;
        });

        star.addEventListener("mouseleave", () => {
          tooltip.style.display = "none";
        });

        // Store star in the interactiveStars array.
        interactiveStars.push(star);

        container.appendChild(star);
        container.appendChild(tooltip);
      });
    })
    .catch((error) => console.error("Error fetching slot machines:", error));
}

// load stars after the window loads.
window.onload = addInteractiveStars;
