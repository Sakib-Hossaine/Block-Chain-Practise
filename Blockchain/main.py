import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Blockchain.Backend.Core.blockchain import Blockchain

if __name__ == "__main__":
    print("Initializing Blockchain...")
    blockchain = Blockchain()

    blockchain.add_next_block()
    blockchain.add_next_block()

    blockchain.print()