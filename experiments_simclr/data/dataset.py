class TimeSeriesSimCLRDataset(Dataset):
    def __init__(self, data, transform=None):
        self.data = data
        self.transform = transform

    def __getitem__(self, idx):
        x = self.data[idx]
        x_i = self.transform(x)
        x_j = self.transform(x)
        return x_i, x_j

    def __len__(self):
        return len(self.data)
