# Datos realistas de la Copa Mundial 2026 para 48 equipos
# 12 equipos por bombo (Pot)
# Confederaciones: UEFA, CONMEBOL, CONCACAF, AFC, CAF, OFC
#alejandra cabrera - 1066921

TEAMS = {
    # BOMBO 1 (Cabezas de serie)
    "Argentina": {"conf": "CONMEBOL", "pot": 1},
    "France": {"conf": "UEFA", "pot": 1},
    "Brazil": {"conf": "CONMEBOL", "pot": 1},
    "England": {"conf": "UEFA", "pot": 1},
    "Belgium": {"conf": "UEFA", "pot": 1},
    "Croatia": {"conf": "UEFA", "pot": 1},
    "Netherlands": {"conf": "UEFA", "pot": 1},
    "Portugal": {"conf": "UEFA", "pot": 1},
    "Italy": {"conf": "UEFA", "pot": 1},
    "Spain": {"conf": "UEFA", "pot": 1},
    "USA": {"conf": "CONCACAF", "pot": 1},
    "Mexico": {"conf": "CONCACAF", "pot": 1},

    # BOMBO 2
    "Morocco": {"conf": "CAF", "pot": 2},
    "Switzerland": {"conf": "UEFA", "pot": 2},
    "Uruguay": {"conf": "CONMEBOL", "pot": 2},
    "Colombia": {"conf": "CONMEBOL", "pot": 2},
    "Germany": {"conf": "UEFA", "pot": 2},
    "Senegal": {"conf": "CAF", "pot": 2},
    "Japan": {"conf": "AFC", "pot": 2},
    "Iran": {"conf": "AFC", "pot": 2},
    "Peru": {"conf": "CONMEBOL", "pot": 2},
    "Denmark": {"conf": "UEFA", "pot": 2},
    "Canada": {"conf": "CONCACAF", "pot": 2},
    "South Korea": {"conf": "AFC", "pot": 2},

    # BOMBO 3
    "Austria": {"conf": "UEFA", "pot": 3},
    "Sweden": {"conf": "UEFA", "pot": 3},
    "Hungary": {"conf": "UEFA", "pot": 3},
    "Tunisia": {"conf": "CAF", "pot": 3},
    "Algeria": {"conf": "CAF", "pot": 3},
    "Egypt": {"conf": "CAF", "pot": 3},
    "Ecuador": {"conf": "CONMEBOL", "pot": 3},
    "Australia": {"conf": "AFC", "pot": 3},
    "Saudi Arabia": {"conf": "AFC", "pot": 3},
    "Costa Rica": {"conf": "CONCACAF", "pot": 3},
    "Panama": {"conf": "CONCACAF", "pot": 3},
    "Nigeria": {"conf": "CAF", "pot": 3},

    # BOMBO 4
    "Jordania": {"conf": "AFC", "pot": 4},
    "Cabo Verde": {"conf": "CAF", "pot": 4},
    "Ghana": {"conf": "CAF", "pot": 4},
    "Curazao": {"conf": "CONCACAF", "pot": 4},
    "Haiti": {"conf": "CONCACAF", "pot": 4},
    "New Zealand": {"conf": "OFC", "pot": 4},

    # 🔥 PLAYOFFS (CLAVE DEL LAB)
    "Playoff UEFA-A": {"conf": "UEFA", "pot": 4},
    "Playoff UEFA-B": {"conf": "UEFA", "pot": 4},
    "Playoff UEFA-C": {"conf": "UEFA", "pot": 4},
    "Playoff UEFA-D": {"conf": "UEFA", "pot": 4},

    "Playoff Inter-1": {"conf": "MULTI", "pot": 4},
    "Playoff Inter-2": {"conf": "MULTI", "pot": 4},
}

GROUPS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
