import random
import matplotlib.pyplot as plt

num_simulations1 = 10000


def flip_coin(num_simulations: int) -> dict:
    counts = {i: 0 for i in range(11)}

    for _ in range(num_simulations):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads_count] += 1

    percentages = {
        k: round((v / num_simulations) * 100, 2)
        for k, v in counts.items()}
    return percentages


def draw_gaussian_distribution_graph(counts: dict) -> None:
    plt.plot(
        list(counts.keys()),
        list(counts.values()),
        linewidth=1
    )
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()


result = flip_coin(10000)
draw_gaussian_distribution_graph(result)
