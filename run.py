test_dataset_path = "test/testdata/cc_dataset.csv"

exec(open("src/scripts/train.py").read(),
    {'dataset_path': test_dataset_path})
