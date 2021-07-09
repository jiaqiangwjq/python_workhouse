import torch.nn as nn

class DNN(nn.Module):

    def __init__(self):
        super(DNN, self).__init__()

        self.fc = nn.Sequential(
            nn.Linear(in_features, out_features),
            nn.ReLU(),
            nn.Linear(in_features, num_classes),
            )

    def forward(self, x):
        
        x = self.fc(x)

        return x

