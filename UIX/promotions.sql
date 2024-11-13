CREATE TABLE promotions (
    promotion_id INTEGER PRIMARY KEY,
    promotion_tier INTEGER NOT NULL,
    promotion_name TEXT NOT NULL,
    reward_value REAL NOT NULL
);

-- Insert promotion data (3 promotions for each tier).
INSERT INTO promotions (promotion_id, promotion_tier, promotion_name, reward_value) VALUES
(1001, 1, 'Tier 1 - Welcome Bonus', 50.00),
(1002, 1, 'Tier 1 - Free Play', 100.00),
(1003, 1, 'Tier 1 - Referral Bonus', 75.00),
(2001, 2, 'Tier 2 - Loyalty Reward', 125.00),
(2002, 2, 'Tier 2 - Holiday Special', 200.00),
(2003, 2, 'Tier 2 - Birthday Gift', 250.00),
(3001, 3, 'Tier 3 - VIP Exclusive Offer', 300.00),
(3002, 3, 'Tier 3 - Premium Free Play', 375.00),
(3003, 3, 'Tier 3 - VIP Rewards', 400.00);
