from teste_achievement import Achievement, AchievementTracker


def test_unlock_adds_points_once() -> None:
    tracker = AchievementTracker()
    ach = Achievement("Primeiro passo", 10)

    assert tracker.unlock(ach) is True
    assert tracker.unlock(ach) is False
    assert tracker.total_points == 10


def test_multiple_achievements_sum_points() -> None:
    tracker = AchievementTracker()

    tracker.unlock(Achievement("Primeiro passo", 10))
    tracker.unlock(Achievement("Mestre da consistência", 50))

    assert tracker.total_points == 60
