"""
Configuration file for defining input/output paths.
"""
import os

INPUT_FILE = os.getenv("INPUT_FILE", "data/input.csv")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "output/tower_jump_analysis.csv")
