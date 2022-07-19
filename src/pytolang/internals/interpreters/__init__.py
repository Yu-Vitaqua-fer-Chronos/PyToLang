from dataclasses import dataclass
from enum import Enum, auto as eauto

class BlockType:
    """This class is used as labels for the types of `Block`s, allowing for the API to easily let you know what type of block you're dealing with."""
    FILE = eauto()
    FUNC = eauto()
    CLASS = eauto()
    IF = eauto()
    WHILE_LOOP = eauto()
    FOR_LOOP = eauto()
    ASSIGNMENT = eauto()
    MATCH = eauto()


@dataclass
class Block:
    """A `Block` will represent a literal block of code, this can be the initial block, a block for if statements, classes or other types."""
    block_type:BlockType