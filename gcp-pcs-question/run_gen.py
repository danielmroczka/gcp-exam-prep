from base_generator import generate_files
from data_1_10 import DATA as DATA1
from data_11_20 import DATA as DATA2
from data_21_40 import DATA as DATA3
from data_41_60 import DATA as DATA4
from data_61_80 import DATA as DATA5
from data_81_100 import DATA as DATA6
from data_101_150 import DATA as DATA7
from data_151_187 import DATA as DATA8
from data_188_205 import DATA as DATA9
from data_206_240 import DATA as DATA10
from data_241_265 import DATA as DATA11
from data_266_361 import DATA as DATA12

if __name__ == "__main__":
    all_data = {}
    all_data.update(DATA1)
    all_data.update(DATA2)
    all_data.update(DATA3)
    all_data.update(DATA4)
    all_data.update(DATA5)
    all_data.update(DATA6)
    all_data.update(DATA7)
    all_data.update(DATA8)
    all_data.update(DATA9)
    all_data.update(DATA10)
    all_data.update(DATA11)
    all_data.update(DATA12)
    generate_files(all_data, "C:/workspace/gcp-pcs-question")
