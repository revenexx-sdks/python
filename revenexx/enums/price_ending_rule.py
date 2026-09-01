from enum import Enum

class PriceEndingRule(Enum):
    EXACT = "exact"
    WHOLE = "whole"
    ENDING_99 = "ending_99"
    ENDING_95 = "ending_95"
    ENDING_50 = "ending_50"
