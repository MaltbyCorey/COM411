def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task2():
    min_max = likelihood_min_max()
    print(f"Minimum likelihood of falling: {min_max[0]}%")
    print(f"Maximum likelihood of falling: {min_max[1]}%")


if __name__ == "__main__":
  run_task2()
