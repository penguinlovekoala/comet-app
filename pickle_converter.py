import pickle
from data_loading_functions import JSONSaver
from params import Parameters

class PickleConverter():
    def __init__(self, dir_):
        self.dir_ = dir_
        self.data_ = []

    def __call__(self):
        with open(self.dir_, 'rb') as f:
            self.data_ = pickle.load(f)

    def save_to_csv_file(self, save_dir):
        saver_ = JSONSaver(self.data_, save_dir)
        saver_()
        print("save_dir:", save_dir)


if __name__ == "__main__":
    pickle_dir = Parameters.pickle_dir
    json_save_dir = ".".join(pickle_dir.split(".")[:-1]) + ".json"
    converter = PickleConverter(pickle_dir)
    converter()
    converter.save_to_csv_file(json_save_dir)


