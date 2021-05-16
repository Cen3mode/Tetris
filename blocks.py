class Block :
    def __init__(self, block_color : int, block_offset : int, block : list) :
        self.block_color = block_color
        self.block_offset = block_offset

block_0_color = 1
block_0_offset = 0
block_0 = [[0,block_0_color,0,0],
           [0,block_0_color,0,0],
           [0,block_0_color,0,0],
           [0,block_0_color,0,0]]

block_1_color = 2
block_1_offset = -1
block_1 = [[0,0,0,0],
           [0,block_1_color,0,0],
           [0,block_1_color,block_1_color,block_1_color],
           [0,0,0,0]]

block_2_color = 3
block_2_offset = -1
block_2 = [[0,0,0,0],
           [0,0,block_2_color,0],
           [block_2_color,block_2_color,block_2_color,0],
           [0,0,0,0]]

block_3_color = 4
block_3_offset = -1
block_3 = [[0,0,0,0],
           [0,block_3_color,block_3_color,0],
           [0,block_3_color,block_3_color,0],
           [0,0,0,0]]

block_4_color = 5
block_4_offset = -1
block_4 = [[0,0,0,0],
           [0,block_4_color,block_4_color,0],
           [block_4_color,block_4_color,0,0],
           [0,0,0,0]]

block_5_color = 6
block_5_offset = -1
block_5 = [[0,0,0,0],
           [0,block_5_color,block_5_color,0],
           [0,0,block_5_color,block_5_color],
           [0,0,0,0]]

block_6_color = 7
block_6_offset = -1
block_6 = [[0,0,0,0],
           [0,block_6_color,0,0],
           [block_6_color,block_6_color,block_6_color,0],
           [0,0,0,0]]

startOffsetTable = [block_0_offset, block_1_offset, block_2_offset, block_3_offset ,block_4_offset ,block_5_offset, block_6_offset]
colorTable = [(0,0,0), (0, 255, 255), (0, 0, 255), (255, 0, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (255, 165, 0)]
blockSet = [block_0, block_1, block_2, block_3, block_4, block_5, block_6]

nesFrame = 1000/48
fallSpeed = [nesFrame*48, nesFrame*43, nesFrame*38, nesFrame*33, nesFrame*28, nesFrame*23, nesFrame*18, nesFrame*13, nesFrame*8, nesFrame*6]