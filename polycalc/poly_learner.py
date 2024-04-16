import torch, numpy as np, matplotlib.pyplot as plt, torch.nn as nn, torch.nn.functional as F, torch.autograd.profiler as profiler


class PolyLearner(nn.Module):

    def __init__(self, input_dim, output_dim, max_degree, device=None, dtype=torch.float32):

        super(PolyLearner, self).__init__()

        self.input_dim = input_dim
        self.output_dim = output_dim
        self.max_degree = max_degree
        self.dtype = dtype

        if device is not None:
            self.device = torch.device(device)
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        elif torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        print(f"Using device: {self.device}")

        self.model = nn.Sequential(
            nn.Linear(input_dim, 124),
            nn.ReLU(),
            nn.Linear(124, 124),
            nn.ReLU(),
            nn.Linear(124, (max_degree)*output_dim),
        ).to(self.device)
        
    
    def forward(self, X):

        # linear output to represent the coefficients of the polynomial
        L = self.model(X)
        return L


    def fit(self, X, Y, val_x=None, val_y=None, epochs=100, lr=0.01, batch_size=32, patience=10, verbose=False):

        self.to(self.device)
        X = X.to(self.device, self.dtype)
        Y = Y.to(self.device, self.dtype)

        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)

        dataset = torch.utils.data.TensorDataset(X, Y)
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

        best_loss = float('inf')
        early_stop_counter = 0

        if val_x is not None:
            val_X = val_x.to(self.device, self.dtype)
            val_Y = val_y.to(self.device, self.dtype)

        for epoch in range(epochs):

            running_loss = 0.0

            for x, y in dataloader:

                optimizer.zero_grad()
                outputs = self(x)
                loss = criterion(outputs, y)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

            if val_x is not None:
                with torch.no_grad():
                    val_outputs = self(val_X)
                    val_loss = criterion(val_outputs, val_Y)
                    print(f'Epoch {epoch + 1}, Loss: {running_loss / len(dataloader):.4f}, Val Loss: {val_loss.item():.4f}')
                    
                if val_loss < best_loss:
                    best_loss = val_loss
                    early_stop_counter = 0
                else:
                    early_stop_counter += 1

                if early_stop_counter >= patience:
                    if verbose:
                        print(f'Early stopping at epoch {epoch + 1}')
                    break
            else:
                if verbose:
                    print(f'Epoch {epoch + 1}, Loss: {running_loss / len(dataloader):.4f}')

    def predict(self, X):
        self.eval()
        X.to(self.device, self.dtype)

        return self(X).detach().cpu().numpy()
    
    def co(self):
        self.eval()
        return self.model[4].weight.detach().cpu().numpy()