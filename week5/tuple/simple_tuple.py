def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    smallest_likelihood = likelihood()
    return f"Minimum likelihood of falling: {smallest_likelihood}%"


if __name__ == "__main__":
    print(run_task1())
