import pandas as pd
import sqlite3

# Constants
dbName = 'slot_machines.db'

# Modifiable lists, higher values = higher priority in sorting for revenue maximization
location_features_val = {
    'bar': 2,
    'bathroom': 2,
    'central': 3,
    'entrance': 3,
    'restaurant': 2,
    'table_service': 2,
    'decoration': 1,
    'walkway_adjacent': 3
}

game_features_val = {
    'progressive_jackpot': 5,
    'high_roller_spins': 5,
    'vip_bonuses': 5,  # Attached to loyalty program
    'jackpot_wheel': 4,
    'megaways': 4,
    'bonus_rounds': 4,
    'free_spins': 4,
    'multipliers': 3,
    'cascading_reels': 3,
    'symbol_transformations': 3,
    'colossal_symbols': 3,
    'split_symbols': 3,
    'pay_both_ways': 3,
    'sticky_wilds': 3,
    'stacked_wilds': 3,
    'walking_wilds': 3,
    'buy_feature': 3,
    'expanding_wilds': 2,
    'wild_symbols': 2,
    'scatter_symbols': 2,
    'random_wilds': 2,
    'pick_and_click': 2,
    'adjacent_pays': 2,
    're_spins': 2,  # Respin feature
    'gamble_feature': 1,
    'mystery_symbols': 1,
    'themed_bonus_rounds': 1,
    'seasonal_features': 1
}

game_type_val = {
    'Progressive Slots': 5,
    'Megaways': 4,
    'Bonus Slots': 4,
    'Themed Slots': 3,
    '3D Slots': 3,
    'Video Slots': 2,
    'Classic Slots': 1
}

game_theme_val = {
    'Adventure': 5,
    'Movie/TV': 5,
    'Mythology': 4,
    'Music': 4,
    'Luxury': 4,
    'Egyptian': 4,
    'Fantasy': 3,
    'Pirate': 3,
    'Wild West': 3,
    'Sci-Fi': 2,
    'Ocean': 2,
    'Jungle': 1,
    'Fruit': 1
}


# machine_id, availability, average_session, location, location_features, game_theme,
# game_type, game_features, maximum_bet, minimum_bet, rtp, reward_program

# Filter machines based on availability
# Stretch goal: I would eventually like to code this so it also factors in the machines
# in use nearby as that is also a revenue driver
def filterActive(slot_machines):
    return [machine for machine in slot_machines if machine['availability'] == True]


# Sort by average session time (Favour higher duration sessions)
def sortHigherSessions(slot_machines):
    return sorted(slot_machines, key=lambda x: x['average_session'])


# Sort by location features (Favour higher traffic areas) (Based on values present in location_feature_val table)
def sortLocationPreference(slot_machines, location_features_val):
    return sorted(slot_machines, key=lambda machine: location_features_val.get(machine['location_features'], 0),
                  reverse=True)


# Sort by game features (Favour high revenue features) (Based on values present in game_feature_val table)
def sortGameFeatures(slot_machines, game_features_val):
    return sorted(slot_machines, key=lambda machine: game_features_val.get(machine['game_features'], 0), reverse=True)


# Sort by bet (favour higher maximum bets, first sort by highest minimum bets)
def sortBetAmt(slot_machines):
    slot_machines = sorted(slot_machines, key=lambda x: x['minimum_bet'])
    return sorted(slot_machines, key=lambda x: x['maximum_bet'])


# Sort by game theme (favour higher popularity themes)
def sortGameTheme(slot_machines, game_theme_val):
    return sorted(slot_machines, key=lambda machine: game_theme_val.get(machine['game_theme'], 0))


# Sort by game type (favour higher revenue types)
def sortGameType(slot_machines, game_type_val):
    return sorted(slot_machines, key=lambda machine: game_type_val.get(machine['game_type'], 0))


# Sort by RTP (favour casino)
def sortCasRTP(slot_machines):
    return sorted(slot_machines, key=lambda x: x['rtp'], reverse=True)


# Stretch goal: Machine_Loyalty_Val
# Based on the sorted list, adds loyalty points.
# Recommendations = higher loyalty values, more incentive to continue playing
# def calcLoyalty(slot_machines):

# Main function to recommend slot machines based on availability and attributes
def calculateRecommendations(slot_machines):
    # Sort out all in use machines at the time of recommendation
    available_machines = filterActive(slot_machines)
    if available_machines:
        # Begin sorting by sort importance in revenue
        available_machines = sortGameType(available_machines, game_type_val)
        available_machines = sortGameFeatures(available_machines, game_features_val)
        available_machines = sortBetAmt(available_machines)
        available_machines = sortLocationPreference(available_machines, location_features_val)
        available_machines = sortGameTheme(available_machines, game_theme_val)
        available_machines = sortHigherSessions(available_machines)
        available_machines = sortCasRTP(available_machines)
        return available_machines
    else:
        print("No recommendations available.")
        return []

# Connect to available db and return dictionary for main
def sqlConnect(db):
    conn = sqlite3.connect(db)
    temp = "SELECT * FROM slot_machines"
    tempSlotData = pd.read_sql_query(temp, conn)
    slotData = tempSlotData.to_dict(orient='records')
    conn.close()
    
    return slotData

if __name__ == "__main__":
    # First connect to db and pull records into accessible dictionary
    slotData = sqlConnect(dbName)
    
    # Sort dictionary
    recommended_machines = calculateRecommendations(slotData)

    # Splice list to specified amount
    recommended_machines = recommended_machines[:10]

    with open("recommendations.txt", "w") as f:
        for machine in recommended_machines:
            print(f"{machine['machine_id']}, {machine['name']}, {machine['location']}", file=f)