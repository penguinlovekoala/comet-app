from glob import glob
from data_loading_functions import CSVLoader
from params import Parameters
import sys

class AtomDataSampler:
    def __init__(self):
        self.target_name = Parameters.target_name
        self.target_type = Parameters.target_type
        self.name_type_dict = Parameters.name_type2dir
        self.name_type = f"{self.target_name}|{self.target_type}"
        self.dir_ = Parameters.atom_dir
        self.dir_ += self.name_type_dict[self.name_type]

    def __call__(self):
        csv_loader = CSVLoader(self.dir_)
        content = csv_loader()
        print(len(content))
        print(type(content))
        sys.exit()

    def koala():
        pass


if __name__ == "__main__":
    sampler = AtomDataSampler()
    sampler()
