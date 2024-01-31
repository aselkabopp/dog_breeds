import pandas as pd

breeds_information = pd.read_csv("dog_breeds/dog_breeds_info.csv")

breeds_information_lowercase = breeds_information.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

breeds_information_lowercase.to_csv("dog_breeds/dog_breeds_info_prepared.csv", index=False)