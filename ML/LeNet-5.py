import torch.nn as nn

class LeNet(nn.Module):

    def __init__(self):
        super(LeNet, self).__init__()

        '''
        以下参数皆以 MNIST 数据集中的图片作为参考
        [C, H, W] = [1, 28, 28] -> [6, 24, 24] -> [6, 12, 12] -> [16, 8, 8] -> [16, 4, 4]
        [n, 4, 4, 16] -> [n, 4x4x16] -> [n, 120] -> [n, 84] -> [n, 10]
        '''

        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=0),
            nn.MaxPool2d(kernel_size=2)
            )

        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0),
            nn.MaxPool2d(kernel_size=2)
            )

        self.fc = nn.Sequential(
            nn.Linear(in_features=16*4*4, out_features=120),
            nn.Linear(in_features=120, out_features=84),
            nn.Linear(in_features=84, out_features=10),
            )

    def forward(self, x):
        
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x