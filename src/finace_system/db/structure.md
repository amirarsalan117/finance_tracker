---
id: structure
aliases: []
tags: []
---
User 1──n Ledger
Ledger 1──n Account
Ledger 1──n Category          (self-FK parent for subcategories)
Account 1──n Transaction
Category 1──n Transaction
Category 1──n Budget          (unique: category + period)
Account 1──0..1 DebtTerms
Ledger 1──n SavingsGoal ──0..1── Account
