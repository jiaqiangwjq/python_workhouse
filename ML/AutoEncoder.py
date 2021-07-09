import torch.nn as nn

# 以下参数皆以 MNIST 数据集中的图片作为参考

class AutoEncoder(nn.Module):

    def __init__(self):
        super(AutoEncoder, self).__init__()

        self.encoder = nn.Sequential(
            nn.Linear(28*28, 100),
            nn.ReLU(True),
            nn.Linear(1000, 500),
            nn.ReLU(True),
            nn.Linear(500, 250),
            nn.ReLU(True),
            nn.Linear(250, 2),
        )

        self.decoder = nn.Sequential(
            nn.Linear(2, 250),
            nn.ReLU(True),
            nn.Linear(250, 500),
            nn.ReLU(True),
            nn.Linear(500, 1000),
            nn.ReLU(True),
            nn.Linear(1000, 28*28),
            nn.Tanh(),
        )
    
    def forward(self, x):

        x = self.encoder(x)
        x = self.decoder(x)
        return x