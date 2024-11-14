const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const app = express();
const port = 3000;

app.use(express.static('public'));

// Open the database
const db = new sqlite3.Database('./db.sql');

// Middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint to get all slot machines
app.get('/api/slot-machines', (req, res) => {
    const query = `
        SELECT 
            machine_id, name, availability, average_session, 
            location, location_features, game_theme, game_type, 
            game_features, maximum_bet, minimum_bet, rtp, reward_program,
            top, left
        FROM slot_machines
    `;
    db.all(query, [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
