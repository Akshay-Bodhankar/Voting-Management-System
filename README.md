# 🗳️ Voting Management System on a Simple Blockchain

A simple blockchain-based **Voting Management System** developed in Python. The project demonstrates how blockchain concepts can be used to record voting transactions in a tamper-evident chain.

## 📌 Overview

The system allows candidates and voters to be registered and votes to be recorded on a simple blockchain.

Each vote is stored as a block containing the voter and candidate information. Blocks are connected using cryptographic hashes, creating a chain that can be validated for integrity.

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
* Count votes for each candidate
* Validate blockchain integrity

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

This means voter `V001` voted for candidate `C001`.

## 📊 Vote Counting

The system counts votes by examining the `candidate_id` stored in each vote block.

For example:

```text
V001 → C001
V002 → C002
V003 → C001
V004 → C003
V005 → C001
```

The resulting vote count is:

```text
===== Vote Counts =====

C001 - Candidate A: 3 vote(s)
C002 - Candidate B: 1 vote(s)
C003 - Candidate C: 1 vote(s)
```

The Genesis block is excluded from the vote count because it does not represent an actual vote.

## 📋 Available Operations

The system provides the following menu:

```text
===== Voting Management System =====

1. Add Candidate
2. Add Voter
3. Cast Vote
4. Count Votes
5. Print Blockchain
6. Validate Chain
7. Exit
```

### 1. Add Candidate

Adds a candidate using:

* Candidate ID
* Candidate Name

Duplicate candidate IDs are not allowed.

### 2. Add Voter

Adds a voter using:

* Voter ID
* Voter Name

Duplicate voter IDs are not allowed.

### 3. Cast Vote

Records a vote for a registered candidate.

The system checks that:

* The voter exists.
* The candidate exists.
* The voter has not already voted.


### 4. Count Votes

Calculates and displays the total number of votes received by each candidate.

Example:

```text
C001 - Candidate A: 3 vote(s)
C002 - Candidate B: 1 vote(s)
C003 - Candidate C: 1 vote(s)
```


### 5. Print Blockchain

Displays the blocks stored in the blockchain, including:

* Index
* Timestamp
* Voter ID
* Candidate ID
* Previous Hash
* Hash

### 6. Validate Chain

Checks the integrity of the blockchain by verifying:

* The current block's hash.
* The recalculated hash of the current block.
* The previous hash stored in the current block.
* The hash of the previous block.

Example:

```text
Blockchain is valid.
```

### 7. Exit

Terminates the application.

## 🧪 Validation

The project includes validation for the following cases.

### Duplicate Candidate ID

```text
Candidate ID: C001
Candidate Name: Candidate C

Candidate ID already exists.
```

### Duplicate Voter ID

```text
Voter ID: V001
Voter Name: Another Person

Voter ID already exists.
```

### Double Voting

If a voter attempts to vote again:

```text
Voter ID: V001
Candidate ID: C002

Voter has already voted.
```

The rejected vote is not added to the blockchain.

### Invalid Voter

```text
Voter ID: V999
Candidate ID: C001

Voter not found.
```

### Invalid Candidate

```text
Voter ID: V006
Candidate ID: C999

Candidate not found.
```

### Invalid Menu Option

If an invalid menu option is entered:

```text
Invalid choice. Please try again.
```

## 🔗 Example Blockchain

A blockchain containing three votes may look like:

```text
===== Blockchain Contents =====

Index: 0
Voter ID: Genesis
Candidate ID: None
Previous Hash: 0
Hash: <genesis-hash>
----------------------------------------

Index: 1
Voter ID: V001
Candidate ID: C001
Previous Hash: <genesis-hash>
Hash: <block-1-hash>
----------------------------------------

Index: 2
Voter ID: V002
Candidate ID: C002
Previous Hash: <block-1-hash>
Hash: <block-2-hash>
----------------------------------------

Index: 3
Voter ID: V003
Candidate ID: C001
Previous Hash: <block-2-hash>
Hash: <block-3-hash>
----------------------------------------
```

The `Previous Hash` of each block should match the `Hash` of the block immediately before it.

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

### Prerequisites

Python 3 is required.

Check your Python version:

```bash
python --version
```

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

It focuses on fundamental blockchain concepts such as:

* Blocks
* Voting transactions
* Cryptographic hashing
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
* Candidate and voter management
* Input validation
* Prevention of duplicate voting
* Vote counting

## 👨‍💻 Author

**Akshay Bodhankar**

GitHub: `https://github.com/Akshay-Bodhankar`
