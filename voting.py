import hashlib
import time

class Voter: 
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False

class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name
    
class Block:
    def __init__(self, index, voter_id, candidate_id, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.voter_id = voter_id
        self.candidate_id = candidate_id
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):   
        value = str(self.index) + str(self.timestamp) + self.voter_id + self.candidate_id + self.previous_hash
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.voters = {}
        self.candidates = {}

    def create_genesis_block(self):
        return Block(0, "Genesis", "None", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_candidate(self, candidate_id,candidate_name):
        if candidate_id in self.candidates:
            print("Candidate already exists.")
            return False
        
        self.candidates[candidate_id] = Candidate(candidate_id, candidate_name)
        print(f"Candidate {candidate_name} added successfully.")
        return True

    def add_voter(self, voter_id, voter_name):
        if voter_id in self.voters:
            print("Voter already exists.")
            return False
        
        self.voters[voter_id] = Voter(voter_id, voter_name)
        print(f"Voter {voter_name} added successfully.")
        return True

    def cast_vote(self, voter_id, candidate_id):
        if voter_id not in self.voters:
            print("Voter not found.")
            return False

        if candidate_id not in self.candidates:
            print("Candidate not found.")
            return False

        voter = self.voters[voter_id]

        if voter.has_voted:
            print("Voter has already cast their vote.")
            return False

        candidate = self.candidates[candidate_id]

        latest_block = self.get_latest_block()
        new_block = Block(
            len(self.chain),
            voter_id,
            candidate_id,
            latest_block.hash
        )
        self.chain.append(new_block)
        voter.has_voted = True
        print(f"Vote cast successfully for " f"{candidate.name} by {voter.name}.")
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != prev.hash:
                return False

        return True

    def count_votes(self):

        results = {}

        for candidate in self.candidates:
            results[candidate] = 0

        for block in self.chain[1:]:
            results[block.candidate_id] += 1

        return results

    def print_blockchain(self):
        print("\n=====Blockchain contents=====")

        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Voter ID: {block.voter_id}")
            print(f"Candidate ID: {block.candidate_id}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}\n")
            print("-" * 40)

if __name__ == "__main__":
    blockchain = Blockchain()

    while True:
        print("\n=====Voting Management System=====")
        print("1. Add Candidate")
        print("2. Add Voter")
        print("3. Cast Vote")
        print("4. Print Blockchain")
        print("5. Validate Chain")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            candidate_id = input("Enter candidate ID: ")
            candidate_name = input("Enter candidate name: ")
            blockchain.add_candidate(candidate_id, candidate_name)

        elif choice == "2":
            voter_id = input("Enter voter ID: ")
            voter_name = input("Enter voter name: ")
            blockchain.add_voter(voter_id, voter_name)

        elif choice == "3":
            voter_id = input("Enter voter ID: ")
            candidate_id = input("Enter candidate ID: ")
            blockchain.cast_vote(voter_id, candidate_id)

        elif choice == "4":
            blockchain.print_blockchain()

        elif choice == "5":
            if blockchain.is_chain_valid():
                print("Blockchain is valid.")
            else:
                print("Blockchain is not valid.")

        elif choice == "6":
            print("Exiting Voting Management System.")
            break

        else:
            print("Invalid choice, Please try again.")