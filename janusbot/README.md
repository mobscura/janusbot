# Janusbot Source Code

This folder contains the main source code for janusbot.

## Project Breakdown

+------------------
| janusbot
| |
| |---------- bot           # telegram bot for convenient management and monitoring of the system
| |
| |---------- connector     # connectors to individual exchanges
| |
| |---------- core          # trading core for market making
| |
| |---------- logger        # handles logging functionality
| |
| |---------- model         # data models for managing DB migrations and market data structures
| |
| |---------- notifier      # sender of notifications, e.g., about completed transactions
| |
| |---------- templates     # templates for config files: general, strategy, and logging
| |
| |---------- user          # handles user-specific requests like balance, rates, market data
| |
+------------------