#alejandra cabrera - 1066921
import copy
from src.world_cup_csp import WorldCupCSP
from src.data import TEAMS, GROUPS

def run_solver(debug=False, preassign_pots_1_2=True):
    """
    Ejecuta el solver CSP para encontrar una asignación válida de equipos a grupos.
    :param debug: Activa las trazas de depuración.
    :param preassign_pots_1_2: Si es True, preasigna de forma secuencial los bombos 1 y 2
                               para simplificar el problema.
    :return: Diccionario con la asignación final o None si no hay solución.
    """
    csp = WorldCupCSP(TEAMS, GROUPS, debug=debug)

    initial_assignment = {}

    if preassign_pots_1_2:
        # Preasignar bombo 1 a los grupos A-L.
        pot_1_teams = [t for t, info in TEAMS.items() if info["pot"] == 1]
        pot_2_teams = [t for t, info in TEAMS.items() if info["pot"] == 2]

        # Asignar los equipos del bombo 1 a los grupos (1 equipo por grupo)
        for i, team in enumerate(pot_1_teams):
            if i < len(GROUPS):
                group = GROUPS[i]
                initial_assignment[team] = group
                if debug:
                    print(f"Preasignado Bombo 1: {team} -> Grupo {group}")

        # Asignar los equipos del bombo 2 a los grupos
        for i, team in enumerate(pot_2_teams):
            if i < len(GROUPS):
                group = GROUPS[i]
                # Verificamos si la asignación inicial es válida con is_valid_assignment
                if csp.is_valid_assignment(group, team, initial_assignment):
                    initial_assignment[team] = group
                    if debug:
                        print(f"Preasignado Bombo 2: {team} -> Grupo {group}")
                else:
                    if debug:
                        print(f"La preasignación del Bombo 2 falló para {team} en el Grupo {group}. Saltando preasignación estricta.")

    print("\nIniciando Solver CSP...")
    # Comenzar backtrack sin dominios
    # Inicializar los dominios primero.
    domains = copy.deepcopy(csp.domains)
    # Aplicar el forward checking con la asignación inicial para acotar el dominio inicial
    success, domains = csp.forward_check(initial_assignment, domains)
    if not success:
        if debug:
            print("Fallo en forward_check con la asignación inicial.")
        return None

    solution = csp.backtrack(initial_assignment, domains)

    return solution

def print_solution(solution):
    """
    Imprime la solución agrupada por cada uno de los grupos (A-L).
    """
    if not solution:
        print("No se encontró solución.")
        return

    print("\n=== Sorteo Final de la Copa Mundial 2026 ===")

    # Agrupar los equipos por grupo
    groups_dict = {g: [] for g in GROUPS}
    for team, group in solution.items():
        groups_dict[group].append(team)

    for group in GROUPS:
        print(f"\nGrupo {group}:")
        teams_in_group = groups_dict[group]

        # Ordenar equipos por bombo (del 1 al 4)
        teams_in_group.sort(key=lambda x: TEAMS[x]["pot"])

        for team in teams_in_group:
            info = TEAMS[team]
            print(f"  - {team} ({info['conf']}, Bombo {info['pot']})")

if __name__ == "__main__":
    solution = run_solver(debug=True)
    print_solution(solution)
