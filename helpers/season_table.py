import pandas as pd

def load_season_tables(parquet_file='data/serie_a_season_tables.parquet'):
    """
    Load the flattened parquet file and reconstruct the nested dictionary structure.
    Returns: {season: {round: DataFrame}}
    """
    # Read the parquet file
    df = pd.read_parquet(parquet_file)
    
    # Reconstruct the nested dictionary
    season_tables_loaded = {}
    
    for season in sorted(df['season'].unique()):
        season_tables_loaded[season] = {}
        season_df = df[df['season'] == season]
        
        for round_num in sorted(season_df['round'].unique()):
            # Get the table for this specific season and round
            table = season_df[season_df['round'] == round_num].copy()
            
            season_tables_loaded[season][round_num] = table
    
    return season_tables_loaded


def calculate_table_for_round(df_matches: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate league table based on matches provided.
    df_matches should contain all matches up to and including the target round.
    """
    teams = pd.unique(df_matches[['team', 'opponent']].values.ravel('K'))
    
    # Initialize table
    table = pd.DataFrame({
        'team': teams,
        'played': 0,
        'w': 0,
        'd': 0,
        'l': 0,
        'points': 0,
        'gf': 0,
        'ga': 0,
        'gd': 0,
        'xg_for': 0.0,
        'xg_against': 0.0
    })
    
    # Process each match
    for _, match in df_matches.iterrows():
        home_team = match['team']
        away_team = match['opponent']
        result = match['result']
        
        # Handle NaN values for xG
        xg = 0.0 if pd.isna(match['xg']) else match['xg']
        xga = 0.0 if pd.isna(match['xga']) else match['xga']
        
        # Update matches played
        table.loc[table['team'] == home_team, 'played'] += 1
        table.loc[table['team'] == away_team, 'played'] += 1
        
        # Update goals
        table.loc[table['team'] == home_team, 'gf'] += match['gf']
        table.loc[table['team'] == home_team, 'ga'] += match['ga']
        table.loc[table['team'] == away_team, 'gf'] += match['ga']
        table.loc[table['team'] == away_team, 'ga'] += match['gf']
        
        # Update xG
        table.loc[table['team'] == home_team, 'xg_for'] += xg
        table.loc[table['team'] == home_team, 'xg_against'] += xga
        table.loc[table['team'] == away_team, 'xg_for'] += xga
        table.loc[table['team'] == away_team, 'xg_against'] += xg
        
        # Update points and W/D/L
        if result == 'W':  # Home win
            table.loc[table['team'] == home_team, 'points'] += 3
            table.loc[table['team'] == home_team, 'w'] += 1
            table.loc[table['team'] == away_team, 'l'] += 1
        elif result == 'L':  # Away win
            table.loc[table['team'] == away_team, 'points'] += 3
            table.loc[table['team'] == away_team, 'w'] += 1
            table.loc[table['team'] == home_team, 'l'] += 1
        elif result == 'D':  # Draw
            table.loc[table['team'] == home_team, 'points'] += 1
            table.loc[table['team'] == away_team, 'points'] += 1
            table.loc[table['team'] == home_team, 'd'] += 1
            table.loc[table['team'] == away_team, 'd'] += 1
    
    # Calculate goal difference
    table['gd'] = table['gf'] - table['ga']
    
    # Sort by points, then goal difference, then goals scored
    table = table.sort_values(
        by=['points', 'gd', 'gf'], 
        ascending=[False, False, False]
    ).reset_index(drop=True)
    
    # Add position column
    table.insert(0, 'pos', range(1, len(table) + 1))
    
    return table


def generate_all_season_tables(df: pd.DataFrame) -> dict:
    """
    Generate tables for all seasons and all rounds.
    Returns a nested dictionary: {season: {round: table_dataframe}}
    """
    all_tables = {}
    seasons = sorted(df['season'].unique())
    
    for season in seasons:
        print(f"Processing season {season}...")
        season_data = df[df['season'] == season].copy()
        
        # Exclude round 0 (play-offs)
        season_data = season_data[season_data['round'] > 0]
        
        rounds = sorted(season_data['round'].unique())
        all_tables[season] = {}
        
        for current_round in rounds:
            # Get all matches up to and including current round
            matches_until_round = season_data[season_data['round'] <= current_round]
            
            # Calculate table
            table = calculate_table_for_round(matches_until_round)
            table['round'] = current_round
            table['season'] = season
            
            all_tables[season][current_round] = table
        
        print(f"  ✓ Generated {len(rounds)} tables for season {season}")
    
    return all_tables