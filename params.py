class Parameters:
    possible_names = ["atom", "conceptnet"]
    possible_types = ["train", "dev", "test"]
    target_name = "atom"
    target_type = "test"
    random_sampling = True
    atom_dir = "../data/atomic/"
    conceptnet_dir = "../data/conceptnet/"
    save_to_file = True
    save_dir = f"../data/samples/{target_name}_{target_type}_sample.txt"
    name_type2dir = {
            "atom|train": "v4_atomic_trn.csv",
            "atom|dev": "v4_atomic_trn.csv",
            "atom|test": "v4_atomic_trn.csv",
            "conceptnet|train": "",
            "conceptnet|dev": "",
            "conceptnet|test": "",
    }

