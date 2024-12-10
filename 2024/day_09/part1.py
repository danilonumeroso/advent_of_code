import re


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()

    blocks = {}
    spaces = {}
    block_id = 0
    for i in range(len(content)):
        if i % 2 == 0:
            blocks[block_id] = int(content[i])
        else:
            spaces[block_id] = int(content[i])
            block_id += 1

    return blocks, spaces


def can_be_moved_left(block_id, spaces):
    for s in [s for s in spaces.keys() if s < block_id]:
        if spaces[s] > 0:
            return True
    return False


def allocate(blocks, spaces):
    blocks_ids = list(blocks.keys())
    allocations = []
    current_space_id = 0
    for block_id in reversed(blocks_ids):
        if not can_be_moved_left(block_id, spaces):
            continue

        block = blocks[block_id]
        while block > 0 and current_space_id < len(spaces.keys()):
            allocations.append((block_id, min(block, spaces[current_space_id])))

            spaces[current_space_id], block = (
                spaces[current_space_id] - min(block, spaces[current_space_id]),
                block - min(block, spaces[current_space_id]),
            )

            if spaces[current_space_id] == 0:
                if current_space_id + 1 == block_id:
                    num_blocks = block
                    block = 0
                else:
                    num_blocks = blocks[current_space_id + 1]

                allocations.append((current_space_id + 1, num_blocks))
                current_space_id += 1

        if current_space_id > len(spaces.keys()):
            break

        if block_id > 0:
            spaces[block_id - 1] += blocks[block_id]

        if block_id in spaces:
            del spaces[block_id]

    return allocations


def main(blocks, spaces):
    start = blocks[0]

    res = 0
    allocations = allocate(blocks, spaces)

    for block_id, length in allocations:
        for _ in range(length):
            # print(f"start * block = {start} * {block_id} = {start * block_id}")
            res += start * block_id
            start += 1

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    blocks, spaces = read_file(file_path)
    result = main(blocks, spaces)
    print("Result:", result)
