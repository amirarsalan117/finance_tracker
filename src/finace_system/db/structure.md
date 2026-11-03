---
id: structure
aliases: []
tags: []
---
[Done]:User 1──n Ledger
[Done]:Ledger 1──n Account
[Done]:Ledger 1──n Category          (self-FK parent for subcategories)
[Done]:Account 1──n Transaction
Category 1──n Transaction
Category 1──n Budget          (unique: category + period)
Account 1──0..1 DebtTerms
Ledger 1──n SavingsGoal ──0..1── Account
