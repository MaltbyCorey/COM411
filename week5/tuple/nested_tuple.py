def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run_task3():
    likelihoods = steps()
    good_steps = []
    bad_steps = []

    for count in likelihoods:
        if count[1] >= 50:
            bad_steps.append(count)
        else:
            good_steps.append(count)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")


if __name__ == "__main__":
    run_task3()
