class Parameters:
    data_dir = "../data/"
    possible_types = ["train", "dev", "test"]
    target_type = "test"
    num_samples = 3
    random_sampling = True
    pickle_dir = "../results/gens/atomic-generation/chosen_ones/6.25e-05_adam_64_22000/test_top_k.gens"
    save_to_file = True
    save_dir = f"../data/samples/{target_type}_sample.txt"
    name_type2dir = {
            "atomic|train": "v4_atomic_trn.csv",
            "atomic|dev": "v4_atomic_trn.csv",
            "atomic|test": "v4_atomic_trn.csv",
            "conceptnet|train": "train100k.txt",
            "conceptnet|dev": "dev1.txt", # there is also "dev2.txt" but it is skipped.
            "conceptnet|test": "test.txt",
    }

