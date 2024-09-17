CREATE TABLE pokemon (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    type1 VARCHAR(20) NOT NULL,
    type2 VARCHAR(20), 
    hp INT NOT NULL,
    attack INT NOT NULL,
    defense INT NOT NULL,
    special_attack INT NOT NULL,
    special_defense INT NOT NULL,
    speed INT NOT NULL,
    ability_id INT,  -- Link to abilities table
    FOREIGN KEY (ability_id) REFERENCES abilities(id)  -- Enforce relationship with abilities
);
CREATE TABLE moves (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    type VARCHAR(20) NOT NULL,
    power INT,
    accuracy DECIMAL(5,2), -- Accuracy as a percentage (e.g., 100.00 for 100%)
    category_id INT,
    effect VARCHAR(255),
    PP INT,
	FOREIGN KEY (category_id) REFERENCES move_categories(id)
);

CREATE TABLE move_categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE  -- 'Physical', 'Special', or 'Status'
);

CREATE TABLE abilities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    effect VARCHAR(255)
);
CREATE TABLE type_effectiveness (
    attacking_type VARCHAR(20) NOT NULL,
    defending_type VARCHAR(20) NOT NULL,
    effectiveness DECIMAL(3,2) NOT NULL,  -- e.g., 2.0 for super effective, 0.5 for not very effective
    PRIMARY KEY (attacking_type, defending_type)
);
CREATE TABLE pokemon_moves (
    pokemon_id INT,
    move_id INT,
    PRIMARY KEY (pokemon_id, move_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (move_id) REFERENCES moves(id)
);
CREATE TABLE items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    effect VARCHAR(255)
);
CREATE TABLE natures (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    increased_stat VARCHAR(20) NOT NULL,
    decreased_stat VARCHAR(20) NOT NULL
);
CREATE TABLE evs (
    pokemon_id INT,
    hp_ev INT DEFAULT 0,
    attack_ev INT DEFAULT 0,
    defense_ev INT DEFAULT 0,
    special_attack_ev INT DEFAULT 0,
    special_defense_ev INT DEFAULT 0,
    speed_ev INT DEFAULT 0,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);
CREATE TABLE ivs (
    pokemon_id INT,
    hp_iv INT DEFAULT 0,
    attack_iv INT DEFAULT 0,
    defense_iv INT DEFAULT 0,
    special_attack_iv INT DEFAULT 0,
    special_defense_iv INT DEFAULT 0,
    speed_iv INT DEFAULT 0,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);
CREATE TABLE pokemon_items (
    pokemon_id INT,
    item_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);
CREATE TABLE pokemon_natures (
    pokemon_id INT,
    nature_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
    FOREIGN KEY (nature_id) REFERENCES natures(id)
);
SELECT * FROM abilities;