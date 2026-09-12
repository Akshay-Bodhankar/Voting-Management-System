# 🗳️ Voting Management System on a Simple Blockchain

A simple blockchain-based **Voting Management System** developed in Python. The project demonstrates how blockchain concepts can be used to record and maintain voting transactions in a tamper-evident chain.

## 📌 Overview

The system allows administrators to manage voters and candidates and record votes on a simple blockchain.

Each vote is stored as a block containing the voter and candidate information. Blocks are connected using cryptographic hashes, ensuring the integrity of the blockchain.

## ✨ Features

* Add candidates
* Add voters
* Cast votes
* Prevent duplicate candidate IDs
* Prevent duplicate voter IDs
* Prevent voters from voting more than once
* Store each vote as a blockchain block
* Generate SHA-256 hashes
* Link blocks using previous hashes
* Display blockchain contents
* Validate blockchain integrity
* Count votes for each candidate

## 🏗️ Blockchain Structure

Each block contains:

```text
Block
├── Index
├── Timestamp
├── Voter ID
├── Candidate ID
├── Previous Hash
└── Hash
```

The hash of each block is generated using its block data and the hash of the previous block.

```text
Genesis Block
      │
      ▼
   Block 1
      │
      ▼
   Block 2
      │
      ▼
   Block 3
```

This creates a chain where every block is linked to the block before it.

## 👥 Entities

### Voter

Each voter contains:

```text
Voter
├── Voter ID
├── Name
└── Has Voted
```

The `has_voted` property is used to prevent a voter from casting more than one vote.

### Candidate

Each candidate contains:

```text
Candidate
├── Candidate ID
└── Name
```

## 🔐 Hashing

The project uses **SHA-256** hashing through Python's `hashlib` module.

A block's hash is generated using:

```text
Index
Timestamp
Voter ID
Candidate ID
Previous Hash
```

Any modification to the stored block data will result in a different hash, allowing the blockchain integrity check to detect changes.

## 🗳️ Voting Process

The voting process follows these steps:

1. Register candidates.
2. Register voters.
3. A registered voter selects a registered candidate.
4. The system verifies that the voter has not already voted.
5. A new block is created for the vote.
6. The block is added to the blockchain.
7. The voter's `has_voted` status is updated.

Example:

```text
V001 → C001
```

means voter `V001` voted for candidate `C001`.

## 📊 Vote Counting

Votes are calculated by examining the candidate ID stored in each vote block.

For example:

```text
V001 → C001
V002 → C002
V003 → C001
```

Results:

```text
C001 - Candidate A: 2 votes
C002 - Candidate B: 1 vote
```

## ⛓️ Blockchain Validation

The blockchain can be validated by checking:

* The current block's hash
* The recalculated hash of the current block
* The previous hash stored in the current block
* The actual hash of the previous block

If any block has been modified, the validation will fail.

Example:

```text
Blockchain is valid.
```

## 📋 Available Operations

```text
1. Add Candidate
2. Add Voter
3. Cast Vote
4. Print Blockchain
5. Validate Chain
6. Exit
```

## 🛠️ Technologies Used

* Python
* Blockchain
* SHA-256
* Object-Oriented Programming
* Cryptographic Hashing

## 📁 Project Structure

```text
Voting-Management-System/
│
├── voting.py
└── README.md
```

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/Akshay-Bodhankar/Voting-Management-System.git
```

### Navigate to the Project

```bash
cd Voting-Management-System
```

### Run the Project

```bash
python voting.py
```

## ⚠️ Project Scope

This project is a **simple blockchain implementation for learning and demonstration purposes**.

It focuses on understanding fundamental blockchain concepts such as:

* Blocks
* Transactions
* Hashing
* Previous-hash linking
* Chain validation
* Data integrity

It is not intended to represent a production-ready electronic voting system.

## 🎯 Learning Objectives

The project demonstrates the practical implementation of:

* Blockchain data structures
* SHA-256 cryptographic hashing
* Block creation
* Genesis blocks
* Blockchain linking
* Blockchain validation
* Voting transactions
* Entity management
* Input validation
* Prevention of duplicate voting

## 👨‍💻 Author

**Akshay B**

GitHub: `https://github.com/Akshay-Bodhankar`
