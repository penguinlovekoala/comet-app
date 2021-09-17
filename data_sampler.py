from glob import glob
from data_loading_functions import CSVLoader
from params import Parameters

class DataSampler:
    def __init__(self):
        self.atom_dir = "../data/atomic/"
        self.conceptnet_dir = "../data/conceptnet/"

    def __call__(self):
        csv_files = self.get_csv_files(self.atom_dir)
        print("koala")
        print(csv_files)

    def get_csv_files(self, dir_):
        files = glob(dir_ + "*.csv")
        return files

    def koala():
        pass


if __name__ == "__main__":
    data_sampler = DataSampler()
    data_sampler()
