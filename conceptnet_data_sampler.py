import pickle
import random
import sys
from pprint import pprint
from glob import glob
from data_loading_functions import TEXTLoader
from params import Parameters

random.seed(42)

class ConceptNetDataSampler:
    def __init__(self):
        self.target_name = "conceptnet" 
        self.num_samples = Parameters.num_samples
        self.target_type = Parameters.target_type
        self.name_type_dict = Parameters.name_type2dir
        self.name_type = f"{self.target_name}|{self.target_type}"
        self.dir_ = Parameters.data_dir + self.target_name + "/"
        self.dir_ += self.name_type_dict[self.name_type]

    def __call__(self):
        text_loader = TEXTLoader(self.dir_)
        content = text_loader()

        line_dict_list = []
        for idx, line in enumerate(content.split("\n")):
            if line:
                pass
            else:
                continue
            line_dict = dict()
            line = line.split("\t")
            rel_, subject_, object_, num_ = line
            num_ = int(num_)
            assert ((num_ == 1) or (num_ == 0)), (
                f"the number at the end should be 1 or 0, "
                f"but it is {num_} at line #{idx} "
                f"where the line is [{line}]"
            )
            # the 1 indicates positive samples that make sense
            # the 0 indicates negative samples that do not make sense
            line_dict = {
                    "subject": subject_,
                    "object": object_,
                    "relation": rel_,
                    "is_true_sample": (num_ == 1)
            }
            line_dict_list.append(line_dict)
        
        # random.shuffle(line_dict_list)
        return line_dict_list[:self.num_samples]


if __name__ == "__main__":
    sampler = ConceptNetDataSampler()
    data_samples = sampler()
    for idx, data_sample in enumerate(data_samples):
        print("-"*10)
        print(f"Data No.{idx+1}")
        pprint(data_sample)
        print("-"*10)

