import amulet
from amulet.api.block import Block
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist
from amulet.utils.world_utils import block_coords_to_chunk_coords, chunk_coords_to_block_coords
import random

class MCAnalyzer:
    BOTTOM = -64
    TOP = 320
    CHUNK_SIZE = 16
    def __init__(self, world_path, version=("java", (1, 16, 2))):
        self.level = amulet.load_level(world_path)
        self.game_version = version

    def print_block_type(self, x, y, z):
        block_type = self.block_type(x, y, z)
        if isinstance(block_type, Block):
            print(f'({x},{y},{z}): {block_type}')
    
    def block_type(self, x, y, z):
        try:
            block, block_entity = self.level.get_version_block(
                x,  # x location
                y,  # y location
                z,  # z location
                "minecraft:overworld",  # dimension
                self.game_version
            )
        except:
            block = "None"
        return block
    
    def print_block_by_loc(self, x, y, z):
        try:
            block, block_entity = self.level.get_version_block(
                x,  # x location
                y,  # y location
                z,  # z location
                "minecraft:overworld",  # dimension
                self.game_version
            )
        except:
            block = "None"
        print(block)
        print(block_entity)
    
    def get_block_id():
        return

    def get_chunks_list(self, world="minecraft:overworld"):
        chunk_list = self.level.all_chunk_coords(world)
        return chunk_list

    def get_neighborhood(self, x, y, z):
        neighborhood = {}
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0:
                        continue  # Skip the original point itself
                    neighbor_x = x + dx
                    neighbor_y = y + dy
                    neighbor_z = z + dz
                    neighbor_location = (neighbor_x, neighbor_y, neighbor_z)
                    neighborhood[neighbor_location] = self.block_type(neighbor_x, neighbor_y, neighbor_z)
        return neighborhood

    def print_chunk_all_block_type(self, cx, cz):
        BOTTOM = -64
        TOP = 320
        CHUNK_SIZE = 16
        for bx in range(cx, cx+CHUNK_SIZE):
            for by in range(BOTTOM, TOP):
                for bz in range(cz, cz+CHUNK_SIZE):
                    self.print_block_type(bx, by, bz)

    def statistic_chunk(self, cx, cz):
        type_list = {}
        BOTTOM = -64
        TOP = 320
        CHUNK_SIZE = 16
        cx = cx*CHUNK_SIZE
        cz = cz*CHUNK_SIZE
        for bx in range(cx, cx+CHUNK_SIZE):
            for by in range(BOTTOM, TOP):
                for bz in range(cz, cz+CHUNK_SIZE):
                    block_type = self.block_type(bx, by, bz)
                    if block_type in type_list:
                        type_list[block_type] += 1
                    else:
                        type_list[block_type] = 1
        print(type_list)
    
    def statistic_level(self):
        type_list = {}
        chunk_list = self.get_chunks_list()
        for chunk in chunk_list:
            cx = chunk[0]*self.CHUNK_SIZE
            cz = chunk[1]*self.CHUNK_SIZE
            for bx in range(cx, cx+self.CHUNK_SIZE):
                for by in range(self.BOTTOM, self.TOP):
                    for bz in range(cz, cz+self.CHUNK_SIZE):
                        block_type = self.block_type(bx, by, bz)
                        if block_type in type_list:
                            type_list[block_type] += 1
                        else:
                            type_list[block_type] = 1
        print(type_list)
    
    def statistic_blocks(self, blocks):
        type_list = {}
        for loc, type in blocks.items():
            if type == "None":
                # print("\033[91m {}\033[00m" .format(f'ALERT: {loc} is None'))
                continue
            if type in type_list:
                type_list[type] += 1
            else:
                type_list[type] = 1
        return type_list

    def get_random_block_by_alt_range(self, bottom_y, top_y):
        chunk_list = list(self.get_chunks_list())
        random_chunk = random.choice(chunk_list)
        random_chunk_init_x = random_chunk[0] * self.CHUNK_SIZE
        random_chunk_init_z = random_chunk[1] * self.CHUNK_SIZE
        target_x = random.randrange(random_chunk_init_x, random_chunk_init_x+self.CHUNK_SIZE)
        target_y = random.randrange(bottom_y, top_y)
        target_z = random.randrange(random_chunk_init_z, random_chunk_init_z+self.CHUNK_SIZE)
        return (target_x, target_y, target_z), self.block_type(target_x, target_y, target_z)

    def get_random_block(self):
        return self.get_random_block_by_alt_range(self.BOTTOM, self.TOP)

    def get_n_random_blocks_by_alt(self, num:int, bottom_y, top_y):
        # if bottom_y < self.BOTTOM or bottom_y > self.TOP:
        #     bottom_y = self.BOTTOM
        # if top_y < self.BOTTOM or top_y > self.TOP:
        #     top_y = self.TOP

        random_blocks = {}
        for i in range(num):
            block_loc, block_type = self.get_random_block_by_alt_range(bottom_y, top_y)
            random_blocks[block_loc] = block_type
        return random_blocks

    def get_n_random_blocks(self, num:int):
        return self.get_n_random_blocks_by_alt(num, self.BOTTOM, self.TOP)
    
    def check_hide_block(self, x, y, z):
        neighborhood = self.get_neighborhood(x, y, z)
        if len(self.statistic_blocks(neighborhood)) > 1:
            return True
        else:
            return False
    
    def close(self):
        self.level.close()