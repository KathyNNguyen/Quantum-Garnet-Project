import sqlite3
import os

db_path = os.path.abspath("UIX/slot_machines.db")

updated_slot_machines = [
(51, 'Atlantis Adventure', 0, 120.45, 'Star51', '["bathroom", "central"]', 'Ocean', 'Progressive Slots', '["high_roller_spins", "bonus_rounds"]', 312.23, 2.34, 92.50, 1),
(52, 'Jungle Madness', 1, 75.12, 'Star52', '["entrance", "decoration"]', 'Jungle', 'Megaways', '["walking_wilds", "vip_bonuses"]', 220.41, 3.15, 90.87, 0),
(53, 'Stellar Spins', 1, 88.96, 'Star53', '["table_service", "bar"]', 'Sci-Fi', 'Bonus Slots', '["cascading_reels", "adjacent_pays", "stacked_wilds"]', 187.33, 2.72, 94.13, 1),
(54, 'Forbidden Treasure', 0, 96.22, 'Star54', '["bathroom", "restaurant"]', 'Pirate', '3D Slots', '["scatter_symbols", "symbol_transformations"]', 277.89, 1.88, 91.26, 0),
(55, 'Fantasy Legend', 1, 79.88, 'Star55', '["walkway_adjacent", "entrance"]', 'Fantasy', 'Classic Slots', '["free_spins", "random_wilds"]', 184.65, 3.33, 89.67, 0),
(56, 'Western Showdown', 1, 94.34, 'Star56', '["table_service", "central"]', 'Wild West', 'Video Slots', '["re_spins", "pick_and_click"]', 102.44, 2.04, 93.77, 1),
(57, 'Mythic Realms', 0, 68.44, 'Star57', '["bar", "bathroom"]', 'Fantasy', 'Megaways', '["sticky_wilds", "bonus_rounds"]', 344.18, 2.98, 92.21, 0),
(58, 'Neon Nights', 1, 82.67, 'Star58', '["central", "entrance"]', 'Sci-Fi', 'Themed Slots', '["gamble_feature", "scatter_symbols"]', 219.34, 1.56, 90.05, 1),
(59, 'Lucky Fortune', 1, 90.19, 'Star59', '["decoration", "restaurant"]', 'Fruit', 'Progressive Slots', '["themed_bonus_rounds"]', 97.11, 2.44, 91.88, 0),
(60, 'Pirate\s Legacy', 0, 115.32, 'Star60', '["walkway_adjacent", "bathroom"]', 'Pirate', 'Megaways', '["colossal_symbols", "stacked_wilds"]', 307.62, 3.22, 92.73, 0),
(61, 'Egyptian Secrets', 0, 77.45, 'Star61', '["bar", "central"]', 'Egyptian', 'Classic Slots', '["pick_and_click", "scatter_symbols"]', 250.17, 1.99, 89.43, 1),
(62, 'Jungle Treasures II', 1, 69.33, 'Star62', '["entrance", "restaurant"]', 'Jungle', 'Bonus Slots', '["wild_symbols", "bonus_rounds"]', 275.21, 4.01, 90.50, 0),
(63, 'Sci-Fi Saga', 0, 85.60, 'Star63', '["table_service", "bathroom"]', 'Sci-Fi', 'Themed Slots', '["megaways", "walking_wilds"]', 201.53, 2.31, 91.70, 1),
(64, 'Treasure Hunt', 1, 74.10, 'Star64', '["decoration", "central"]', 'Adventure', '3D Slots', '["gamble_feature", "scatter_symbols"]', 199.38, 2.90, 93.01, 1),
(65, 'Moonlight Magic', 0, 54.87, 'Star65', '["bar", "walkway_adjacent"]', 'Fantasy', 'Megaways', '["pick_and_click", "bonus_rounds"]', 282.78, 3.02, 90.17, 0),
(66, 'Royal Riches', 1, 71.21, 'Star66', '["restaurant", "central"]', 'Egyptian', 'Bonus Slots', '["wild_symbols", "high_roller_spins"]', 305.45, 2.55, 92.25, 1),
(67, 'Wild Hunt', 0, 62.34, 'Star67', '["entrance", "table_service"]', 'Wild West', 'Classic Slots', '["re_spins", "bonus_rounds"]', 150.22, 2.84, 90.01, 0),
(68, 'Oceanic Oddities', 1, 99.38, 'Star68', '["bathroom", "bar"]', 'Ocean', 'Megaways', '["vip_bonuses", "seasonal_features"]', 244.99, 2.08, 93.87, 0),
(69, 'Galactic Glory', 1, 117.10, 'Star69', '["restaurant", "bar"]', 'Sci-Fi', '3D Slots', '["sticky_wilds", "scatter_symbols"]', 211.44, 1.65, 91.99, 1),
(70, 'Treasure Island', 0, 93.45, 'Star70', '["walkway_adjacent", "central"]', 'Pirate', 'Themed Slots', '["expanding_wilds", "high_roller_spins"]', 190.63, 2.76, 89.15, 0),
(71, 'Adventure Awaits II', 1, 111.56, 'Star71', '["bathroom", "bar"]', 'Adventure', 'Video Slots', '["adjacent_pays", "bonus_rounds"]', 210.11, 1.87, 92.55, 1),
(72, 'Mystic Maze', 1, 73.44, 'Star72', '["central", "table_service"]', 'Fantasy', '3D Slots', '["walking_wilds", "seasonal_features"]', 333.19, 1.98, 91.02, 0),
(73, 'Cosmic Quest', 0, 91.67, 'Star73', '["bar", "restaurant"]', 'Sci-Fi', 'Megaways', '["scatter_symbols", "gamble_feature"]', 284.10, 1.11, 93.30, 1),
(74, 'Jungle Jewel', 1, 55.34, 'Star74', '["entrance", "walkway_adjacent"]', 'Jungle', 'Progressive Slots', '["stacked_wilds", "adjacent_pays"]', 227.98, 2.88, 89.99, 0),
(75, 'Sunken Secrets', 0, 104.45, 'Star75', '["walkway_adjacent", "bathroom"]', 'Ocean', 'Bonus Slots', '["megaways", "free_spins"]', 177.33, 2.99, 90.85, 1),
(76, 'Starry Jackpot', 1, 113.89, 'Star76', '["table_service", "restaurant"]', 'Sci-Fi', 'Bonus Slots', '["cascading_reels", "wild_symbols"]', 157.89, 1.85, 92.14, 0),
(77, 'Ancient Relics', 0, 87.33, 'Star77', '["restaurant", "central"]', 'Egyptian', 'Themed Slots', '["re_spins", "progressive_jackpot"]', 345.67, 3.40, 88.70, 1),
(78, 'Fantasy Forest', 1, 99.10, 'Star78', '["central", "decoration"]', 'Fantasy', 'Classic Slots', '["bonus_rounds", "wild_symbols"]', 223.90, 2.88, 91.23, 0),
(79, 'Golden Crown', 1, 74.22, 'Star79', '["walkway_adjacent", "entrance"]', 'Egyptian', 'Video Slots', '["scatter_symbols", "pick_and_click"]', 311.89, 3.04, 89.91, 1),
(80, 'Lost Atlantis', 0, 120.34, 'Star80', '["bathroom", "central"]', 'Ocean', 'Progressive Slots', '["sticky_wilds", "wild_symbols"]', 324.88, 3.50, 91.70, 0),
(81, 'Jungle Joy', 1, 82.50, 'Star81', '["restaurant", "walkway_adjacent"]', 'Jungle', 'Classic Slots', '["adjacent_pays", "vip_bonuses"]', 300.45, 2.78, 91.88, 1),
(82, 'Neptune Wrath', 0, 110.23, 'Star82', '["central", "bar"]', 'Ocean', '3D Slots', '["symbol_transformations", "scatter_symbols"]', 366.22, 1.92, 94.25, 1),
(83, 'Pharaoh Wrath', 1, 98.44, 'Star83', '["walkway_adjacent", "decoration"]', 'Egyptian', 'Bonus Slots', '["free_spins", "bonus_rounds"]', 251.89, 3.23, 90.60, 0),
(84, 'Cosmic Conquest', 0, 122.67, 'Star84', '["entrance", "bathroom"]', 'Sci-Fi', 'Megaways', '["seasonal_features", "stacked_wilds"]', 244.77, 1.78, 93.15, 1),
(85, 'Royal Fortune', 0, 88.33, 'Star85', '["bar", "walkway_adjacent"]', 'Pirate', 'Classic Slots', '["scatter_symbols", "sticky_wilds"]', 290.45, 2.40, 91.44, 0),
(86, 'Fantasy Dreams', 1, 90.78, 'Star86', '["restaurant", "central"]', 'Fantasy', '3D Slots', '["bonus_rounds", "wild_symbols"]', 189.45, 2.99, 91.00, 1),
(87, 'Western Wonders', 1, 75.11, 'Star87', '["bathroom", "restaurant"]', 'Wild West', 'Megaways', '["progressive_jackpot", "high_roller_spins"]', 320.90, 2.77, 93.33, 0),
(88, 'Ocean Treasures', 0, 94.88, 'Star88', '["central", "bar"]', 'Ocean', 'Themed Slots', '["colossal_symbols", "walking_wilds"]', 270.88, 3.45, 92.40, 1),
(89, 'Galactic Chase', 1, 89.77, 'Star89', '["entrance", "table_service"]', 'Sci-Fi', 'Progressive Slots', '["bonus_rounds", "scatter_symbols"]', 333.99, 3.66, 94.11, 0),
(90, 'Pirate\s Booty', 0, 117.99, 'Star90', '["walkway_adjacent", "restaurant"]', 'Pirate', '3D Slots', '["symbol_transformations", "sticky_wilds"]', 200.34, 1.88, 91.80, 0),
(91, 'Golden Pyramid', 1, 80.22, 'Star91', '["central", "entrance"]', 'Egyptian', 'Video Slots', '["scatter_symbols", "progressive_jackpot"]', 188.89, 1.92, 89.78, 1),
(92, 'Oceanic Treasures', 0, 106.45, 'Star92', '["table_service", "bar"]', 'Ocean', 'Bonus Slots', '["colossal_symbols", "scatter_symbols"]', 344.99, 3.21, 93.77, 1),
(93, 'Jungle Gem II', 1, 64.33, 'Star93', '["bathroom", "entrance"]', 'Jungle', 'Classic Slots', '["wild_symbols", "bonus_rounds"]', 222.11, 2.99, 91.43, 0),
(94, 'Cosmic Fortune', 1, 97.23, 'Star94', '["restaurant", "walkway_adjacent"]', 'Sci-Fi', 'Themed Slots', '["scatter_symbols", "vip_bonuses"]', 277.34, 1.88, 93.11, 1),
(95, 'Fantasy Riches', 0, 73.45, 'Star95', '["decoration", "bathroom"]', 'Fantasy', 'Bonus Slots', '["pick_and_click", "walking_wilds"]', 310.78, 2.21, 90.45, 0),
(96, 'Galactic Journey', 1, 113.12, 'Star96', '["table_service", "central"]', 'Sci-Fi', 'Progressive Slots', '["re_spins", "megaways"]', 345.88, 2.79, 94.56, 1),
(97, 'Adventure Ahead', 0, 88.44, 'Star97', '["bar", "central"]', 'Adventure', 'Megaways', '["scatter_symbols", "stacked_wilds"]', 284.56, 3.14, 92.98, 0),
(98, 'Pharaoh\s Legacy', 0, 104.67, 'Star98', '["walkway_adjacent", "entrance"]', 'Egyptian', 'Themed Slots', '["bonus_rounds", "walking_wilds"]', 256.44, 2.34, 91.50, 0),
(99, 'Royal Voyage', 1, 96.78, 'Star99', '["restaurant", "bar"]', 'Pirate', 'Video Slots', '["vip_bonuses", "progressive_jackpot"]', 330.90, 3.89, 93.77, 1),
(100, 'Western Legacy', 1, 87.33, 'Star100', '["decoration", "walkway_adjacent"]', 'Wild West', '3D Slots', '["re_spins", "scatter_symbols"]', 250.45, 2.23, 89.67, 1),
(101, 'Mystic Realms', 0, 79.45, 'Star101', '["bar", "entrance"]', 'Fantasy', 'Bonus Slots', '["adjacent_pays", "seasonal_features"]', 377.56, 2.10, 93.25, 0),
(102, 'Galactic Wealth', 1, 92.67, 'Star102', '["central", "walkway_adjacent"]', 'Sci-Fi', 'Bonus Slots', '["re_spins", "sticky_wilds"]', 305.77, 2.99, 92.45, 0),
(103, 'Ocean Mysteries', 0, 110.34, 'Star103', '["table_service", "restaurant"]', 'Ocean', 'Progressive Slots', '["bonus_rounds", "scatter_symbols"]', 299.88, 3.50, 93.88, 1),
(104, 'Golden Adventure', 1, 85.22, 'Star104', '["bar", "central"]', 'Egyptian', '3D Slots', '["stacked_wilds", "bonus_rounds"]', 321.89, 3.04, 91.80, 1),
(105, 'Wild Quest', 0, 104.78, 'Star105', '["entrance", "decoration"]', 'Wild West', 'Themed Slots', '["progressive_jackpot", "wild_symbols"]', 243.90, 2.44, 89.99, 0),
(106, 'Treasure Hunt', 1, 96.34, 'Star106', '["bathroom", "bar"]', 'Pirate', 'Classic Slots', '["colossal_symbols", "bonus_rounds"]', 211.45, 2.77, 92.34, 0),
(107, 'Fantasy Quest', 0, 108.45, 'Star107', '["central", "walkway_adjacent"]', 'Fantasy', 'Megaways', '["free_spins", "scatter_symbols"]', 245.11, 2.88, 91.20, 1),
(108, 'Cosmic Blitz', 1, 103.99, 'Star108', '["table_service", "restaurant"]', 'Sci-Fi', 'Video Slots', '["re_spins", "vip_bonuses"]', 289.56, 3.89, 93.60, 0),
(109, 'Pirate Plunder', 0, 117.44, 'Star109', '["bar", "decoration"]', 'Pirate', '3D Slots', '["scatter_symbols", "stacked_wilds"]', 255.77, 3.14, 92.10, 1),
(110, 'Pharaohs Treasure', 1, 94.89, 'Star110', '["restaurant", "central"]', 'Egyptian', 'Progressive Slots', '["walking_wilds", "re_spins"]', 267.45, 2.77, 89.99, 0),
(111, 'Western Trails', 0, 85.99, 'Star111', '["table_service", "bathroom"]', 'Wild West', 'Classic Slots', '["vip_bonuses", "adjacent_pays"]', 321.23, 3.45, 91.99, 1),
(112, 'Jungle Safari', 1, 92.88, 'Star112', '["bar", "central"]', 'Jungle', 'Themed Slots', '["free_spins", "walking_wilds"]', 355.22, 3.20, 90.10, 0),
(113, 'Lost Relics', 0, 109.12, 'Star113', '["walkway_adjacent", "restaurant"]', 'Adventure', 'Bonus Slots', '["scatter_symbols", "wild_symbols"]', 311.67, 3.55, 93.77, 1),
(114, 'Mystic Jungle', 1, 87.33, 'Star114', '["decoration", "bar"]', 'Jungle', 'Megaways', '["stacked_wilds", "bonus_rounds"]', 299.44, 2.44, 91.40, 0),
(115, 'Golden Galaxy', 0, 116.89, 'Star115', '["restaurant", "table_service"]', 'Sci-Fi', 'Progressive Slots', '["re_spins", "scatter_symbols"]', 288.33, 3.77, 92.15, 1),
(116, 'Oceans Depths', 1, 95.99, 'Star116', '["bar", "central"]', 'Ocean', 'Themed Slots', '["wild_symbols", "vip_bonuses"]', 321.90, 2.33, 91.80, 0),
(117, 'Fantasy Isles', 0, 100.45, 'Star117', '["walkway_adjacent", "restaurant"]', 'Fantasy', 'Classic Slots', '["scatter_symbols", "walking_wilds"]', 344.22, 2.45, 92.10, 1),
(118, 'Cosmic Victory', 1, 110.12, 'Star118', '["table_service", "bathroom"]', 'Sci-Fi', '3D Slots', '["bonus_rounds", "re_spins"]', 254.56, 3.22, 93.99, 0),
(119, 'Pirate Gold', 0, 87.88, 'Star119', '["central", "bar"]', 'Pirate', 'Megaways', '["stacked_wilds", "scatter_symbols"]', 311.34, 3.55, 91.60, 1)
]

