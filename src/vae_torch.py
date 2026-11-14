"""PyTorch VAE for log-normalised PBMC single-cell RNA-seq."""

import random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


class VAE(nn.Module):
    def __init__(self, n_genes=2006, latent_dim=16, hidden=(256, 64)):
        super().__init__()

        h1, h2 = hidden

        self.encoder = nn.Sequential(
            nn.Linear(n_genes, h1),
            nn.ReLU(),
            nn.Linear(h1, h2),
            nn.ReLU()
        )

        self.fc_mu = nn.Linear(h2, latent_dim)
        self.fc_logvar = nn.Linear(h2, latent_dim)

        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, h2),
            nn.ReLU(),
            nn.Linear(h2, h1),
            nn.ReLU(),
            nn.Linear(h1, n_genes)
        )

    def encode(self, x):
        h = self.encoder(x)
        return self.fc_mu(h), self.fc_logvar(h)

    def reparameterize(self, mu, logvar):
        if not self.training:
            return mu

        logvar = torch.clamp(logvar, min=-10, max=10)
        std = torch.exp(0.5 * logvar)
        return mu + std * torch.randn_like(std)

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        x_hat = self.decoder(z)
        return x_hat, mu, logvar


def vae_loss(x_hat, x, mu, logvar, beta=1.0):
    logvar = torch.clamp(logvar, min=-10, max=10)

    recon = F.mse_loss(
        x_hat, x, reduction="none"
    ).sum(dim=1).mean()

    kl = (
        -0.5 * (1 + logvar - mu.pow(2) - logvar.exp())
        .sum(dim=1)
    ).mean()

    total = recon + beta * kl
    return total, recon, kl
