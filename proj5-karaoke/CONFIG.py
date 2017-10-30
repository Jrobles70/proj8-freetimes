"""
Configuration of vocabulary game server.
Generated Sun Oct 29 15:29:26 PDT 2017
Edit to fit development or deployment environment.

"""

PORT=5000
DEBUG = True  # Set to False for production use
secret_key="3f4bb71c2e4e76c772bcd3976514958a"
success_at_count = 3  # How many matches before we declare victory? 
vocab="data/vocab.txt"  # CHANGE THIS to use another vocabulary file