# updating coordinates
coordinates = [
(1, 17.97, 11.66), (2, 28.05, 8.26), (3, 28.05, 15.69), (4, 11.84, 32.55), (5, 11.84, 35.32),
(6, 11.84, 37.84), (7, 11.84, 40.35), (8, 11.84, 42.87), (9, 11.84, 45.26), (10, 11.84, 47.65),
(11, 11.84, 50.17), (12, 11.84, 52.68), (13, 11.84, 55.08), (14, 11.84, 57.47), (15, 11.84, 59.98),
(16, 11.84, 62.63), (17, 11.84, 65.14), (18, 11.84, 67.41), (19, 23.67, 37.58), (20, 23.67, 39.97),
(21, 23.67, 62.37), (22, 23.67, 64.89), (23, 30.68, 37.58), (24, 30.68, 39.97), (25, 30.68, 62.37),
(26, 30.68, 64.89), (27, 26.96, 35.07), (28, 26.96, 42.37), (29, 26.96, 59.98), (30, 26.96, 67.28),
(31, 23.67, 49.29), (32, 23.67, 52.68), (33, 29.81, 49.29), (34, 29.81, 52.68), (35, 30.03, 74.08),
(36, 30.03, 76.59), (37, 30.03, 79.24), (38, 30.03, 81.63), (39, 30.03, 84.14), (40, 30.03, 86.66),
(41, 30.03, 89.05), (42, 44.27, 2.6), (43, 48.44, 2.6), (44, 53.04, 2.6), (45, 57.42, 2.6),
(46, 61.81, 2.6), (47, 65.75, 2.6), (48, 47.78, 11.54), (49, 60.27, 11.54), (50, 51.72, 9.65),
(51, 55.89, 9.65), (52, 51.72, 13.42), (53, 55.89, 13.42), (54, 44.27, 21.48), (55, 48.44, 21.48),
(56, 52.60, 21.48), (57, 56.98, 21.48), (58, 61.37, 21.48), (59, 73.86, 6.38), (60, 73.86, 8.89),
(61, 73.86, 11.28), (62, 73.86, 13.80), (63, 73.86, 16.19), (64, 73.86, 18.71), (65, 73.86, 21.22),
(66, 44.27, 33.05), (67, 48.66, 33.05), (68, 52.60, 33.05), (69, 57.20, 33.05), (70, 61.59, 33.05),
(71, 65.53, 33.05), (72, 70.57, 33.05), (73, 74.74, 33.05), (74, 47.12, 47.02), (75, 72.77, 47.02),
(76, 51.29, 45.13), (77, 55.67, 45.13), (78, 60.05, 45.13), (79, 64.00, 45.13), (80, 68.38, 45.13),
(81, 51.29, 49.04), (82, 55.67, 49.04), (83, 60.05, 49.04), (84, 64.00, 49.04), (85, 68.38, 49.04),
(86, 52.82, 62.00), (87, 59.40, 62.00), (88, 52.82, 71.18), (89, 59.18, 71.18), (90, 52.60, 80.49),
(91, 59.18, 80.49), (92, 52.16, 89.43), (93, 59.00, 89.65), (94, 75.18, 64.01), (95, 81.53, 64.01),
(96, 75.18, 67.53), (97, 81.09, 67.53), (98, 73.64, 76.34), (99, 82.63, 76.34), (100, 78.24, 74.08),
(101, 78.03, 78.86), (102, 74.52, 84.90), (103, 80.66, 84.90), (104, 74.74, 88.42), (105, 80.66, 88.55),
(106, 94.90, 60.23), (107, 94.90, 62.63), (108, 94.90, 65.27), (109, 94.90, 67.66), (110, 94.90, 70.18),
(111, 94.90, 72.57), (112, 94.90, 74.96), (113, 94.90, 77.60), (114, 94.90, 79.87), (115, 94.90, 82.38),
(116, 94.90, 84.90), (117, 94.90, 87.42), (118, 94.90, 89.93), (119, 94.90, 92.45)
]

with open('UIX/static/js/db.sql', 'r') as f:
    sql = f.read()

try:
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    sqlite_new_query = """INSERT OR REPLACE INTO slot_machines (
        machine_id, name, availability, average_session, location, location_features,
        game_theme, game_type, game_features, maximum_bet, minimum_bet, rtp, reward_program
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.executemany(sqlite_new_query, updated_slot_machines)

    # Update coordinates for each machine
    for machine_id, top, left in coordinates:
        cursor.execute("""
            UPDATE slot_machines
            SET top = ?, left = ?
            WHERE machine_id = ?;
        """, (top, left, machine_id))

    # Commit the changes
    connection.commit()
    print("Coordinates updated successfully.")

    # Verify updates (optional)
    cursor.execute("SELECT machine_id, name, top, left FROM slot_machines;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
