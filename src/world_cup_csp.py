#alejandra cabrera - 1066921
import copy

class WorldCupCSP:
    def __init__(self, teams, groups, debug=False):
        self.teams = teams
        self.groups = groups
        self.debug = debug

        self.variables = list(teams.keys())
        self.domains = {team: list(groups) for team in self.variables}

    def get_team_confederation(self, team):
        return self.teams[team]["conf"]

    def get_team_pot(self, team):
        return self.teams[team]["pot"]

    # 🔥 VALIDACIÓN CORRECTA CSP FIFA
    def is_valid_assignment(self, group, team, assignment):
        conf = self.get_team_confederation(team)
        pot = self.get_team_pot(team)

        teams_in_group = [t for t, g in assignment.items() if g == group]

        # 🔹 Máximo 4 equipos por grupo
        if len(teams_in_group) >= 4:
            return False

        # 🔹 1 equipo por bombo
        for t in teams_in_group:
            if self.get_team_pot(t) == pot:
                return False

        # 🔹 Contar confederaciones
        conf_count = {}
        for t in teams_in_group:
            c = self.get_team_confederation(t)
            conf_count[c] = conf_count.get(c, 0) + 1

        # 🔥 PLAYOFF INTER-2 (CLAVE DEL LAB)
        if team == "Playoff Inter-2":
            # NO bloquear AFC → permite doble AFC (Grupo K)
            blocked = ["CONMEBOL", "CONCACAF"]

            for b in blocked:
                if conf_count.get(b, 0) >= 1:
                    return False

            return True

        # 🔥 PLAYOFF INTER-1
        if team == "Playoff Inter-1":
            blocked = ["CONMEBOL", "CAF", "OFC"]

            for b in blocked:
                if conf_count.get(b, 0) >= 1:
                    return False

            return True

        # 🔥 PLAYOFF UEFA
        if "Playoff UEFA" in team:
            if conf_count.get("UEFA", 0) >= 2:
                return False
            return True

        # 🔹 Regla UEFA normal
        if conf == "UEFA":
            if conf_count.get("UEFA", 0) >= 2:
                return False
        else:
            if conf_count.get(conf, 0) >= 1:
                return False

        return True

    # 🔥 FORWARD CHECKING
    def forward_check(self, assignment, domains):
        new_domains = copy.deepcopy(domains)

        for team in self.variables:
            if team not in assignment:
                for group in domains[team][:]:
                    if not self.is_valid_assignment(group, team, assignment):
                        new_domains[team].remove(group)

                if len(new_domains[team]) == 0:
                    return False, None

        return True, new_domains

    # 🔥 MRV
    def select_unassigned_variable(self, assignment, domains):
        unassigned = [v for v in self.variables if v not in assignment]
        return min(unassigned, key=lambda var: len(domains[var]))

    # 🔥 BACKTRACKING
    def backtrack(self, assignment, domains=None):
        if domains is None:
            domains = self.domains

        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment, domains)

        for value in domains[var]:
            if self.is_valid_assignment(value, var, assignment):

                new_assignment = assignment.copy()
                new_assignment[var] = value

                if self.debug:
                    print(f"Intentando: {var} -> Grupo {value}")

                success, new_domains = self.forward_check(new_assignment, domains)

                if success:
                    result = self.backtrack(new_assignment, new_domains)
                    if result:
                        return result

                if self.debug:
                    print(f"Backtracking en: {var}")

        return None
