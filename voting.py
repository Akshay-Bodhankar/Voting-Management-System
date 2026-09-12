import hashlib
import time

class Block:
    def __init__(self, index, voter_id, vote, previous_hash):
        self.index=index
        self.timestamp=time.time()
        self.voter_id=voter_id
        self.vote=vote
        self.previous_hash=previous_hash
        self.hash=self.calculate_hash()

    def calculate_hash(self):
        value=str(self.index) + str(self.timestamp) + self.voter_id + self.vote + self.previous_hash
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain=[self.create_genesis_block()]
        self.voters=set()
        self.candidates=set()

    def create_genesis_block(self):
        return Block(0, "Genesis", "None", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_candidate(self, candidate_name):
        self.candidates.add(candidate_name)

    def cast_vote(self, voter_id, candidate_name):
        if candidate_name not in self.candidates:
            print("Candidate not found.")
            return False
        if voter_id in self.voters:
            print("Voter has already voted.")
            return False

        latest_block=self.get_latest_block()
        new_block=Block(len(self.chain), voter_id, candidate_name, latest_block.hash)
        self.chain.append(new_block)
        self.voters.add(voter_id)
        print(f"Vote cast successfully for {candidate_name} by {voter_id}.")
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current=self.chain[i]
            prev=self.chain[i-1]

            if current.hash!=current.calculate_hash():
                return False

            if current.previous_hash !=prev.hash:
                return False

        return True

    def count_votes(self):

        results={}

        for candidate in self.candidates:
            results[candidate]=0

        for block in self.chain[1:]:
            results[block.vote]+=1

        return results

if __name__ == "__main__":
    blockchain=Blockchain()
    blockchain.add_candidate("Candidate A")
    blockchain.add_candidate("Candidate B")
    


    blockchain.cast_vote("voter1", "Candidate A")
    blockchain.cast_vote("voter2", "Candidate B")
    blockchain.cast_vote("voter1", "Candidate A")
    blockchain.cast_vote("voter3", "Candidate A")


    print("\nBlockchain valid: ", blockchain.is_chain_valid())

    print("\nVote counts:")
    for candidate, count in blockchain.count_votes().items():
        print(f"{candidate}: {count}")

    print("\nBlockchain contents:")
    for block in blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Voter ID: {block.voter_id}")
        print(f"Vote: {block.vote}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash[:10]}...")  # Print only the first 10 characters of the hash for brevity
        print("-" * 40)