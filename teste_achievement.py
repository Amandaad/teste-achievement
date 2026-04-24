"""Módulo simples para gerenciar achievements."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Achievement:
    """Representa uma conquista desbloqueável."""

    name: str
    points: int


class AchievementTracker:
    """Controla achievements desbloqueados por um usuário."""

    def __init__(self) -> None:
        self._unlocked: list[Achievement] = []

    def unlock(self, achievement: Achievement) -> bool:
        """Desbloqueia uma conquista se ainda não existir.

        Retorna True quando a conquista é adicionada.
        Retorna False quando ela já estava desbloqueada.
        """
        if achievement in self._unlocked:
            return False
        self._unlocked.append(achievement)
        return True

    @property
    def total_points(self) -> int:
        """Total de pontos acumulados."""
        return sum(item.points for item in self._unlocked)


if __name__ == "__main__":
    tracker = AchievementTracker()
    tracker.unlock(Achievement("Primeiro passo", 10))
    tracker.unlock(Achievement("Mestre da consistência", 50))
    print(f"Pontos totais: {tracker.total_points}")
