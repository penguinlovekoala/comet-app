import pickle
import random
import sys
from pprint import pprint
from glob import glob
from data_loading_functions import CSVLoader, JSONSaver
from params import Parameters

random.seed(42)

class AtomDataSampler:
    def __init__(self):
        self.target_name = "atomic" 
        self.num_samples = Parameters.num_samples
        self.target_type = Parameters.target_type
        self.name_type_dict = Parameters.name_type2dir
        self.name_type = f"{self.target_name}|{self.target_type}"
        self.dir_ = Parameters.data_dir + self.target_name + "/"
        self.dir_ += self.name_type_dict[self.name_type]

    def __call__(self):
        csv_loader = CSVLoader(self.dir_)
        content = csv_loader()
        header_list, content = content[0], content[1:]

        line_dict_list = []
        for line in content:
            line_dict = dict()
            for idx, header in enumerate(header_list):
                assert header not in line_dict
                line_dict[header] = line[idx]
            line_dict_list.append(line_dict)
        
        random.shuffle(line_dict_list)
        
        return line_dict_list[:self.num_samples]


if __name__ == "__main__":
    sampler = AtomDataSampler()
    data_samples = sampler()
    for idx, data_sample in enumerate(data_samples):
        print("-"*10)
        print(f"Data No.{idx+1}")
        pprint(data_sample)
        print("-"*10)

