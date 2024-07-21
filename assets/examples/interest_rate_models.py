import torch
from quantorch.models.interest_rate.vasicek_model import VasicekModel

spot_rate = torch.tensor(0.03)
kappa = torch.tensor(0.5)
theta = torch.tensor(0.04)
sigma = torch.tensor(0.01)
time = 365

model = VasicekModel(spot_rate, kappa, theta, sigma, time)
rates = model.simulate()
print(f'Interest Rates: {rates}')